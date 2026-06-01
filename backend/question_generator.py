import random

TECH_QUESTIONS = {
    "python": [
        "What are Python decorators and where are they used?",
        "Explain difference between list and tuple.",
        "What is memory management in Python?"
    ],
    "sql": [
        "What is normalization in SQL?",
        "Difference between JOIN and UNION?",
        "Write a query to find duplicate records."
    ],
    "powerbi": [
        "What are dashboards in Power BI?",
        "Difference between Power BI and Excel?",
        "What is DAX in Power BI?"
    ],
    "machine learning": [
        "What is overfitting and how do you prevent it?",
        "Explain bias-variance tradeoff.",
        "Difference between supervised and unsupervised learning."
    ],
    "default": [
        "Explain your recent project in detail.",
        "What challenges did you face in your project?",
        "How do you debug a production issue?"
    ]
}


def generate_questions(role, skills):
    skills = skills.lower()

    selected_questions = []

    # match skill keywords
    for key in TECH_QUESTIONS:
        if key in skills:
            selected_questions.extend(TECH_QUESTIONS[key])

    # fallback if nothing matched
    if not selected_questions:
        selected_questions = TECH_QUESTIONS["default"]

    # shuffle and pick 5
    random.shuffle(selected_questions)

    return selected_questions[:5]