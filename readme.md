# 🛰️ NATS Chatbot with Streamlit and GPT-4o

This project demonstrates a simple pub/sub chatbot system using the [NATS messaging system](https://nats.io), [Docker](https://www.docker.com/), [Nats Docker](https://hub.docker.com/_/nats), [Streamlit](https://streamlit.io/), and [OpenAI GPT-4o-mini](https://platform.openai.com/docs/models/gpt-4o). 

---

## 🚀 Getting Started

### 1️⃣ Pull the NATS server image from Docker Hub

```bash
docker pull nats
```
### 2️⃣ Run the NATS server in the background
```bash
docker run -d --name nats-server -p 4222:4222 nats
```
You can start it again later using:
```bash
docker start nats-server
```
To see if it’s running:
```bash
docker ps
```
To stop the NATS container:
```bash
docker stop nats-server
```
💻 Set up your Python environment
📦 Install dependencies
First, make sure you have Python 3.9+ and pip installed. Then run:
```bash
pip install -r requirements.txt
```

Make sure to also set your OpenAI API key in a .env file:
```bash
OPENAI_API_KEY=your_openai_key_here
```

🧠 Run the Streamlit chatbot interface
```bash
streamlit run app.py
```

The chatbot sends messages via NATS to the updates subject.

Responses are generated using GPT-4o-mini with full history tracking.

🔁 Optional: Run the pub/sub model manually
If you want to test the classic pub/sub terminal model, you can also run:

✅ 1. Start the subscriber (LangChain-based)
```bash
python subscriber.py
```
✅ 2. Run the publisher (type messages)
```bash
python publisher.py
```
This setup publishes messages from terminal input and receives responses through GPT.

📂 File Overview
app.py – Main Streamlit-based chatbot UI.

subscriber.py – NATS subscriber with GPT-4o LangChain integration.

publisher.py – NATS publisher with terminal input.

.env – Contains your OpenAI API key.

requirements.txt – Python dependencies list.

🧠 Need Help?
If you're having trouble getting started, try the subscriber.py and publisher.py approach first to make sure your NATS server is working.

🛑 Cleanup (optional)
To remove the NATS Docker container:
```bash
docker rm -f nats-server
```
