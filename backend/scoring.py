def calculate_readiness(interview_score, resume_match, time_score):

    final_score = (
        0.6 * interview_score +
        0.3 * resume_match +
        0.1 * time_score
    )

    return round(final_score, 2)