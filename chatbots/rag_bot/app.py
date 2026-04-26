from flask import Flask, render_template, request, jsonify
from rag import load_pdf_text, chunk_text, build_vector_store, retrieve, generate_answer

app = Flask(__name__)

# Load & Prepare Documents
text = load_pdf_text("data/YTech_Info.pdf")
chunks = chunk_text(text)
index, _ = build_vector_store(chunks)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    user_msg = request.json["message"]
    docs = retrieve(user_msg, chunks, index)
    context = "\n".join(docs)
    answer = generate_answer(context, user_msg)
    return jsonify({"reply": answer})



if __name__ == "__main__":
    app.run(debug=True)
