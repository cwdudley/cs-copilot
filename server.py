"""
CS Copilot web server + simulation orchestrator.

Serves the browser frontend and manages the two-agent simulation entirely
in-process — no separate terminal needed for the customer agent when using
the simulation buttons.

Routes
------
GET  /          → index.html
GET  /token     → LiveKit JWT for the browser (?room= defaults to cs-copilot)
POST /start-scenario  { "scenario": 0–9 }  → stops any running sim, starts a new one
POST /stop-scenario   → stops any running simulation

Direct copilot use (Connect button in the browser):
  Still requires agent.py running separately:
    .venv/Scripts/python.exe agent.py dev
"""

import asyncio
import logging
import os
import random
import uuid

from aiohttp import web
from dotenv import load_dotenv
from livekit import rtc
from livekit.agents import AgentSession
from livekit.agents.utils import http_context
from livekit.agents.voice.room_io import RoomOptions
from livekit.api import AccessToken, VideoGrants
from livekit.plugins import groq, silero

from agent import Assistant
from customer_agent import CUSTOMER_SCENARIOS, CUSTOMER_VOICES, CustomerAgent

load_dotenv()
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("cs-server")

COPILOT_ROOM = "cs-copilot"
SIMULATION_ROOM = "cs-simulation"
PORT = 3000

# ── Simulation state ──────────────────────────────────────────────────────────

_sim_task = None  # currently running asyncio.Task, or None


def _make_token(identity: str, name: str, room: str) -> str:
    return (
        AccessToken()
        .with_identity(identity)
        .with_name(name)
        .with_grants(VideoGrants(room_join=True, room=room))
        .to_jwt()
    )


async def run_simulation(scenario_index: int, voice: str) -> None:
    """Run both the CS copilot and customer agents in cs-simulation room."""
    scenario = CUSTOMER_SCENARIOS[scenario_index % len(CUSTOMER_SCENARIOS)]
    logger.info(
        "▶ Simulation scenario %d: %s | customer voice: %s",
        scenario_index,
        scenario["name"],
        voice,
    )

    copilot_room = None
    customer_room = None

    try:
        lk_url = os.getenv("LIVEKIT_URL")

        # Subscribe to BOTH human and agent participants — without this,
        # an AgentSession ignores audio from other agents in the room.
        sim_room_opts = RoomOptions(
            participant_kinds=[
                rtc.ParticipantKind.PARTICIPANT_KIND_STANDARD,
                rtc.ParticipantKind.PARTICIPANT_KIND_AGENT,
            ],
        )

        # ── CS Copilot ────────────────────────────────────────────────────────
        copilot_room = rtc.Room()
        await copilot_room.connect(
            lk_url,
            _make_token("copilot-sim", "CS Copilot", SIMULATION_ROOM),
        )

        copilot_session = AgentSession(
            stt=groq.STT(model="whisper-large-v3-turbo"),
            llm=groq.LLM(model="llama-3.3-70b-versatile"),
            tts=groq.TTS(model="canopylabs/orpheus-v1-english", voice="diana"),
            vad=silero.VAD.load(),
            turn_handling={"endpointing": {"min_delay": 0.5, "max_delay": 5.0}},
        )
        await copilot_session.start(
            agent=Assistant(),
            room=copilot_room,
            room_options=sim_room_opts,
        )

        # ── Customer Agent ────────────────────────────────────────────────────
        customer_room = rtc.Room()
        await customer_room.connect(
            lk_url,
            _make_token("customer-sim", "Customer", SIMULATION_ROOM),
        )

        customer_session = AgentSession(
            stt=groq.STT(model="whisper-large-v3-turbo"),
            # 8B keeps the customer's 1-3 sentence persona fine and runs ~3x faster
            # than 70B, which frees CPU for Silero VAD and avoids turn-detection stalls.
            llm=groq.LLM(model="llama-3.1-8b-instant"),
            tts=groq.TTS(model="canopylabs/orpheus-v1-english", voice=voice),
            vad=silero.VAD.load(),
            turn_handling={"endpointing": {"min_delay": 2.0, "max_delay": 5.0}},
        )
        await customer_session.start(
            agent=CustomerAgent(scenario["persona"]),
            room=customer_room,
            room_options=sim_room_opts,
        )

        # ── Kick off ──────────────────────────────────────────────────────────
        await copilot_session.say("Hey, I'm your CS copilot. What are you working on?")
        await asyncio.sleep(2.0)
        await customer_session.say(scenario["opening"])

        # Hold until cancelled
        await asyncio.Event().wait()

    except asyncio.CancelledError:
        logger.info("■ Simulation cancelled (scenario %d).", scenario_index)
    except Exception:
        logger.exception("Simulation error (scenario %d)", scenario_index)
    finally:
        if copilot_room:
            await copilot_room.disconnect()
        if customer_room:
            await customer_room.disconnect()
        logger.info("Simulation rooms disconnected.")


async def _stop_simulation() -> None:
    global _sim_task
    if _sim_task and not _sim_task.done():
        _sim_task.cancel()
        try:
            await _sim_task
        except (asyncio.CancelledError, Exception):
            pass
    _sim_task = None


# ── HTTP handlers ─────────────────────────────────────────────────────────────

async def handle_token(request):
    room = request.rel_url.query.get("room", COPILOT_ROOM)
    identity = f"user-{uuid.uuid4().hex[:8]}"
    token = (
        AccessToken()
        .with_identity(identity)
        .with_name("CS Leader")
        .with_grants(VideoGrants(room_join=True, room=room))
        .to_jwt()
    )
    return web.json_response({
        "token": token,
        "url": os.getenv("LIVEKIT_URL"),
        "room": room,
    })


async def handle_start_scenario(request):
    global _sim_task
    data = await request.json()
    scenario_index = int(data.get("scenario", 0))
    voice = random.choice(CUSTOMER_VOICES)

    await _stop_simulation()

    _sim_task = asyncio.create_task(run_simulation(scenario_index, voice))

    name = CUSTOMER_SCENARIOS[scenario_index % len(CUSTOMER_SCENARIOS)]["name"]
    return web.json_response({
        "ok": True,
        "scenario": scenario_index,
        "name": name,
        "voice": voice,
    })


async def handle_stop_scenario(request):
    await _stop_simulation()
    return web.json_response({"ok": True})


async def handle_index(request):
    return web.FileResponse("index.html")


# ── App ───────────────────────────────────────────────────────────────────────

async def _http_context_lifespan(app):
    """Open a shared aiohttp session so LiveKit plugins work outside a job context."""
    async with http_context.open():
        yield


app = web.Application()
app.cleanup_ctx.append(_http_context_lifespan)
app.router.add_get("/", handle_index)
app.router.add_get("/token", handle_token)
app.router.add_post("/start-scenario", handle_start_scenario)
app.router.add_post("/stop-scenario", handle_stop_scenario)

if __name__ == "__main__":
    print(f"CS Copilot server → http://localhost:{PORT}")
    web.run_app(app, host="localhost", port=PORT, print=None)
