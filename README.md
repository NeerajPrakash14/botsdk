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


## 🛠️ Setup Instructions

### 1. Clone the Project

```bash
git clone https://github.com/your-user/whatsapp-mcp-bot.git
cd whatsapp-mcp-bot
