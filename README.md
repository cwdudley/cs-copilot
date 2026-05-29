# SuccessCOACHING Voice Copilot

A voice Q&A copilot for Customer Success leaders, built on [LiveKit Agents](https://docs.livekit.io/agents/), Groq (STT / LLM / TTS), and a browser UI.

Talk through renewals, account health, onboarding, expansion, and operational CS questions. The agent uses the full **SuccessCOACHING** methodology (TARO, lifecycle stages, health bands, churn tiers, renewals, expansion, and related frameworks) as its system prompt.

## Quick start

**Prerequisites:** Python 3.10+, a [LiveKit Cloud](https://cloud.livekit.io/) project, and a [Groq](https://console.groq.com/) API key.

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

   Set these in `.env`:

   - `LIVEKIT_URL`
   - `LIVEKIT_API_KEY`
   - `LIVEKIT_API_SECRET`
   - `GROQ_API_KEY`

3. Run (one terminal):

   ```powershell
   .\.venv\Scripts\python.exe server.py
   ```

4. Open http://localhost:3000, click **Connect**, and allow microphone access.

The server serves the UI **and** runs the copilot agent in-process — no second terminal required.

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
| `agent.py` | Agent definition, full SuccessCOACHING system prompt, web search tool |
| `livekit_context.py` | Shared LiveKit knowledge loader (used by legacy sim code) |
| `customer_agent.py` | Unused on `main`; customer personas for the sim branch |
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

On that branch you may need both `server.py` and `agent.py dev` depending on the mode; see the UI on that branch for details.

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
