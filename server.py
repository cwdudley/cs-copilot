"""
SuccessCOACHING Q&A web server.

Serves the browser frontend and issues LiveKit JWTs so the user can
connect and speak directly to the CS copilot agent.

Routes
------
GET  /        → index.html
GET  /token   → LiveKit JWT (?room= defaults to cs-copilot)

Run the copilot agent separately before opening the browser:
  .venv/Scripts/python.exe agent.py dev
"""

import logging
import os
import uuid

from aiohttp import web
from dotenv import load_dotenv
from livekit.api import AccessToken, VideoGrants

load_dotenv()
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("sc-server")

COPILOT_ROOM = "cs-copilot"
PORT = 3000


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


app = web.Application()
app.router.add_get("/", handle_index)
app.router.add_get("/token", handle_token)

if __name__ == "__main__":
    print(f"SuccessCOACHING Q&A → http://localhost:{PORT}")
    print("Run the agent in a second terminal: .venv/Scripts/python.exe agent.py dev")
    web.run_app(app, host="localhost", port=PORT, print=None)
