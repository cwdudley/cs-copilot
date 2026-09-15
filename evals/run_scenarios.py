"""
Run coaching scenarios against the live ElevenLabs agent as text turns.

Each scenario opens a fresh session (same signed-URL path the web app uses),
sends the user turns in order, and records the agent's replies. Transcripts are
written to a JSON file for grading against evals/coaching-rubric.md.

Usage: python evals/run_scenarios.py <label>
"""

import asyncio
import json
import os
import sys
import time
from pathlib import Path

import aiohttp
from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "evals" / "runs"
load_dotenv(ROOT / ".env")

API = "https://api.elevenlabs.io/v1"
KEY = os.environ["ELEVENLABS_API_KEY"]
AGENT = os.environ["ELEVENLABS_AGENT_ID"]

SCENARIOS = [
    # Existing rubric scenarios (evals/coaching-rubric.md, 1-8; 9 is graded across all).
    {"id": "S1-usage-growth", "turns": [
        "Acme's usage is up 40% this quarter. Should I pitch the enterprise tier?"]},
    {"id": "S2-enthusiastic-contact", "turns": [
        "Sarah loves us and wants to roll us out to her whole department."]},
    {"id": "S3-seats-value-problem", "turns": [
        "They want 50 more seats, but only 60% of their current seats are active."]},
    {"id": "S4-whitespace", "turns": [
        "They have three other business units we don't sell to."]},
    {"id": "S5-sufficient-context", "turns": [
        "Their VP of Ops owns a documented initiative to cut ticket handling time 25% by March, "
        "the budget is approved, and she's asked us for a proposal for two more teams. "
        "Our current teams hit their targets last quarter."]},
    {"id": "S6-positive-goal", "turns": [
        "They're launching in EMEA next year and need to meet local compliance requirements."]},
    {"id": "S7-multi-turn-adaptation", "turns": [
        "Usage is way up at Northwind.",
        "They reorganized and moved support onto our platform, but nobody's sure who owns it now."]},
    {"id": "S8-quick-factual", "turns": [
        "What's the difference between a Critical Event and a Compelling Event?"]},
    # New scenarios for this patch.
    {"id": "N1-early-opportunity", "turns": [
        "Our Security team at Globex is live and happy. The Platform team lead told me they have "
        "the same problem and they're interested. Do I have an opportunity?"]},
    {"id": "N2-vp-role-assumption", "turns": [
        "Globex is a $900K renewal in four months. I've only ever worked with the Director of IT. "
        "There's a VP of Infrastructure I've never met."]},
    {"id": "N3-parallel-workstreams", "turns": [
        "We have no executive coverage on the existing Globex account, but their Analytics business "
        "unit just asked us for a demo. Should I fix exec coverage before I chase Analytics?"]},
    {"id": "N4-motivation-inference", "turns": [
        "For expansion at Globex, should I prioritize Platform or Security? Platform uses the same "
        "workflow as the team where we already proved value. Security has a different use case but "
        "has budget this quarter.",
        "I keep coming back to Security though. They have budget."]},
]


async def run_one(session: aiohttp.ClientSession, scenario: dict) -> dict:
    async with session.get(f"{API}/convai/conversation/get-signed-url",
                           params={"agent_id": AGENT}, headers={"xi-api-key": KEY}) as r:
        signed = (await r.json())["signed_url"]

    exchange, audio_chunks = [], 0
    async with session.ws_connect(signed, timeout=30) as ws:
        # text_only: same agent, prompt and knowledge base, but no TTS spend.
        await ws.send_json({
            "type": "conversation_initiation_client_data",
            "conversation_config_override": {"conversation": {"text_only": True}},
        })

        async def next_agent_response(timeout: float) -> str | None:
            nonlocal audio_chunks
            deadline = time.monotonic() + timeout
            while time.monotonic() < deadline:
                try:
                    msg = await asyncio.wait_for(ws.receive(), timeout=deadline - time.monotonic())
                except asyncio.TimeoutError:
                    return None
                if msg.type != aiohttp.WSMsgType.TEXT:
                    return None
                data = json.loads(msg.data)
                kind = data.get("type")
                if kind == "ping":
                    await ws.send_json({"type": "pong", "event_id": data["ping_event"]["event_id"]})
                elif kind == "audio":
                    audio_chunks += 1
                elif kind == "agent_response":
                    return data["agent_response_event"]["agent_response"]
            return None

        greeting = await next_agent_response(30)
        for turn in scenario["turns"]:
            await ws.send_json({"type": "user_message", "text": turn})
            reply = await next_agent_response(90)
            # Collect any immediate follow-on response in the same agent turn.
            extra = await next_agent_response(4)
            if extra:
                reply = f"{reply} {extra}" if reply else extra
            exchange.append({"user": turn, "agent": reply})

    return {"id": scenario["id"], "greeting": greeting, "exchange": exchange, "audio_chunks": audio_chunks}


async def main(label: str) -> None:
    results = []
    async with aiohttp.ClientSession() as session:
        for scenario in SCENARIOS:
            try:
                result = await run_one(session, scenario)
            except Exception as e:  # keep going; record the failure
                result = {"id": scenario["id"], "error": f"{type(e).__name__}: {e}"}
            results.append(result)
            print(f"\n=== {result['id']} ===")
            if "error" in result:
                print("ERROR:", result["error"])
                continue
            for turn in result["exchange"]:
                print(f"USER:  {turn['user']}")
                print(f"AGENT: {turn['agent']}")
    out = OUT_DIR / f"scenarios_{label}.json"
    out.write_text(json.dumps(results, indent=2), encoding="utf-8")
    print(f"\nSaved {out}")


if __name__ == "__main__":
    asyncio.run(main(sys.argv[1] if len(sys.argv) > 1 else "run"))
