# LiveKit Platform Reference

This is the shared LiveKit knowledge base used by both the CS copilot and the
customer simulation agents. It is loaded at runtime by `livekit_context.py`.

The CSM agent uses this as its source of truth for product-level
recommendations. The customer agents use it as background — they know their
team built on LiveKit, but they don't know the specifics and will push the
CSM for concrete answers.

---

## 1. What LiveKit Is

LiveKit is a real-time communications platform built on WebRTC, with
first-class support for AI agents, voice and video applications, and
telephony integration. Two main components:

- **LiveKit Server** — open-source Selective Forwarding Unit (SFU) that
  routes WebRTC media. Available self-hosted or as LiveKit Cloud.
- **LiveKit Agents** — Python and Node.js framework for building AI voice
  and video agents that participate as real-time participants in rooms.

---

## 2. LiveKit Cloud

- Global edge network across US, EU, and Asia regions. Automatic region
  selection based on the participant's geo.
- Multi-region session distribution. Agent workloads can be pinned to a
  region (`LIVEKIT_REGION_OVERRIDE`) to minimize round trips.
- Built-in observability: per-session latency breakdowns, packet loss,
  jitter, model usage, and audio quality scores.
- Production tiers with SLA, dedicated capacity, enterprise SSO, and BAA
  (Business Associate Agreement) for HIPAA-eligible workloads.

---

## 3. Core Room & Participant Model

- **Room**: a session container. Participants and tracks live inside a room.
- **Participant**: a connected client. Has an identity, name, metadata, and
  arbitrary key-value attributes.
- **Track**: a single media stream (audio, video, or data) published by a
  participant.
- **ParticipantKind**:
  - `STANDARD` — humans on a LiveKit SDK
  - `AGENT` — an AI agent (separate kind so apps can route differently)
  - `SIP` — telephony participant (inbound or outbound call)
  - `EGRESS` — recording or stream egress worker
  - `INGRESS` — broadcast-to-room (e.g., RTMP/WHIP) worker

Subscription defaults to STANDARD-only. To let an agent hear other agents,
set `participant_kinds=[STANDARD, AGENT]` on `RoomOptions`.

---

## 4. LiveKit Agents Framework (Python)

### Core classes
- `AgentSession` — orchestrator. Wires STT, LLM, TTS, VAD, and turn
  detection into a single voice loop.
- `Agent` — the brain. Holds the system prompt (`instructions`) and tools
  decorated with `@function_tool`.
- `JobContext` — runtime context provided by the worker for hosted jobs;
  exposes a shared aiohttp session, inference executor, and the room.

### Worker vs direct-room mode
- **Worker mode**: `agents.cli.run_app(WorkerOptions(entrypoint_fnc=...))`.
  The agents runtime manages job lifecycle, the HTTP session pool, and the
  inference executor. Use this for production deployments.
- **Direct mode**: connect an `rtc.Room()` yourself and start the session
  outside a JobContext. Requires wrapping plugin usage in
  `async with livekit.agents.utils.http_context.open():`. Useful for
  test scripts and embedded servers.

### Provider plugins
- **STT**: Deepgram, AssemblyAI, OpenAI Whisper, Groq Whisper, Azure Speech,
  Google Speech.
- **LLM**: OpenAI, Anthropic, Google Gemini, Groq (Llama, Mixtral), Cerebras,
  Together, plus custom adapters.
- **TTS**: ElevenLabs, OpenAI, Cartesia, PlayAI, Rime, Azure, Google,
  Groq (Canopy Orpheus).
- **VAD**: Silero (local, CPU). Each `silero.VAD.load()` returns a
  per-stream instance.
- **Turn detection**: `MultilingualModel` from
  `livekit-plugins-turn-detector`. Semantic end-of-utterance prediction —
  but requires a JobContext's inference executor, so worker mode only.

### Turn handling
```python
turn_handling={
    "turn_detection": MultilingualModel(),     # optional, worker-only
    "endpointing": {
        "min_delay": 0.5,    # silence required before ending the user's turn
        "max_delay": 5.0,    # force end-of-turn after this much partial silence
    },
}
```
Without `max_delay`, a session can hang indefinitely if the VAD never
declares clean silence — especially in two-agent simulations where the
VAD is starved by simultaneous TTS playback.

---

## 5. Voice Pipeline Latency Budgets

Tier-1 production target: under **1500 ms** from end-of-user-speech to
start-of-agent-audio.

Typical contributions:
- LiveKit edge transport: 100–300 ms (region-dependent)
- STT first transcript: 150–300 ms (streaming STT)
- LLM time-to-first-token: 300–800 ms (Groq much lower; frontier 70B+ higher)
- TTS first audio chunk: 150–500 ms

### Optimization levers
- **Region pinning** for agent compute near the LiveKit edge.
- **Streaming everywhere**: STT interim results, LLM token streaming, TTS
  chunked output. Never wait for full completion at any stage.
- **Adaptive streaming** on the LiveKit transport adjusts bitrate to
  network conditions automatically.
- **Dynacast** only forwards simulcast layers actually being consumed.
- **VAD-based barge-in** for natural interruptions when the user starts
  speaking over the agent.
- **Model tiering**: use small models (Llama 8B, Haiku) for short turns and
  classification; reserve large models (70B, Sonnet) for reasoning-heavy
  turns.

---

## 6. SIP / Telephony

LiveKit supports inbound and outbound phone calls via SIP trunking.

- **SIP trunk providers**: Twilio, Telnyx, Plivo, Vonage, or any
  SIP-compatible carrier.
- **Inbound**: map phone numbers to LiveKit rooms; an agent joins the
  room automatically when a call arrives.
- **Outbound**: trigger a call from the LiveKit API; the agent dials out
  and joins the room as the call connects.
- **DTMF**: send/receive touch-tone events using either RFC 2833 or SIP
  INFO mode (must match the carrier's mode).
- **Recording**: egress to S3/GCS in MP4 (composite) or OGG (track-level).
- **Transfer**: REFER-based transfer to a human queue or another number.
  Maintain context across handoff via room metadata or external store.
- **Redundancy**: configure backup trunks; LiveKit will fail over if the
  primary trunk is unreachable.

For production AI voice contact centers, the most common architecture is:
inbound number → SIP trunk → LiveKit room → AI agent → optional REFER
transfer to a human queue if the agent escalates.

---

## 7. Production Operations

### Observability
- **Session Analytics**: per-session breakdown of latency stages, audio
  quality (jitter, packet loss, MOS), and model usage.
- **Agent telemetry**: STT confidence, LLM token counts, TTS character
  counts, turn-by-turn timings.
- **Webhooks**: `room_started`, `participant_joined`, `track_published`,
  `room_finished`, etc. Use to land session events in your data warehouse.

### Scaling
- LiveKit Cloud autoscales SFU capacity. No customer-side action needed
  for typical workloads.
- For agent workers: deploy as a pool. Each worker handles N concurrent
  jobs (configurable). Capacity = workers × jobs-per-worker.
- For consumer/concurrency-heavy products: pre-warm worker pools ahead of
  predictable peaks (e.g., evening for companion apps, school hours for
  tutoring).

### Recording & Egress
- **Room composite** recording: full meeting MP4.
- **Track-level egress**: individual participant audio/video to S3/GCS.
- **Stream egress**: RTMP push for live broadcast.
- Egress is configurable per-room with templates; can start automatically
  on room creation.

### Security & Compliance
- All media encrypted in transit (DTLS-SRTP).
- End-to-end encryption available via media plugin.
- HIPAA-eligible on the Enterprise tier (BAA available).
- SOC 2 Type II compliant.
- Access via signed JWTs with grant-level permissions
  (`room_join`, `can_publish`, `can_subscribe`, `room_admin`, etc.).

---

## 8. Common Agent Patterns

### Function calling
Decorate Python functions with `@function_tool`. The LLM can call them
during conversation. Use for lookups, mutations, escalation triggers, and
external system calls (CRM, EHR, billing).

### Voice + screen-share (multimodal)
The agent subscribes to a participant's screen-share track, samples frames
into a multimodal model (GPT-4o vision, Gemini), and grounds answers in
what it sees. Common for in-app copilots.

### Handoff / escalation
- **Agent → human in same room**: invite a human via the API; both share
  context naturally.
- **SIP REFER**: transfer the call leg to a human queue or another number.
- **Agent → agent**: hand off to a specialist agent. Persist conversation
  state in room metadata or an external store.

### Multi-agent in one room
Multiple agents can coexist (e.g., primary CSM + a specialist). Each is
its own `AgentSession`. To make them hear each other, set
`participant_kinds=[STANDARD, AGENT]` on `RoomOptions`.

### RAG over knowledge bases
Function tools call into a vector store (Pinecone, Weaviate, pgvector).
Stream the retrieved chunks into the LLM context before generating the
turn. For latency, retrieve in parallel with the start of the turn.

---

## 9. Common Failure Modes & Fixes

| Symptom | Likely cause | Fix |
|---|---|---|
| Agents in the same room don't hear each other | Default subscription is STANDARD-only | `room_options=RoomOptions(participant_kinds=[STANDARD, AGENT])` |
| Latency spikes during peak hours | Agent compute far from LiveKit edge | Region-pin agents; check the Session Analytics latency breakdown |
| Awkward agent interruptions mid-sentence | Endpointing too aggressive | Raise `min_delay`; add `MultilingualModel` semantic turn detection |
| Conversation stalls after N turns | No `max_delay` set; VAD missing silence | Always set `max_delay`; check Silero CPU load |
| SIP DTMF lost | RFC 2833 vs SIP INFO mode mismatch | Match the trunk's DTMF mode in the SIP config |
| TTS plugin errors outside worker mode | No HTTP session in scope | `async with livekit.agents.utils.http_context.open():` |
| Cost growing faster than usage | All sessions on premium models | Tier models by use case; cap session duration; use smaller models for classification |
| Adoption flat after launch | No structured rollout instrumentation | Wire Session Analytics + custom feature-usage events; cohort by use case |

---

## 10. Pricing Model (Cloud)

- **Connection minutes**: per participant-minute in a room.
- **Egress minutes**: per minute of recording/streaming.
- **Bandwidth**: included up to a tier-specific cap.
- **SIP**: per SIP-minute, separate from connection minutes.
- The Agents framework itself is open source — you pay for the underlying
  STT/LLM/TTS providers plus LiveKit Cloud minutes.
- Volume discounts and commit-based contracts available at Enterprise tier.

When customers ask about cost, the levers that actually move the needle:
1. Average session duration (cap idle/runaway sessions)
2. Model tier (Llama 8B vs 70B vs frontier)
3. TTS provider (open Orpheus vs ElevenLabs Pro)
4. Concurrent peak load (right-size, don't pay for unused capacity)
5. Region selection (don't egress across regions unnecessarily)

---

## 11. Key Documentation URLs

- `docs.livekit.io` — main documentation
- `docs.livekit.io/agents` — Agents framework
- `docs.livekit.io/sip` — telephony
- `docs.livekit.io/home/cloud` — LiveKit Cloud
- `docs.livekit.io/home/recording` — egress and recording
- `docs.livekit.io/home/security` — security and compliance
- `github.com/livekit/agents` — Agents Python framework source
- `github.com/livekit/livekit` — LiveKit server source
- `github.com/livekit/agents-js` — Agents Node.js framework
