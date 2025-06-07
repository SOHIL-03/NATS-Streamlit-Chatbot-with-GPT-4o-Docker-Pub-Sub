import asyncio
from nats.aio.client import Client as NATS   # type: ignore
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory

load_dotenv()

llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0.7)

memory = ConversationBufferMemory()

conversation = ConversationChain(
    llm=llm,
    memory=memory,
    verbose=True
)


async def message_handler(msg):
    subject = msg.subject
    data = msg.data.decode()
    response = conversation.predict(input=data)
    print(f"[Subscriber] Response: {response}")

async def run():
    nc = NATS()
    await nc.connect("localhost:4222")

    await nc.subscribe("updates", cb=message_handler)

    print("[Subscriber] Listening on 'updates' subject...")
    while True:
        await asyncio.sleep(1)

if __name__ == "__main__":
    asyncio.run(run())
