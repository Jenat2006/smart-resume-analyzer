def calculate_resume_score(text, skills):

    score = 0

    text = text.lower()

    # Contact Details
    if "@" in text:
        score += 10

    # Education
    education_keywords = [
        "b.tech",
        "btech",
        "bachelor",
        "master",
        "m.tech",
        "degree"
    ]

    for word in education_keywords:
        if word in text:
            score += 15
            break

    # Projects
    if "project" in text:
        score += 20

    # Certifications
    if "certification" in text or "certificate" in text:
        score += 10

    # Skills Score
    score += min(len(skills) * 2, 30)

    # Experience
    if "experience" in text:
        score += 15

    if score > 100:
        score = 100

    return score