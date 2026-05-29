from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from config import get_settings
from agent import SYSTEM_PROMPT


def main() -> None:
    settings = get_settings()
    if not settings.livekit_url.startswith("wss://"):
        raise RuntimeError("LIVEKIT_URL must start with wss://")
    if len(SYSTEM_PROMPT) < 1000:
        raise RuntimeError("SuccessCOACHING prompt did not load correctly")

    index_path = ROOT / "index.html"
    if not index_path.exists():
        raise RuntimeError("index.html is missing")

    print("Smoke check passed: config, prompt, and UI assets are present.")


if __name__ == "__main__":
    main()
