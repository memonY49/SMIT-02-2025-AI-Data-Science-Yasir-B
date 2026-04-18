from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

app = FastAPI()


nlp = pipeline("sentiment-analysis")

class PromptRequest(BaseModel):
    text: str


@app.post("/analyze")
def analyze_text(request: PromptRequest):
    result = nlp(request.text)
    return {
        "input": request.text,
        "output": result
    }

# @app.post("/generate")
# async def generate_text(request: PromptRequest):
#     result = nlp(request.text, max_length=50)
#     return {"response": result}