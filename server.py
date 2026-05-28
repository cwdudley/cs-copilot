"""
SuccessCOACHING Q&A web server.

Serves the browser frontend AND runs the CS copilot agent in-process —
one terminal only. No simulation, no scenario buttons.

Routes
------
GET  /        → index.html
GET  /token   → LiveKit JWT (?room= defaults to cs-copilot)
"""

import asyncio
import logging
import os
import uuid

from aiohttp import web
from dotenv import load_dotenv
from livekit import rtc
from livekit.agents import AgentSession
from livekit.agents.utils import http_context
from livekit.api import AccessToken, VideoGrants
from livekit.plugins import groq, silero

from agent import Assistant

load_dotenv()
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("sc-server")

COPILOT_ROOM = "cs-copilot"
PORT = 3000

_copilot_task = None


def _make_token(identity: str, name: str, room: str) -> str:
    return (
        AccessToken()
        .with_identity(identity)
        .with_name(name)
        .with_grants(VideoGrants(room_join=True, room=room))
        .to_jwt()
    )


async def run_copilot() -> None:
    room = None
    try:
        room = rtc.Room()
        await room.connect(
            os.getenv("LIVEKIT_URL"),
            _make_token("copilot", "CS Copilot", COPILOT_ROOM),
        )
        logger.info("Copilot connected to room: %s", COPILOT_ROOM)

        session = AgentSession(
            stt=groq.STT(model="whisper-large-v3-turbo"),
            llm=groq.LLM(model="llama-3.3-70b-versatile"),
            tts=groq.TTS(model="canopylabs/orpheus-v1-english", voice="diana"),
            vad=silero.VAD.load(),
            turn_handling={"endpointing": {"min_delay": 0.3, "max_delay": 5.0}},
        )
        await session.start(agent=Assistant(), room=room)

        greeted = False

        @room.on("participant_connected")
        def on_participant_connected(participant):
            nonlocal greeted
            if (
                participant.kind == rtc.ParticipantKind.PARTICIPANT_KIND_STANDARD
                and not greeted
            ):
                greeted = True
                asyncio.ensure_future(session.say("Hey, what can I help you with?"))

        @room.on("participant_disconnected")
        def on_participant_disconnected(participant):
            nonlocal greeted
            # Reset so the greeting plays again on reconnect
            still_connected = any(
                p.kind == rtc.ParticipantKind.PARTICIPANT_KIND_STANDARD
                for p in room.remote_participants.values()
            )
            if not still_connected:
                greeted = False

        await asyncio.Event().wait()

    except asyncio.CancelledError:
        logger.info("Copilot task cancelled.")
    except Exception:
        logger.exception("Copilot error")
    finally:
        if room:
            await room.disconnect()


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


async def handle_index(request):
    return web.FileResponse("index.html")


async def _http_context_lifespan(app):
    global _copilot_task
    async with http_context.open():
        _copilot_task = asyncio.create_task(run_copilot())
        yield
        if _copilot_task and not _copilot_task.done():
            _copilot_task.cancel()
            try:
                await _copilot_task
            except (asyncio.CancelledError, Exception):
                pass


app = web.Application()
app.cleanup_ctx.append(_http_context_lifespan)
app.router.add_get("/", handle_index)
app.router.add_get("/token", handle_token)

if __name__ == "__main__":
    print(f"SuccessCOACHING Q&A → http://localhost:{PORT}")
    web.run_app(app, host="localhost", port=PORT, print=None)
