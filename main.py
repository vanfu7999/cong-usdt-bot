
import os
import requests
from flask import Flask, request

app = Flask(__name__)

BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")
TARGET_URL = os.environ.get("TARGET_URL")

@app.route('/')
def home():
    return "Bot is running!"

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    try:
        message = f"Đã nhận dữ liệu: {data}"
        requests.get(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage", params={
            "chat_id": CHAT_ID,
            "text": message
        })
    except Exception as e:
        return str(e), 500
    return "OK", 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000)
