import asyncio
from nats.aio.client import Client as NATS   # type: ignore

async def run():
    nc = NATS()
    await nc.connect("localhost:4222")

    print("🔵 Type messages to send to the 'updates' subject. Type 'exit' to quit.")

    while True:
        msg = input("You: ")
        if msg.lower() in ("exit", "quit"):
            break
        await nc.publish("updates", msg.encode())
        print(f"[Publisher] Sent: {msg}")

    await nc.drain()

if __name__ == "__main__":
    asyncio.run(run())
