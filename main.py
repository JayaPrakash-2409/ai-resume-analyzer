from pdfminer.high_level import extract_text
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

resume = extract_text("resume.pdf")
job = "We need python, sql and machine learning skills"

skills = ["python", "sql", "machine learning"]

# AI score
vectorizer = TfidfVectorizer()
vectors = vectorizer.fit_transform([resume, job])
similarity = cosine_similarity(vectors[0], vectors[1])
score = similarity[0][0] * 100

# Missing skills
missing = []
for skill in skills:
    if skill in job.lower() and skill not in resume.lower():
        missing.append(skill)

print("Match Score:", round(score, 2))
print("Missing Skills:", missing)