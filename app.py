import streamlit as st
from pdfminer.high_level import extract_text
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

st.set_page_config(page_title="AI Resume Analyzer", layout="centered")

st.title("🚀 AI Resume Analyzer")
st.markdown("Upload your resume and compare it with a job description")

uploaded_file = st.file_uploader("📄 Upload Resume (PDF)")
job = st.text_area("🧾 Paste Job Description")

if uploaded_file and job:

    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.read())

    resume = extract_text("temp.pdf")

    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([resume, job])
    similarity = cosine_similarity(vectors[0], vectors[1])
    score = similarity[0][0] * 100

    st.subheader("📊 Match Score")
    st.success(f"{round(score, 2)} %")

    skills = ["python", "sql", "machine learning", "data analysis"]

    matched = []
    missing = []

    for skill in skills:
        if skill in resume.lower() and skill in job.lower():
            matched.append(skill)
        elif skill in job.lower():
            missing.append(skill)

    st.subheader("✅ Matched Skills")
    st.write(matched if matched else "None")

    st.subheader("❌ Missing Skills")
    st.write(missing if missing else "None")