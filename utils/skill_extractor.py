# List of known skills

SKILLS = [
    "python",
    "java",
    "c++",
    "html",
    "css",
    "javascript",
    "sql",
    "mysql",
    "flask",
    "django",
    "machine learning",
    "deep learning",
    "artificial intelligence",
    "nlp",
    "pandas",
    "numpy",
    "scikit learn",
    "tensorflow",
    "keras",
    "bootstrap",
    "react",
    "git",
    "github",
    "aws",
    "docker",
    "linux"
]


def extract_skills(text):

    text = text.lower()

    found_skills = []

    for skill in SKILLS:

        if skill.lower() in text:

            found_skills.append(skill.title())

    return sorted(list(set(found_skills)))