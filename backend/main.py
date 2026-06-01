from fastapi import FastAPI
from pydantic import BaseModel
import random

app = FastAPI()

class QuestionRequest(BaseModel):
    role: str

class EvalRequest(BaseModel):
    question: str
    answer: str

@app.post("/generate-question")
def generate_question(req: QuestionRequest):
    questions = [
        "Explain OOP concepts",
        "What is Python used for?",
        "Explain REST API",
        "What is SQL JOIN?"
    ]
    return {"question": random.choice(questions)}

@app.post("/evaluate")
def evaluate(req: EvalRequest):
    score = random.randint(5, 10)
    return {"score": score}