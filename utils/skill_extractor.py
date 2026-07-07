# List of known skills

import re

# ==========================
# Master Skill Database
# ==========================

SKILLS = [

    # Programming
    "python","java","c","c++","c#","javascript","typescript","php",
    "ruby","go","kotlin","swift","r","matlab",

    # Web
    "html","css","bootstrap","tailwind","react","angular","vue",
    "node","nodejs","express","django","flask","fastapi",

    # Database
    "mysql","postgresql","sqlite","mongodb","oracle","sql","firebase",

    # AI / ML
    "machine learning","deep learning","artificial intelligence",
    "nlp","computer vision","tensorflow","keras","pytorch",
    "scikit-learn","opencv","pandas","numpy","matplotlib",

    # Data Science
    "data analysis","data science","power bi","tableau","excel",

    # Cloud
    "aws","azure","google cloud","gcp",

    # DevOps
    "docker","kubernetes","git","github","linux","jenkins",

    # Cyber Security
    "network security","ethical hacking","penetration testing",
    "wireshark","metasploit",

    # Mobile
    "android","flutter","react native",

    # Soft Skills
    "leadership","communication","teamwork","problem solving",
    "critical thinking","time management","adaptability"
]


# ==========================
# Extract Skills
# ==========================

def extract_skills(text):

    text = text.lower()

    found_skills = []

    for skill in SKILLS:

        pattern = r"\b" + re.escape(skill) + r"\b"

        if re.search(pattern, text):

            found_skills.append(skill.title())

    return sorted(list(set(found_skills)))