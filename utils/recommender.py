import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# ==========================
# Job Recommendation Engine
# ==========================

def recommend_jobs(resume_text):

    try:

        jobs = pd.read_csv("jobs.csv")

    except Exception:

        return []

    # Check required columns
    if "Job" not in jobs.columns or "Skills" not in jobs.columns:
        return []

    # Resume + Job Skills
    documents = [resume_text]

    documents.extend(
        jobs["Skills"].fillna("").tolist()
    )

    # TF-IDF Vectorizer
    vectorizer = TfidfVectorizer(stop_words="english")

    vectors = vectorizer.fit_transform(documents)

    # Resume Vector
    resume_vector = vectors[0]

    # Job Vectors
    job_vectors = vectors[1:]

    similarity = cosine_similarity(
        resume_vector,
        job_vectors
    ).flatten()

    jobs["Score"] = (similarity * 100).round(2)

    jobs = jobs.sort_values(
        by="Score",
        ascending=False
    )

    # Top 5 Jobs
    recommendations = []

    for _, row in jobs.head(5).iterrows():

        recommendations.append({

            "Job": row["Job"],

            "Score": float(row["Score"]),

            "Skills": row["Skills"]

        })

    return recommendations