from flask import Flask, request, jsonify, render_template
from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv()

app = Flask(__name__)


client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key= os.getenv("OPENAI_API_KEY"),
)


@app.route("/")
def home():
    return render_template("index.html")



chat_history = [
    {"role": "system", "content": "You are a helpful, professional AI assistant and our company is Ytech internationals. you sould only answer for datascience questions and asnwer you do not know anything except datascience "}
]

@app.route("/chat", methods=["POST"])
def chat():
    global chat_history
    try:
        user_message = request.json.get("message")
        chat_history.append({"role": "user", "content": user_message})

        response = client.chat.completions.create(
            model="openai/gpt-oss-20b:free",
            messages=chat_history
        )
        bot_reply = response.choices[0].message.content
        chat_history.append({"role": "assistant", "content": bot_reply})
        return jsonify({
            "reply": bot_reply
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
