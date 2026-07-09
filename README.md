# 🤖 Smart Resume Analyzer (AI Powered)

An AI-powered Resume Analyzer built with **Flask, Python, SQLite, NLP, Machine Learning, and Google Gemini AI**. The application analyzes resumes, calculates ATS scores, extracts skills, recommends jobs, identifies missing skills, generates AI-powered resume reviews, and creates downloadable PDF reports.

---

## 🚀 Features

- 👤 User Registration & Login
- 📄 Upload PDF/DOCX Resume
- 🧠 Resume Text Extraction
- 🔍 NLP Text Preprocessing
- 💡 Skill Extraction
- 📊 ATS Resume Score
- 💼 Job Recommendation
- ⚠️ Missing Skill Detection
- 🤖 AI Resume Review (Google Gemini)
- 📑 PDF Report Generation
- 📈 User Dashboard
- 💾 Resume History
- 🎨 Responsive Bootstrap UI

---

## 🛠️ Technologies Used

### Backend
- Python 3
- Flask
- SQLite

### AI / Machine Learning
- Google Gemini AI
- spaCy
- Scikit-Learn
- Pandas
- NumPy

### Frontend
- HTML5
- CSS3
- Bootstrap 5
- JavaScript

### Other Libraries
- PyPDF2
- python-docx
- ReportLab
- python-dotenv

---

## 📂 Project Structure

```
SmartResumeAnalyzer/
│
├── app.py
├── requirements.txt
├── README.md
├── .env
├── resume.db
│
├── static/
│   ├── css/
│   ├── uploads/
│   └── images/
│
├── templates/
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   ├── dashboard.html
│   ├── upload.html
│   └── result.html
│
├── utils/
│   ├── ai_helper.py
│   ├── database.py
│   ├── preprocess.py
│   ├── recommender.py
│   ├── resume_parser.py
│   ├── score.py
│   ├── skill_extractor.py
│   ├── skill_gap.py
│   ├── suggestions.py
│   └── pdf_generator.py
```

---

# ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/Jenat2006/smart-resume-analyzer.git
```

```bash
cd smart-resume-analyzer
```

---

### Create Virtual Environment

```bash
python -m venv venv
```

Windows

```bash
venv\Scripts\activate
```

---

### Install Requirements

```bash
pip install -r requirements.txt
```

---

### Configure Environment Variable

Create a `.env` file

```env
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
```

---

### Run Project

```bash
python app.py
```

Open browser

```
http://127.0.0.1:5000
```

---

# 📊 Workflow

```
Resume Upload
      │
      ▼
Text Extraction
      │
      ▼
NLP Preprocessing
      │
      ▼
Skill Extraction
      │
      ▼
ATS Score
      │
      ▼
Job Recommendation
      │
      ▼
Missing Skills
      │
      ▼
Gemini AI Resume Review
      │
      ▼
PDF Report
```

---

# 📷 Screenshots

Add screenshots here.

### Home Page

```
images/home.png
```

### Login

```
images/login.png
```

### Upload Resume

```
images/upload.png
```

### Result Page

```
images/result.png
```

### Dashboard

```
images/dashboard.png
```

---

# 🔮 Future Enhancements

- AI Resume Rewrite
- Cover Letter Generator
- LinkedIn Summary Generator
- Interview Question Generator
- Resume Comparison
- Multi-language Resume Analysis
- Resume Ranking System
- Cloud Deployment

---

# 👨‍💻 Author

**Jenat Naj**

B.Tech (Artificial Intelligence & Machine Learning)

---

# ⭐ GitHub Repository

https://github.com/Jenat2006/smart-resume-analyzer

---

## 📜 License

This project is developed for educational and learning purposes.