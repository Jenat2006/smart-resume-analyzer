import pandas as pd


def recommend_jobs(skills):

    jobs = pd.read_csv("jobs.csv")

    recommended = []

    for _, row in jobs.iterrows():

        required_skills = row["Skills"].lower().split()

        score = 0

        for skill in skills:

            if skill.lower() in required_skills:
                score += 1

        if score > 0:

            recommended.append({
                "Job": row["Job Title"],
                "Score": score
            })

    recommended = sorted(
        recommended,
        key=lambda x: x["Score"],
        reverse=True
    )

    return recommended[:5]