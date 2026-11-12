# Resume Parser & Job Skill Matcher System

## Domain Track
Python Programming

## Project Overview

The **Resume Parser & Job Skill Matcher System** is a Python-based application that extracts useful information from a candidate's resume PDF.

The system reads the resume, extracts the candidate's contact details, identifies technical skills, and stores the parsed information in a structured JSON file.

## Tech Stack

- Python 3
- pdfplumber
- Regular Expressions (`re`)
- JSON

## Features

1. Extracts text from PDF resume files.
2. Extracts the candidate's email address.
3. Extracts the candidate's phone number.
4. Matches technical skills from a predefined skill list.
5. Stores the parsed candidate profile in JSON format.
6. Handles missing resume files and unreadable PDF content.

## Technical Skills Matched

The current system checks for:

- Python
- SQL
- React
- Java
- Git
- Excel

## Project Structure

```text
week2-resume-parser/
│
├── resume_parser.py
├── parsed_resume.json
├── README.md
├── requirements.txt
│
└── sample_resumes/
    └── sample_resume.pdf
```

## Installation

Install the required Python library using:

```bash
python -m pip install pdfplumber
```

## How to Run

1. Place the resume PDF inside the `sample_resumes` folder.
2. Make sure the file is named `sample_resume.pdf`.
3. Open the project folder in VS Code.
4. Run the following command:

```bash
python resume_parser.py
```

## Output

After successful execution, the program displays the extracted candidate information in the terminal and creates:

```text
parsed_resume.json
```

Example output:

```json
{
    "Name": "RAHUL SHARMA",
    "Email": "rahul.sharma25@example.com",
    "Phone": "+91 9876543210",
    "Matched Skills": [
        "Python",
        "SQL",
        "React",
        "Java",
        "Git",
        "Excel"
    ]
}
```

## Learning Outcomes

Through this project, I learned how to:

- Extract text from PDF documents using Python.
- Use regular expressions to identify specific information.
- Match technical skills from unstructured text.
- Work with JSON files for structured data storage.
- Organize a Python project for GitHub submission.

## Note

The included resume is a fictional sample resume created only for testing and demonstration purposes. The contact information and other details are not real.