# ==========================
# Resume ATS Score Calculator
# ==========================

REQUIRED_SKILLS = [

    # Programming
    "python",
    "java",
    "c++",
    "sql",

    # Web
    "html",
    "css",
    "javascript",
    "flask",
    "django",

    # AI / ML
    "machine learning",
    "deep learning",
    "artificial intelligence",
    "tensorflow",
    "pytorch",
    "nlp",

    # Data Science
    "pandas",
    "numpy",
    "scikit-learn",

    # Tools
    "git",
    "github",
    "docker",

    # Soft Skills
    "communication",
    "teamwork",
    "problem solving"
]


def calculate_resume_score(clean_text, skills):

    score = 0

    text = clean_text.lower()

    # -----------------------------
    # Skill Score (70 Marks)
    # -----------------------------

    matched = 0

    for skill in REQUIRED_SKILLS:

        if skill.lower() in text:
            matched += 1

    score += (matched / len(REQUIRED_SKILLS)) * 70

    # -----------------------------
    # Resume Length (15 Marks)
    # -----------------------------

    words = len(text.split())

    if words >= 400:
        score += 15

    elif words >= 250:
        score += 10

    elif words >= 150:
        score += 5

    # -----------------------------
    # Contact Information (10 Marks)
    # -----------------------------

    if "@" in clean_text:
        score += 5

    if any(ch.isdigit() for ch in clean_text):
        score += 5

    # -----------------------------
    # Projects / Experience (5 Marks)
    # -----------------------------

    keywords = [
        "project",
        "experience",
        "internship",
        "research"
    ]

    for word in keywords:

        if word in text:
            score += 1

    score = min(round(score), 100)

    return score