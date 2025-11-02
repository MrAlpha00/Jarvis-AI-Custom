from flask import Flask, request, jsonify
from Backend.Chatbot import Chatbot
from Backend.RealtimeSearchEngine import RealtimeSearchEngine
from Backend.TextToSpeech import TextToSpeech
from dotenv import dotenv_values

env = dotenv_values(".env")
app = Flask(__name__)

@app.route("/")
def home():
    return "Jarvis Web is Online!"

@app.route("/ask", methods=["POST"])
def ask():
    user_text = request.json.get("query", "")
    if not user_text:
        return jsonify({"error": "No query given"}), 400

    # Use your existing logic (like Chatbot or RealtimeSearchEngine)
    answer = Chatbot(user_text)
    TextToSpeech(answer)  # optional
    return jsonify({"answer": answer})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
