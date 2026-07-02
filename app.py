from flask import Flask, render_template, request, redirect, url_for
import os
from utils.resume_parser import extract_resume_text
from utils.preprocess import preprocess_text
from utils.skill_extractor import extract_skills
from utils.recommender import recommend_jobs
from utils.score import calculate_resume_score
from utils.suggestions import generate_suggestions
# ==========================
# Flask App Configuration
# ==========================

app = Flask(__name__)

app.config['SECRET_KEY'] = 'smart_resume_secret_key'

UPLOAD_FOLDER = "static/uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

ALLOWED_EXTENSIONS = {"pdf", "docx"}

# Create upload folder if it does not exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


# ==========================
# Function to Check File Type
# ==========================

def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


# ==========================
# Home Page
# ==========================

@app.route("/")
def home():
    return render_template("index.html")


# ==========================
# Upload Page
# ==========================

@app.route("/upload")
def upload():
    return render_template("upload.html")


# ==========================
# Resume Upload
# ==========================

@app.route("/analyze", methods=["POST"])
def analyze():

    if "resume" not in request.files:
        return "No file selected."

    file = request.files["resume"]

    if file.filename == "":
        return "Please select a resume."

    if file and allowed_file(file.filename):

        filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)

        file.save(filepath)

        resume_text = extract_resume_text(filepath)
        clean_text = preprocess_text(resume_text)
        skills = extract_skills(clean_text)
        resume_score = calculate_resume_score(clean_text, skills)
        suggestions = generate_suggestions(clean_text, skills)
        recommended_jobs = recommend_jobs(clean_text)
        

    return render_template(
    "result.html",
    filename=file.filename,
    resume_text=resume_text,
    clean_text=clean_text,
    skills=skills,
    recommended_jobs=recommended_jobs,
    resume_score=resume_score,
    suggestions=suggestions
    )

    return "Only PDF and DOCX files are allowed."


# ==========================
# Run Flask App
# ==========================

if __name__ == "__main__":
    app.run(debug=True)