def generate_suggestions(text, skills):

    suggestions = []

    text = text.lower()

    # Email
    if "@" not in text:
        suggestions.append("Add an Email Address.")

    # Phone Number
    if "+" not in text and "phone" not in text:
        suggestions.append("Add your Phone Number.")

    # GitHub
    if "github" not in text:
        suggestions.append("Add your GitHub Profile.")

    # LinkedIn
    if "linkedin" not in text:
        suggestions.append("Add your LinkedIn Profile.")

    # Experience
    if "experience" not in text:
        suggestions.append("Add Internship or Work Experience.")

    # Certifications
    if "certification" not in text and "certificate" not in text:
        suggestions.append("Add Certifications.")

    # Projects
    if "project" not in text:
        suggestions.append("Add Academic or Personal Projects.")

    # Skills
    if len(skills) < 8:
        suggestions.append("Include more Technical Skills.")

    return suggestions