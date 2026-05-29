import logging
from pathlib import Path
from dotenv import load_dotenv
from livekit import agents, rtc
from livekit.agents import Agent, AgentSession, RoomInputOptions, function_tool
from livekit.plugins import groq, silero
from livekit.plugins.turn_detector.multilingual import MultilingualModel

load_dotenv()

logger = logging.getLogger("voice-agent")


PROMPT_PATH = Path(__file__).parent / "prompts" / "successcoaching.md"
SYSTEM_PROMPT = PROMPT_PATH.read_text(encoding="utf-8").strip()


@function_tool
async def search_web(query: str) -> str:
    """Search the web for information about a company, person, news, or any topic relevant to a customer success conversation."""
    from duckduckgo_search import DDGS
    results = DDGS().text(query, max_results=5)
    if not results:
        return "No results found for that query."
    return "\n\n".join(f"{r['title']}: {r['body']}" for r in results[:4])


class Assistant(Agent):
    def __init__(self) -> None:
        super().__init__(instructions=SYSTEM_PROMPT, tools=[search_web])

    async def tts_node(self, text, model_settings):
        first_frame = True
        async for frame in Agent.default.tts_node(self, text, model_settings):
            if first_frame:
                first_frame = False
                yield rtc.AudioFrame.create(
                    frame.sample_rate,
                    frame.num_channels,
                    int(frame.sample_rate * 0.25),
                )
            yield frame

    async def on_user_turn_completed(self, turn_ctx, new_message) -> None:
        # Sliding window: keep only the last N messages each turn. The system
        # prompt is preserved automatically. This keeps per-call token usage
        # flat in long conversations so we don't hit Groq's per-minute cap.
        turn_ctx.truncate(max_items=12)


async def entrypoint(ctx: agents.JobContext):
    logger.info("Agent connected to room: %s", ctx.room.name)
    await ctx.connect()

    session = AgentSession(
        stt=groq.STT(model="whisper-large-v3-turbo"),
        llm=groq.LLM(model="llama-3.3-70b-versatile"),
        tts=groq.TTS(model="canopylabs/orpheus-v1-english", voice="diana"),
        vad=silero.VAD.load(),
        turn_handling={
            "turn_detection": MultilingualModel(),
            "endpointing": {"min_delay": 0.8, "max_delay": 8.0},
        },
    )

    await session.start(
        room=ctx.room,
        agent=Assistant(),
        room_input_options=RoomInputOptions(),
    )

    await session.say("Hey, what can I help you with?")


if __name__ == "__main__":
    agents.cli.run_app(agents.WorkerOptions(entrypoint_fnc=entrypoint))
