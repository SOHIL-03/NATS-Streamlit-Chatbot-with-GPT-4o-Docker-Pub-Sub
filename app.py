import streamlit as st
import asyncio
from nats.aio.client import Client as NATS    # type: ignore
from dotenv import load_dotenv
import os
import openai

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
client = openai.Client()

st.title("💬 NATS Chatbot with History (GPT-4o-mini)")

if "history" not in st.session_state:
    st.session_state.history = [{"role": "system", "content": "You are a helpful assistant."}]

if "messages" not in st.session_state:
    st.session_state.messages = []

user_input = st.text_input("You:", placeholder="Type your message and press Enter")

async def send_to_nats_and_get_response(message):
    # Publish to NATS
    nc = NATS()
    await nc.connect("localhost:4222")
    await nc.publish("updates", message.encode())
    await nc.drain()

    # Add user message to history
    st.session_state.history.append({"role": "user", "content": message})

    # Get response from GPT-4o-mini
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=st.session_state.history,
    )

    # Extract assistant's reply
    reply = response.choices[0].message.content.strip()

    # Append assistant message to history
    st.session_state.history.append({"role": "assistant", "content": reply})

    return reply

# On user input
if user_input:
    st.session_state.messages.append(("user", user_input))

    # Send and get assistant reply
    assistant_reply = asyncio.run(send_to_nats_and_get_response(user_input))

    st.session_state.messages.append(("assistant", assistant_reply))

# Display messages
for sender, msg in st.session_state.messages:
    st.chat_message(sender).write(msg)
