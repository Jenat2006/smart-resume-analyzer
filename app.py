from flask import(
Flask,
render_template,
request,
redirect,
url_for,
session,
send_file,
flash
)

import os

from utils.database import (
    create_database,
    register_user,
    login_user,
    save_resume,
    get_resume_history
)

from utils.resume_parser import extract_resume_text
from utils.preprocess import preprocess_text
from utils.skill_extractor import extract_skills
from utils.recommender import recommend_jobs
from utils.score import calculate_resume_score
from utils.suggestions import generate_suggestions
from utils.skill_gap import find_missing_skills
from utils.pdf_generator import create_pdf


# ===============================
# Flask Configuration
# ===============================

app = Flask(__name__)

app.secret_key = "smart_resume_analyzer_2026"

UPLOAD_FOLDER = "static/uploads"

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

ALLOWED_EXTENSIONS = {"pdf", "docx"}

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

create_database()


# ===============================
# Helper Function
# ===============================

def allowed_file(filename):

    return (
        "." in filename and
        filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS
    )


# ===============================
# Home Page
# ===============================

@app.route("/")
def home():

    return render_template("index.html")


# ===============================
# Register
# ===============================

@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        name = request.form["name"]

        email = request.form["email"]

        password = request.form["password"]

        try:

            register_user(
                name,
                email,
                password
            )

            flash("Registration Successful")

            return redirect(url_for("login"))

        except Exception:

            flash("Email Already Exists")

            return redirect(url_for("register"))

    return render_template("register.html")


# ===============================
# Login
# ===============================

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form["email"]

        password = request.form["password"]

        user = login_user(
            email,
            password
        )

        if user:

            session["email"] = email

            return redirect(
                url_for("dashboard")
            )

        flash("Invalid Login")

    return render_template("login.html")


# ===============================
# Logout
# ===============================

@app.route("/logout")
def logout():

    session.clear()

    return redirect(url_for("home"))
# ===============================
# Upload Resume Page
# ===============================

@app.route("/upload")
def upload():

    if "email" not in session:
        return redirect(url_for("login"))

    return render_template("upload.html")


# ===============================
# Analyze Resume
# ===============================

@app.route("/analyze", methods=["POST"])
def analyze():

    if "email" not in session:
        return redirect(url_for("login"))

    if "resume" not in request.files:
        flash("Please select a resume file.")
        return redirect(url_for("upload"))

    file = request.files["resume"]

    if file.filename == "":
        flash("Please select a file.")
        return redirect(url_for("upload"))

    if not allowed_file(file.filename):
        flash("Only PDF and DOCX files are allowed.")
        return redirect(url_for("upload"))

    filename = file.filename

    filepath = os.path.join(
        app.config["UPLOAD_FOLDER"],
        filename
    )

    file.save(filepath)

    # -----------------------------
    # Resume Processing
    # -----------------------------

    resume_text = extract_resume_text(filepath)

    clean_text = preprocess_text(resume_text)

    skills = extract_skills(clean_text)

    resume_score = calculate_resume_score(
        clean_text,
        skills
    )

    recommended_jobs = recommend_jobs(
        clean_text
    )

    suggestions = generate_suggestions(
        clean_text,
        skills
    )

    missing_skills = find_missing_skills(
        skills
    )

    # -----------------------------
    # Save Resume History
    # -----------------------------

    save_resume(
        session["email"],
        filename,
        resume_score
    )

    return render_template(

        "result.html",

        filename=filename,

        resume_text=resume_text,

        clean_text=clean_text,

        skills=skills,

        resume_score=resume_score,

        recommended_jobs=recommended_jobs,

        suggestions=suggestions,

        missing_skills=missing_skills

    )


# ===============================
# Dashboard
# ===============================

@app.route("/dashboard")
def dashboard():

    if "email" not in session:
        return redirect(url_for("login"))

    history = get_resume_history(
        session["email"]
    )

    return render_template(

        "dashboard.html",

        history=history,

        email=session["email"]

    )
# ===============================
# Download PDF Report
# ===============================

@app.route("/download-report")
def download_report():

    if "email" not in session:
        return redirect(url_for("login"))

    report_file = "resume_report.pdf"

    # Temporary values (baad me actual analysis data pass karenge)
    create_pdf(
        report_file,
        75,
        [],
        [],
        []
    )

    return send_file(
        report_file,
        as_attachment=True
    )


# ===============================
# Run Application
# ===============================

if __name__ == "__main__":

    app.run(
        debug=True
    )