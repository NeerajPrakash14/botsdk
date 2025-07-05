# 🚀 WhatsApp MCP Bot - FastAPI + Groq + Twilio

This project is a smart WhatsApp chatbot using FastAPI, Groq LLaMA3 models, and Twilio. It runs as a cloud-native MCP (Message Control Processor) service on Google Cloud Run.

---

## 🧠 Features

- LLaMA3-powered AI assistant (via Groq API)
- WhatsApp integration via Twilio Sandbox
- Per-user memory with command handling
- Stateless deployment via Docker + GCP Cloud Run

---

## 📦 Project Structure

```bash
📁 your-project/
├── main.py             # FastAPI app (MCP logic)
├── requirements.txt    # Dependencies
├── Dockerfile          # Container setup
├── .env                # Your API keys (not committed)
├── .env.example        # Template for env vars
```


## 🛠️ Setup Instructions

### 1. Clone the Project

```bash
git clone https://github.com/your-user/whatsapp-mcp-bot.git
cd whatsapp-mcp-bot
```

### 2. Install Python Requirements (for local dev)

```bash
pip install -r requirements.txt
```

### 3. Add .env File

Create a .env file with:

```bash
GROQ_API_KEY=your_groq_api_key
GROQ_API_URL=https://api.groq.com/openai/v1
```


## 🚀 Deploy to Google Cloud Run

### 1. Enable Required Services

```bash
gcloud config set project YOUR_PROJECT_ID
gcloud services enable run.googleapis.com cloudbuild.googleapis.com artifactregistry.googleapis.com
```

### 2. Deploy with Cloud Build

```bash
gcloud run deploy whatsapp-mcp-bot \
  --source . \
  --region us-central1 \
  --platform managed \
  --allow-unauthenticated \
  --set-env-vars GROQ_API_KEY=your_groq_key,GROQ_API_URL=https://api.groq.com/openai/v1
```

### 3. Copy Public URL
You'll receive a URL like:

```bash
[git clone https://github.com/your-user/whatsapp-mcp-bot.git
cd whatsapp-mcp-bot](https://whatsapp-mcp-bot-xyz.a.run.app)
```
Go to Twilio > Sandbox > Configure > "When a message comes in":
```bash
[[git clone https://github.com/your-user/whatsapp-mcp-bot.git
cd whatsapp-mcp-bot](https://whatsapp-mcp-bot-xyz.a.run.app)](https://whatsapp-mcp-bot-xyz.a.run.app/whatsapp)
```


## 💬 Test It

### 1. Join Twilio Sandbox from your WhatsApp

### 2. Send hi, /help, /agent expert, etc.

### 3. Receive Groq-generated replies from your MCP bot

## 📚 Commands Supported

| Command            | Description                        |
|--------------------|------------------------------------|
| `/reset`           | Clears the conversation memory     |
| `/help`            | Lists available commands           |
| `/agent expert`    | Switches to expert-level assistant |
| `/agent assistant` | Switches back to casual assistant  |

---


## 🧱 Tech Stack

- Python 3.11
- FastAPI
- Twilio Messaging API
- Groq API (LLaMA3)
- Docker
- Google Cloud Run



