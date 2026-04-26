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

memory = [
    # {'role':'system','content':'you are a policy managment bot. Where we have a company for software solutions named as Ytech Internationals. Our company is based in Hyderabad/Pakistan.'}
]

@app.route("/chat", methods=["POST"])
def chat():
    try:
        user_message = request.json.get("message")
        memory.append({"role": "user", "content": user_message})
        response = client.chat.completions.create(
            model="openai/gpt-oss-20b:free",
            messages=memory
        )
        assist = response.choices[0].message.content
        memory.append(
            {'role':'assistant','content':assist}
        )
        return jsonify({
            "reply": assist
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
