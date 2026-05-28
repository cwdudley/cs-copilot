"""
Shared LiveKit knowledge loader.

Reads livekit_docs.md from disk and exposes it as a module-level string so
both the CSM agent (agent.py) and the customer simulation agents
(customer_agent.py) can inject it into their system prompts.

Edit livekit_docs.md to update the knowledge — no Python changes needed.
"""

from pathlib import Path

_DOC_PATH = Path(__file__).parent / "livekit_docs.md"

# Full knowledge — kept on disk for human reference and editing.
# NOT injected into LLM prompts because at ~3,100 tokens it blows past
# Groq's free-tier 12k TPM limit on llama-3.3-70b-versatile after 1-2 turns.
LIVEKIT_KNOWLEDGE_FULL = _DOC_PATH.read_text(encoding="utf-8")


# Compact reference actually sent to the CSM. ~400 tokens. Names every key
# feature the CSM might cite, with one-line context — enough for the LLM
# to use them correctly in conversation.
LIVEKIT_COMPACT = """## LIVEKIT QUICK REFERENCE (CSM source of truth)

LiveKit = realtime infra for AI voice/video and SIP telephony.
Two surfaces: LiveKit Cloud (global edge SFU + observability) and
LiveKit Agents (Python/Node framework: AgentSession orchestrates
STT → LLM → TTS → VAD + turn handling).

Plugins: STT (Deepgram, Whisper, Groq), LLM (any), TTS (ElevenLabs,
Cartesia, Groq Orpheus), VAD (Silero), turn (MultilingualModel — semantic
end-of-utterance, worker mode only).

Knobs to cite by name:
- RoomOptions.participant_kinds — subscribe to STANDARD vs AGENT
- turn_handling.endpointing.min_delay / max_delay — silence windows
- LIVEKIT_REGION_OVERRIDE — pin agent compute near the edge
- @function_tool — Python decorator for LLM tool calls
- http_context.open() — required for plugins outside worker mode

Latency target: <1500ms end-of-user-speech → start-of-agent-audio.
Typical budget: edge 100-300ms, STT 150-300ms, LLM TTFT 300-800ms,
TTS first chunk 150-500ms. Levers: region pinning, streaming
(interim STT, token streaming, chunked TTS), model tiering.

SIP/Telephony: trunks via Twilio/Telnyx/Plivo/Vonage/BYO. DTMF via
RFC 2833 or SIP INFO (must match carrier). REFER-transfer to human
queue. Multi-trunk failover. Egress to S3/GCS (MP4 composite or OGG
track-level) for recording / audit trails.

Production ops:
- Session Analytics: per-session latency stages, jitter, packet loss,
  MOS, model usage
- Webhooks: room_started, participant_joined, track_published,
  room_finished
- Worker pools for agent scaling; pre-warm before peaks
- HIPAA-eligible Enterprise tier (BAA), SOC 2 Type II, DTLS-SRTP

Pricing: participant-minute + egress-minute + SIP-minute. Agents
framework is OSS; pay providers + Cloud minutes. Commit contracts at
Enterprise.

Common failure modes & one-line fixes:
- Agents in same room don't hear each other → participant_kinds=[STANDARD, AGENT]
- Latency spikes at peak → region-pin, check Session Analytics
- Awkward interruptions mid-sentence → raise min_delay, add MultilingualModel
- Conversation stalls after N turns → always set max_delay
- TTS errors outside worker → wrap with http_context.open()
- Cost growing faster than usage → model tiering (8B vs 70B), cap session length

Doc URLs: docs.livekit.io, docs.livekit.io/agents, docs.livekit.io/sip,
github.com/livekit/agents.
"""


CSM_KNOWLEDGE_HEADER = """
## YOUR LIVEKIT KNOWLEDGE

You are a LiveKit Customer Success Manager. Use the compact reference
below as ground truth. When giving advice:
- Cite specific features by name (Session Analytics, participant_kinds,
  REFER-transfer, MultilingualModel, LIVEKIT_REGION_OVERRIDE, etc.).
- Recommend concrete next steps anchored in real product capabilities.
- If something is outside LiveKit's scope, say so and redirect.
- Don't invent features that aren't in the reference.

"""


# Framing block for the customer side. Customer plays user-level competent
# but technically shallow — they know they're on LiveKit, they know the
# rough capabilities, but they don't know the specifics and they push the
# CSM to be concrete.
CUSTOMER_KNOWLEDGE_HEADER = """
## BACKGROUND: LIVEKIT (You use it, your engineers know it, you don't)

You are a customer of LiveKit. The reference below is LiveKit's full
product knowledge — but YOU don't have this depth. Your engineering team
set things up. You know the high-level vocabulary (latency, SIP, regions,
observability) but not the specifics.

How to use this reference:
- Stay in character. Speak like an operator, founder, or product leader —
  not like someone reciting docs.
- You can hint at concepts you've heard from your team ("our engineers
  mentioned region pinning", "we have some SIP redundancy thing").
- DO NOT lecture the CSM about LiveKit features. They are the expert.
- If the CSM gives vague advice, push them for specifics: which feature,
  which setting, which doc page, which metric.
- If the CSM cites a specific LiveKit feature and it sounds relevant,
  show interest and ask follow-up questions.

──────────────────────────────────────────────────────────────────────────
"""


def csm_context() -> str:
    """Compact LiveKit reference for the CSM system prompt (~500 tokens)."""
    return CSM_KNOWLEDGE_HEADER + LIVEKIT_COMPACT


def customer_context() -> str:
    """
    Framing block only — intentionally NOT the full knowledge dump.

    The customer agents run on a smaller LLM with a tight free-tier rate
    limit (Groq Llama 3.1 8B Instant: ~6k tokens/minute). Injecting the
    full LiveKit doc adds ~3k tokens to every turn and exhausts the budget
    in 2-3 calls.

    The customer doesn't need to cite features anyway — they just need to
    know they're a LiveKit user and play less-technical than the CSM. The
    framing header alone gives the LLM enough to do that in character.
    """
    return CUSTOMER_KNOWLEDGE_HEADER
