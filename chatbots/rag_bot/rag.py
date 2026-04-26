import os
import faiss
import numpy as np
from PyPDF2 import PdfReader
from openai import OpenAI
from dotenv import load_dotenv


load_dotenv()


client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key= os.getenv("OPENAI_API_KEY"),
)

#load pdf
def load_pdf_text(path):
    reader = PdfReader(path)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text


#create chunks from text
def chunk_text(text, chunk_size=500, overlap=100):
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start += chunk_size - overlap
    return chunks

#create embaddings of chunks
def embed_texts(texts):
    embeddings = []
    for t in texts:
        emb = client.embeddings.create(
            model="text-embedding-3-small",
            input=t
        )
        embeddings.append(emb.data[0].embedding)
    return np.array(embeddings).astype("float32")


#vector db
def build_vector_store(chunks):
    embeddings = embed_texts(chunks)
    index = faiss.IndexFlatL2(len(embeddings[0]))
    index.add(embeddings)
    return index, embeddings


#find similar docs
def retrieve(query, chunks, index, k=3):
    q_emb = embed_texts([query])
    _, indices = index.search(q_emb, k)
    return [chunks[i] for i in indices[0]]


#answer generation
def generate_answer(context, question):
    prompt = f"""
You are a helpful assistant.
Answer ONLY from the context below.

Context:
{context}

Question:
{question}
"""

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b:free",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2
    )

    return response.choices[0].message.content
