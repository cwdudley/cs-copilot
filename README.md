# Account Management Coach

A voice coach for CS and account management leaders, built on ElevenLabs Agents.
Grounded in the SuccessCOACHING methodology, plus SPICED for diagnosis and
MEDDPICC for qualification.

> This branch (`elevenlabs-am-coach`) is a rebuild of the LiveKit version on
> `main`. See **Why this exists** below for the architectural argument.

---

## Running it

```bash
pip install -r requirements.txt
```

Add to `.env`:

```
ELEVENLABS_API_KEY=your_key_here
```

Provision the agent — uploads the knowledge base and creates the agent, then
writes `ELEVENLABS_AGENT_ID` back to `.env`:

```bash
python provision.py
```

Start the server and open <http://localhost:3000>:

```bash
python server.py
```

Optional `.env` overrides: `ELEVENLABS_VOICE_ID`, `ELEVENLABS_TTS_MODEL`
(default `eleven_flash_v2_5`), `ELEVENLABS_LLM` (default `claude-sonnet-4-5`).

---

## Why this exists

The LiveKit build hit Groq's free-tier rate limit — 12,000 tokens per minute on
`llama-3.3-70b-versatile`. The full SuccessCOACHING playbook was ~3,000 tokens
and sat in the system prompt, so every single turn re-sent the entire
methodology. Conversations died after two exchanges.

The fix at the time was to compact the playbook down to a ~700-token persona
stub. TARO, the eight lifecycle stages, health bands, churn tiers, the seven
guardrails — cut, so the conversation could survive.

**That deleted the product.** The methodology *is* the coaching.

The real problem was that the prompt fused two different kinds of content:

| Kind | Example | Belongs in |
|---|---|---|
| Behavioral rules | "Never say an account will churn" | The prompt — must apply every turn |
| Reference material | The MEDDPICC element definitions | Retrieval — needed only when relevant |

Reference material has no business being re-sent on every turn. Asking about
renewal risk shouldn't also pay to restate the onboarding milestone gates.

So this build splits along that seam:

- **`coach/instructions.md`** — persona, response style, the seven guardrails,
  attribution rules, and a one-line index of each framework so the agent knows
  what exists and when to reach for it. Small, flat, sent every turn.
- **`coach/kb/*.md`** — the full framework corpus, uploaded as knowledge base
  documents and retrieved semantically when a question calls for them.

Adding SPICED and MEDDPICC grew the methodology by roughly 2.5x. **The per-turn
prompt cost did not change**, because the new material went into retrieval. That
is the whole point — under the old architecture, expanding the methodology would
have made the rate limit problem worse.

### What got deleted

Everything below was pipeline plumbing on the LiveKit build. None of it made the
coaching better:

- `http_context.open()` to run plugins outside a worker job context
- `RoomInputOptions(close_on_disconnect=False)` so the session survived an empty room
- A missing `model_q8.onnx` turn-detector download
- Brute-force probing the TTS API to discover valid voice names
- Content-based transcript deduplication across two publishers
- Migrating off a deprecated transcription event API
- Prompt compaction and a `truncate(max_items=N)` sliding window

STT, LLM orchestration, TTS, and turn-taking are now managed. `server.py` mints
signed URLs and serves one static file.

### Turn-taking is a product feature here

Not a generic latency point. A CS leader reasoning about a live account pauses
mid-thought constantly — *"we've got a renewal in… maybe 90 days, and the
champion just left, so—"*. VAD timing forces a bad trade: interrupt them, or add
dead air to every turn.

The LiveKit build diagnosed this correctly and reached for the `MultilingualModel`
semantic turn detector — which then only ran in worker mode, and whose model file
wasn't downloaded. Right diagnosis, unreliable delivery. Managed semantic
turn-taking is the difference between a coach and an interrogator.

### The honest tradeoffs

- **Less pipeline control.** No independent STT swap, no direct VAD tuning.
- **Pricing shifts** from component costs to per-minute conversational.
- **LLM routing** is theirs unless you wire a custom endpoint.
- **Multi-agent simulation doesn't fit.** The `main` branch runs two agents
  talking to each other in a shared LiveKit room, which needs agents as
  first-class room peers (`participant_kinds=[STANDARD, AGENT]`). That is
  LiveKit's design center, not this platform's. Rebuilding it here would mean
  hand-rolling the room abstraction against the grain of a managed service.

One-to-one coaching belongs here. Multi-agent realtime belongs on LiveKit. The
split is real, which is why both branches still exist.

---

## Layout

```
coach/
  instructions.md          persona, guardrails, framework index  (prompt)
  kb/
    01-taro.md             execution framework
    02-lifecycle-and-value.md
    03-health-and-churn.md
    04-renewals.md
    05-expansion.md
    06-onboarding.md
    07-cs-operations.md
    08-revenue-operations.md
    09-spiced.md           diagnosis framework
    10-meddpicc.md         qualification framework
    11-framework-selection.md   which to reach for, and when
provision.py               uploads KB, creates the agent
server.py                  signed-URL endpoint + static files
index.html                 voice UI
```

### The three frameworks

| Framework | Job | Answers |
|---|---|---|
| SPICED | Diagnosis | What is true about this account? |
| MEDDPICC | Qualification | Is this revenue event real and winnable? |
| TARO | Execution | What play do I run? |

Diagnose, then qualify, then act. `11-framework-selection.md` covers routing and
how gaps in one feed the next.
