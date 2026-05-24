from flask import Flask, request, render_template
from pdfminer.high_level import extract_text
from io import BytesIO

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    text = ""
    score = 0
    found_skills = []
    suggestions = []

    if request.method == "POST":

        uploaded_file = request.files["resume"]

        pdf_data = uploaded_file.read()

        text = extract_text(BytesIO(pdf_data))

        # ATS Score

        keywords = [
            "Python",
            "Machine Learning",
            "NLP",
            "IoT",
            "SQL",
            "FastAPI"
        ]

        for keyword in keywords:
            if keyword.lower() in text.lower():
                score += 15

        if score > 100:
            score = 100

        # Skill Detection

        skills = [
            "Python",
            "Machine Learning",
            "IoT",
            "NLP",
            "FastAPI",
            "MATLAB"
        ]

        for skill in skills:
            if skill.lower() in text.lower():
                found_skills.append(skill)

        # Suggestions

        if "internship" not in text.lower():
            suggestions.append("Add internship experience")

        if "projects" not in text.lower():
            suggestions.append("Add more projects")

        if len(text) < 1500:
            suggestions.append("Resume content is short")

    return render_template(
        "index.html",
        text=text,
        score=score,
        skills=found_skills,
        suggestions=suggestions
    )

handler = app