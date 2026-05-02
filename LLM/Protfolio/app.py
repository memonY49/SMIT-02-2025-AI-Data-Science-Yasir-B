from flask import Flask, render_template, request, jsonify
from rag_engine import PortfolioRAG

# from projects.sentiment import analyze
# from projects.summarizer import summarize

app = Flask(__name__)


rag = PortfolioRAG()


@app.route("/")
def home():
    return render_template("index.html")



@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()

    if not data or "message" not in data:
        return jsonify({"error": "No message provided"}), 400

    try:
        response = rag.ask(data["message"])
        return jsonify({"response": response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# @app.route("/sentiment", methods=["POST"])
# def sentiment_api():
#     data = request.get_json()

#     if not data or "text" not in data:
#         return jsonify({"error": "No text provided"}), 400

#     try:
#         result = analyze(data["text"])
#         return jsonify({"result": result})
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500


# @app.route("/summarize", methods=["POST"])
# def summarize_api():
#     data = request.get_json()

#     if not data or "text" not in data:
#         return jsonify({"error": "No text provided"}), 400

#     try:
#         summary = summarize(data["text"])
#         return jsonify({"summary": summary})
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500



@app.route("/health")
def health():
    return jsonify({"status": "running"})


if __name__ == "__main__":
    app.run(debug=True)