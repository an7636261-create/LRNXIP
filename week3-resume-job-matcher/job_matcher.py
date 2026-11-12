
import re

skills_list = [
    "Python", "SQL", "Java", "React",
    "Git", "Excel", "HTML", "CSS",
    "JavaScript", "Machine Learning"
]

def calculate_job_match(candidate_skills, job_description):

    required_skills = []

    for skill in skills_list:
        if re.search(r"(?<!\w)" + re.escape(skill) + r"(?!\w)",
                     job_description, re.IGNORECASE):
            required_skills.append(skill)

    matched_skills = []
    missing_skills = []

    for skill in required_skills:
        if skill.lower() in [s.lower() for s in candidate_skills]:
            matched_skills.append(skill)
        else:
            missing_skills.append(skill)

    if len(required_skills) == 0:
        score = 0
    else:
        score = (len(matched_skills) / len(required_skills)) * 100

    return {
        "score": round(score, 2),
        "matched": matched_skills,
        "missing": missing_skills
    }
