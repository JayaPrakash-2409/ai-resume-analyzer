from flask import Flask, request
from pdfminer.high_level import extract_text
from io import BytesIO

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":

        uploaded_file = request.files["resume"]

        pdf_data = uploaded_file.read()

        text = extract_text(BytesIO(pdf_data))

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