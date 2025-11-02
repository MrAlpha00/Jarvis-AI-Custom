from flask import Flask, request, jsonify, render_template
from Backend.Chatbot import Chatbot
from Backend.RealtimeSearchEngine import RealtimeSearchEngine
from Backend.TextToSpeech import TextToSpeech
from dotenv import dotenv_values

env = dotenv_values(".env")

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")   # changed from returning plain text

@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    user_query = data.get("query")

    if not user_query:
        return jsonify({"error": "No query received"}), 400

    if "search" in user_query.lower():
        answer = RealtimeSearchEngine(user_query)
    else:
        answer = Chatbot(user_query)

    try:
        TextToSpeech(answer)
    except Exception as e:
        print("TTS error:", e)

    return jsonify({"answer": answer})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
