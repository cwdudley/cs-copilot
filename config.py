import os
from dataclasses import dataclass

from dotenv import load_dotenv


@dataclass(frozen=True)
class Settings:
    livekit_url: str
    livekit_api_key: str
    livekit_api_secret: str
    groq_api_key: str
    room_name: str = "cs-copilot"
    port: int = 3000


def get_settings() -> Settings:
    load_dotenv()

    required = {
        "LIVEKIT_URL": os.getenv("LIVEKIT_URL"),
        "LIVEKIT_API_KEY": os.getenv("LIVEKIT_API_KEY"),
        "LIVEKIT_API_SECRET": os.getenv("LIVEKIT_API_SECRET"),
        "GROQ_API_KEY": os.getenv("GROQ_API_KEY"),
    }
    missing = [name for name, value in required.items() if not value]
    if missing:
        raise RuntimeError(
            "Missing required environment variables: "
            + ", ".join(missing)
            + ". Copy .env.example to .env and add your own keys."
        )

    return Settings(
        livekit_url=required["LIVEKIT_URL"],
        livekit_api_key=required["LIVEKIT_API_KEY"],
        livekit_api_secret=required["LIVEKIT_API_SECRET"],
        groq_api_key=required["GROQ_API_KEY"],
        room_name=os.getenv("ROOM_NAME", "cs-copilot"),
        port=int(os.getenv("PORT", "3000")),
    )
