# SuccessCOACHING Voice Copilot

A voice Q&A copilot for Customer Success leaders, built on [LiveKit Agents](https://docs.livekit.io/agents/), Groq (STT / LLM / TTS), and a browser UI.

Talk through renewals, account health, onboarding, expansion, and operational CS questions. The agent uses the full **SuccessCOACHING** methodology (TARO, lifecycle stages, health bands, churn tiers, renewals, expansion, and related frameworks) as its system prompt.

## Bring your own keys

This repo is **self-hosted** — there is no shared backend. Every developer runs the app locally with **their own** API credentials.

1. Create a [LiveKit Cloud](https://cloud.livekit.io/) project → copy the **WebSocket URL**, **API Key**, and **API Secret** from Project Settings.
2. Create a [Groq](https://console.groq.com/) account → create an **API key**.
3. Paste all four values into `.env` (see step 2 below).

The values in `.env.example` are placeholders only. Without real keys, the UI may load but **Connect** will fail.

## Quick start

**Prerequisites:** Python 3.10+, a LiveKit Cloud project, and a Groq API key (see above).

1. Clone and install:

   ```powershell
   git clone https://github.com/cwdudley/cs-copilot.git
   cd cs-copilot
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   pip install -r requirements.txt
   ```

2. Configure environment:

   ```powershell
   copy .env.example .env
   ```

   Edit `.env` and replace every placeholder with your real credentials:

   ```env
   LIVEKIT_URL=wss://YOUR-PROJECT.livekit.cloud
   LIVEKIT_API_KEY=your_livekit_api_key
   LIVEKIT_API_SECRET=your_livekit_api_secret
   GROQ_API_KEY=your_groq_api_key
   ROOM_NAME=cs-copilot
   PORT=3000
   ```

3. Run (one terminal):

   ```powershell
   .\.venv\Scripts\python.exe server.py
   ```

4. Open http://localhost:3000, click **Connect**, and allow microphone access.

The server serves the UI **and** runs the copilot agent in-process — no second terminal required.

Optional sanity check before running the app:

```powershell
.\.venv\Scripts\python.exe scripts\smoke_check.py
```

## How it works

```
Browser (index.html)  ←→  LiveKit room (cs-copilot)  ←→  Copilot agent (server.py)
     mic + audio              realtime WebRTC                    Groq STT → LLM → TTS
```

- The browser fetches a JWT from `/token` and joins the `cs-copilot` room.
- `server.py` connects the agent to the same room on startup.
- When you connect, the copilot greets you and responds to voice input.
- Transcripts appear in the UI via LiveKit's `lk.transcription` text stream.

## Project layout

| File | Purpose |
|------|---------|
| `index.html` | Browser UI — orb, status, transcript, Connect button |
| `server.py` | Web server, token endpoint, in-process copilot agent |
| `agent.py` | Agent definition, voice pipeline hooks, and web search tool |
| `config.py` | Environment loading and startup validation |
| `prompts/successcoaching.md` | Full SuccessCOACHING system prompt |
| `experiments/` | Archived simulation and voice-probing experiments |
| `.env.example` | Environment variable template |

## Branches

| Branch | Description |
|--------|-------------|
| **`main`** | SuccessCOACHING voice Q&A (this README) |
| **`simulated-attempt`** | Archived experiment — AI-vs-AI customer simulations with four scenario personas. Kept for reference; not actively maintained. |

To try the sim version:

```powershell
git checkout simulated-attempt
```

On that branch you may need both `server.py` and `agent.py dev` depending on the mode; see the UI on that branch for details. The `experiments/` folder on `main` preserves the exploratory files, but the supported app is the one-terminal Q&A flow.

## Notes

- **Groq rate limits:** The full SuccessCOACHING prompt is large (~2k+ tokens). On Groq's free tier you may hit per-minute token caps in longer conversations. Upgrading your Groq plan or trimming the prompt in `agent.py` helps if responses stall.
- **Conversation memory:** The agent keeps a sliding window of the last 12 turns to control token usage per request.
- **Web search:** The agent can call DuckDuckGo via the `search_web` tool for ad-hoc lookups during a session.

## Optional: standalone agent worker

`agent.py` can also run as a LiveKit Cloud worker (separate process):

```powershell
.\.venv\Scripts\python.exe agent.py dev
```

This is **not required** for local development on `main` — `server.py` already runs the agent. Use the standalone worker if you deploy agents to LiveKit Cloud's worker pool instead of in-process.

## Troubleshooting

| Symptom | Likely cause | Fix |
|---------|--------------|-----|
| `Connection failed` in the browser | Missing or placeholder `.env` values | Replace every value in `.env` with real LiveKit Cloud and Groq credentials — the template placeholders will not work |
| `ModuleNotFoundError` on startup | Dependencies not installed | Run `pip install -r requirements.txt` inside your activated venv |
| Page won't load at localhost:3000 | Server not running | Start `server.py` first; look for `SuccessCOACHING Q&A → http://localhost:3000` in the terminal |
| Connected but agent never replies | Invalid Groq key or rate limit | Check the terminal for Groq errors; free-tier Groq may stall on long conversations with the full prompt |
| `Copilot error` in terminal on startup | Bad LiveKit URL or API keys | Verify `LIVEKIT_URL` starts with `wss://` and key/secret match your LiveKit Cloud project |

**This repo does not include shared API keys.** You must create your own [LiveKit Cloud](https://cloud.livekit.io/) project and [Groq](https://console.groq.com/) account before the app will connect.
