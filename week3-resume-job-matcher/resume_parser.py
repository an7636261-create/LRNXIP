
import pdfplumber
import re

skills_list = [
    "Python", "SQL", "Java", "React",
    "Git", "Excel", "HTML", "CSS",
    "JavaScript", "Machine Learning"
]

def extract_resume_data(pdf_file):

    text = ""

    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""

    email = re.findall(
        r'[\w\.-]+@[\w\.-]+\.\w+', text
    )

    phone = re.findall(
        r'\b\d{10}\b', text
    )

    found_skills = []

    for skill in skills_list:
        if re.search(
            r"(?<!\w)" + re.escape(skill) + r"(?!\w)",
            text, re.IGNORECASE
        ):
            found_skills.append(skill)

    return {
        "email": email[0] if email else "Not found",
        "phone": phone[0] if phone else "Not found",
        "skills": found_skills
    }
