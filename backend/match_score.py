def calculate_match_score(
    resume_skills,
    jd_skills
):

    matched = set(
        resume_skills
    ).intersection(
        set(jd_skills)
    )

    score = (
        len(matched)
        /
        len(jd_skills)
    ) * 100

    return round(score, 2)

resume_skills = [
    "Python",
    "Git",
    "SQL"
]

jd_skills = [
    "Python",
    "Git",
    "AI",
    "Playwright"
]

print(
    calculate_match_score(
        resume_skills,
        jd_skills
    )
)