# ============================================
# Skill Gap Analysis
# ============================================

# Common industry skills
REQUIRED_SKILLS = [

    # Programming
    "Python",
    "Java",
    "C++",
    "SQL",

    # Web
    "HTML",
    "CSS",
    "JavaScript",
    "React",
    "Node.js",
    "Flask",
    "Django",

    # Database
    "MySQL",
    "MongoDB",

    # AI / ML
    "Machine Learning",
    "Deep Learning",
    "Artificial Intelligence",
    "TensorFlow",
    "PyTorch",
    "NLP",

    # Data Science
    "Pandas",
    "NumPy",
    "Scikit-learn",

    # Cloud
    "AWS",
    "Azure",
    "Docker",
    "Kubernetes",

    # Version Control
    "Git",
    "GitHub",

    # Soft Skills
    "Communication",
    "Leadership",
    "Problem Solving",
    "Teamwork"
]


def find_missing_skills(user_skills):

    user_skills = [skill.lower() for skill in user_skills]

    missing = []

    for skill in REQUIRED_SKILLS:

        if skill.lower() not in user_skills:
            missing.append(skill)

    return missing