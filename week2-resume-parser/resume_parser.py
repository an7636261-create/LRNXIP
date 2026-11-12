import pdfplumber
from pathlib import Path
import re
import json

TECHNICAL_SKILLS = ["Python", "SQL", "React", "Java", "Git", "Excel"]

def extract_text_from_pdf(pdf_path):
    extracted_text = []
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                extracted_text.append(text)
    return "\n".join(extracted_text)

def extract_email(text):
    pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"
    match = re.search(pattern, text)
    return match.group() if match else None

def extract_phone(text):
    pattern = r"(?<!\w)(?:\+91[\s.-]?)?[6-9]\d{9}(?!\w)"
    match = re.search(pattern, text)
    return match.group() if match else None

def extract_name(text):
    for line in text.splitlines():
        line = line.strip()
        if line and not line.lower().startswith(("email:", "phone:")):
            return line
    return None

def match_skills(text):
    matched_skills = []
    for skill in TECHNICAL_SKILLS:
        pattern = r"(?<!\w)" + re.escape(skill) + r"(?!\w)"
        if re.search(pattern, text, re.IGNORECASE):
            matched_skills.append(skill)
    return matched_skills

def parse_resume(pdf_path):
    text = extract_text_from_pdf(pdf_path)
    if not text.strip():
        raise ValueError("No readable text found in the PDF.")
    return {
        "Name": extract_name(text),
        "Email": extract_email(text),
        "Phone": extract_phone(text),
        "Matched Skills": match_skills(text)
    }

def save_to_json(candidate, output_path):
    with open(output_path, "w", encoding="utf-8") as file:
        json.dump(candidate, file, indent=4)

def main():
    pdf_path = Path("sample_resumes/sample_resume.pdf")
    output_path = Path("parsed_resume.json")
    if not pdf_path.is_file():
        print(f"Error: Resume PDF not found: {pdf_path}")
        return
    try:
        candidate = parse_resume(pdf_path)
        save_to_json(candidate, output_path)
        print("Resume parsed successfully!")
        print(json.dumps(candidate, indent=4))
        print(f"JSON saved to: {output_path}")
    except Exception as error:
        print(f"Error processing resume: {error}")

if __name__ == "__main__":
    main()
