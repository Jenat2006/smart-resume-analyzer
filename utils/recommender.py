import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def recommend_jobs(resume_text):

    jobs = pd.read_csv("jobs.csv")

    job_titles = jobs["Job Title"].tolist()

    job_skills = jobs["Skills"].tolist()

    # Resume + All Job Skills
    documents = [resume_text] + job_skills

    # Convert text to vectors
    vectorizer = TfidfVectorizer()

    tfidf_matrix = vectorizer.fit_transform(documents)

    # Compare resume with every job
    similarity = cosine_similarity(
        tfidf_matrix[0:1],
        tfidf_matrix[1:]
    )[0]

    recommendations = []

    for i in range(len(job_titles)):

        recommendations.append({

            "Job": job_titles[i],

            "Score": round(similarity[i] * 100, 2)

        })

    recommendations = sorted(
        recommendations,
        key=lambda x: x["Score"],
        reverse=True
    )

    return recommendations[:5]
          