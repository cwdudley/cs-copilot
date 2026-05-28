# CS Copilot

Voice Customer Success copilot demo built on [LiveKit Agents](https://docs.livekit.io/agents/), Groq (STT/LLM/TTS), and a browser UI.

## Features

- **Live mode** — Talk to the CS copilot in your browser (microphone).
- **Simulation mode** — Watch AI-vs-AI practice calls with four customer scenarios.

## Setup

1. Clone the repo and create a virtual environment:

   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   pip install -r requirements.txt
   ```

2. Copy environment template and add your keys:

   ```powershell
   copy .env.example .env
   ```

   Required: `LIVEKIT_URL`, `LIVEKIT_API_KEY`, `LIVEKIT_API_SECRET`, `GROQ_API_KEY`.

3. Run the web server:

   ```powershell
   .\.venv\Scripts\python.exe server.py
   ```

   Open http://localhost:3000

4. For **Connect** (live voice), run the agent worker in a second terminal:

   ```powershell
   .\.venv\Scripts\python.exe agent.py dev
   ```

   Simulations work with only `server.py` running.

## Project layout

| File | Purpose |
|------|---------|
| `index.html` | Browser UI |
| `server.py` | Web server + simulation orchestrator |
| `agent.py` | CS copilot LiveKit agent |
| `customer_agent.py` | Simulated customer personas |
| `livekit_context.py` | LiveKit knowledge for prompts |
