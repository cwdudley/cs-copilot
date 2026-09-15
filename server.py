"""
AM Coach web server — ElevenLabs Agents.

Serves the frontend and mints short-lived signed URLs so the browser can open a
conversation without ever seeing the API key.

There is no agent pipeline here. STT, LLM orchestration, TTS, and turn-taking
all run on ElevenLabs; this process only handles auth and static files.

Routes
------
GET  /            → index.html
GET  /signed-url  → { signed_url } for the provisioned agent

Run provision.py first to create the agent.
"""

import logging
import os

import aiohttp
from aiohttp import web
from dotenv import load_dotenv

load_dotenv()
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("am-coach")

API_BASE = "https://api.elevenlabs.io/v1"
API_KEY = os.getenv("ELEVENLABS_API_KEY")
AGENT_ID = os.getenv("ELEVENLABS_AGENT_ID")
# 3000 is commonly taken by other local dev servers; sharing an origin with
# another app's open tabs caused stale pages and confusing 404s.
PORT = int(os.getenv("PORT", "3100"))


async def handle_signed_url(request):
    """Mint a signed WebSocket URL. Expires after ~15 minutes."""
    if not API_KEY or not AGENT_ID:
        return web.json_response(
            {"error": "ELEVENLABS_API_KEY or ELEVENLABS_AGENT_ID missing. Run provision.py."},
            status=500,
        )

    session: aiohttp.ClientSession = request.app["http"]
    url = f"{API_BASE}/convai/conversation/get-signed-url?agent_id={AGENT_ID}"

    async with session.get(url, headers={"xi-api-key": API_KEY}) as resp:
        body = await resp.text()
        if resp.status != 200:
            logger.error("Signed URL request failed (%s): %s", resp.status, body)
            return web.json_response(
                {"error": "Could not get a signed URL", "detail": body},
                status=resp.status,
            )
        return web.json_response(await resp.json())


async def handle_index(request):
    # no-store so a reload always picks up UI changes during development.
    return web.FileResponse("index.html", headers={"Cache-Control": "no-store"})


async def _http_session(app):
    app["http"] = aiohttp.ClientSession()
    yield
    await app["http"].close()


app = web.Application()
app.cleanup_ctx.append(_http_session)
app.router.add_get("/", handle_index)
app.router.add_get("/signed-url", handle_signed_url)

if __name__ == "__main__":
    if not AGENT_ID:
        print("Warning: ELEVENLABS_AGENT_ID is not set. Run provision.py first.\n")
    print(f"AM Coach -> http://localhost:{PORT}")
    web.run_app(app, host="localhost", port=PORT, print=None)
