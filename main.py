from fastapi import FastAPI, Request, Form
import uvicorn
from twilio.twiml.messaging_response import MessagingResponse
import openai
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

openai.api_key = os.getenv("OPENAI_API_KEY")

@app.post("/whatsapp")
async def whatsapp_webhook(
    Body: str = Form(...),
    From: str = Form(...)
):
    print(f"Incoming from {From}: {Body}")

    # Call OpenAI
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": Body}
            ]
        )
        reply = response.choices[0].message["content"].strip()
    except Exception as e:
        print("Error:", e)
        reply = "Oops, something went wrong."

    twilio_resp = MessagingResponse()
    twilio_resp.message(reply)
    return str(twilio_resp)



# health check
@app.get('/health')
def health_check():
    """
    Health check endpoint.
    :return: 200 if the API is alive.
    """
    response = {"status": 200}

    return response


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8082, reload=True)
