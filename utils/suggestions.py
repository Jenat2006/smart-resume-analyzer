# =====================================
# AI Resume Improvement Suggestions
# =====================================

def generate_suggestions(clean_text, skills):

    suggestions = []

    text = clean_text.lower()

    # -------------------------
    # Resume Length
    # -------------------------

    if len(text.split()) < 250:
        suggestions.append(
            "Increase your resume content. A resume with 300–500 words is generally more effective."
        )

    # -------------------------
    # Skills
    # -------------------------

    if len(skills) < 6:
        suggestions.append(
            "Add more technical skills relevant to your target job."
        )

    # -------------------------
    # Projects
    # -------------------------

    if "project" not in text:
        suggestions.append(
            "Include at least 2–3 academic or personal projects."
        )

    # -------------------------
    # Experience
    # -------------------------

    if "experience" not in text and "internship" not in text:
        suggestions.append(
            "Mention internships or practical experience if available."
        )

    # -------------------------
    # Certifications
    # -------------------------

    if "certificate" not in text and "certification" not in text:
        suggestions.append(
            "Add certifications such as NPTEL, Coursera, Udemy or AWS."
        )

    # -------------------------
    # GitHub
    # -------------------------

    if "github" not in text:
        suggestions.append(
            "Add your GitHub profile link."
        )

    # -------------------------
    # LinkedIn
    # -------------------------

    if "linkedin" not in text:
        suggestions.append(
            "Add your LinkedIn profile."
        )

    # -------------------------
    # Achievements
    # -------------------------

    if "achievement" not in text and "hackathon" not in text:
        suggestions.append(
            "Mention achievements, hackathons or coding competitions."
        )

    # -------------------------
    # Default
    # -------------------------

    if not suggestions:
        suggestions.append(
            "Excellent! Your resume looks well structured."
        )

    return suggestions