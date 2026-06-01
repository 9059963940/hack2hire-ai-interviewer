from pypdf import PdfReader
import re
from resume_parser import get_resume_skills


def extract_jd_text(pdf_path):

    reader = PdfReader(pdf_path)

    text = ""

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return text


def extract_role(text):

    roles = [
        "Intern, AI - Software Quality Assurance",
        "Software Quality Assurance",
        "Machine Learning Engineer",
        "Data Scientist",
        "Data Analyst",
        "Software Engineer"
    ]

    text_lower = text.lower()

    for role in roles:
        if role.lower() in text_lower:
            return role

    return "Unknown"


def extract_skills(text):

    skills_db = [
        "Python",
        "Java",
        "JavaScript",
        "SQL",
        "Git",
        "CI",
        "Machine Learning",
        "AI",
        "Playwright",
        "Selenium",
        "Cypress",
        "pytest",
        "JUnit",
        "CSV",
        "JSON",
        "FastAPI",
        "React",
        "Docker",
        "AWS"
    ]

    found_skills = []

    for skill in skills_db:
        if skill.lower() in text.lower():
            found_skills.append(skill)

    return found_skills


def extract_experience(text):

    pattern = r'(\d+)\+?\s*years'

    match = re.search(pattern, text, re.IGNORECASE)

    if match:
        return int(match.group(1))

    return 0


# ⭐ NEW FUNCTION (IMPORTANT FOR PHASE 9)
def build_jd_output(text):

    role = extract_role(text)
    jd_skills = extract_skills(text)
    experience = extract_experience(text)

    resume_skills = get_resume_skills()

    matched = set(resume_skills).intersection(set(jd_skills))

    match_score = 0

    if len(jd_skills) > 0:
        match_score = (len(matched) / len(jd_skills)) * 100

    return {
        "role": role,
        "required_skills": jd_skills,
        "preferred_skills": [],
        "experience": experience,
        "resume_skills": resume_skills,
        "matched_skills": list(matched),
        "match_score": round(match_score, 2)
    }


if __name__ == "__main__":

    text = extract_jd_text("sample_jd.pdf")

    result = build_jd_output(text)

    print(result)