"""
Probe Groq's canopylabs/orpheus-v1-english endpoint to find which voices
your account can actually use.

Usage:
    .venv\\Scripts\\python.exe probe_voices.py

Outputs a Python list at the end that you can paste into CUSTOMER_VOICES
in customer_agent.py.
"""

import asyncio
import os
import sys

import aiohttp
from dotenv import load_dotenv

load_dotenv()

# Add any other voice names you see in the Groq playground to this list.
CANDIDATES = ["autumn", "diana", "hannah", "austin", "daniel", "troy"]

GROQ_TTS_URL = "https://api.groq.com/openai/v1/audio/speech"
MODEL = "canopylabs/orpheus-v1-english"


async def probe(session: aiohttp.ClientSession, voice: str):
    headers = {"Authorization": f"Bearer {os.getenv('GROQ_API_KEY')}"}
    payload = {
        "model": MODEL,
        "input": "hi",
        "voice": voice,
        "response_format": "wav",
    }
    try:
        async with session.post(GROQ_TTS_URL, json=payload, headers=headers) as r:
            if r.status == 200:
                return voice, 200, "ok"
            text = await r.text()
            return voice, r.status, text[:120]
    except Exception as e:
        return voice, -1, str(e)[:120]


async def main():
    if not os.getenv("GROQ_API_KEY"):
        print("ERROR: GROQ_API_KEY missing from .env")
        sys.exit(1)

    print(f"Probing {len(CANDIDATES)} candidate voices against {MODEL}...\n")

    async with aiohttp.ClientSession() as session:
        results = await asyncio.gather(*[probe(session, v) for v in CANDIDATES])

    working = []
    for voice, status, msg in results:
        if status == 200:
            working.append(voice)
            print(f"  OK   {voice}")
        else:
            print(f"  FAIL {voice}  (status {status}: {msg})")

    print()
    print("=" * 60)
    print(f"{len(working)} working voices found.")
    print()
    print("Paste this into customer_agent.py:")
    print()
    print(f"CUSTOMER_VOICES = {working!r}")


if __name__ == "__main__":
    asyncio.run(main())
