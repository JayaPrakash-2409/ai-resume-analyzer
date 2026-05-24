from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>AI Resume Analyzer 🚀</h1>
    <p>Successfully deployed on Vercel</p>
    """

# Vercel entry point
handler = app