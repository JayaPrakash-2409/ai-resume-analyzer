from flask import Flask, request
from pdfminer.high_level import extract_text
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        file = request.files["resume"]

        filepath = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(filepath)

        text = extract_text(filepath)

        return f"""
        <h1>Resume Uploaded Successfully 🚀</h1>
        <h3>Extracted Resume Text:</h3>
        <pre>{text[:3000]}</pre>
        """

    return """
    <h1>AI Resume Analyzer 🚀</h1>

    <form method="POST" enctype="multipart/form-data">
        <input type="file" name="resume" required>
        <button type="submit">Analyze Resume</button>
    </form>
    """

handler = app