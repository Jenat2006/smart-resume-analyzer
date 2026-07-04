import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def recommend_jobs(resume_text):

    # Load jobs
    jobs = pd.read_csv("jobs.csv")

    job_titles = jobs["Job Title"]

    job_skills = jobs["Skills"]

    # Resume + Job descriptions
    corpus = [resume_text] + job_skills.tolist()

    # TF-IDF
    vectorizer = TfidfVectorizer(stop_words="english")

    tfidf_matrix = vectorizer.fit_transform(corpus)

    # Similarity
    similarity = cosine_similarity(
        tfidf_matrix[0:1],
        tfidf_matrix[1:]
    )

    similarity_scores = similarity.flatten()

    recommendations = []

    for i in range(len(job_titles)):

        recommendations.append({

            "Job": job_titles[i],

            "Score": round(similarity_scores[i] * 100, 2)

        })

    recommendations = sorted(
        recommendations,
        key=lambda x: x["Score"],
        reverse=True
    )

    return recommendations[:5]