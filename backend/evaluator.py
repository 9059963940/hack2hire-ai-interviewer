import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")


def evaluate_answer(question, answer):

    prompt = f"""
    Evaluate this interview answer.

    Question:
    {question}

    Answer:
    {answer}

    Score based on:
    - Accuracy
    - Clarity
    - Depth
    - Relevance

    Return ONLY JSON:
    {{
      "accuracy": 0-10,
      "clarity": 0-10,
      "depth": 0-10,
      "relevance": 0-10
    }}
    """

    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response["choices"][0]["message"]["content"]