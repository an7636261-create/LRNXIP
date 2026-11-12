
import streamlit as st
from resume_parser import extract_resume_data
from job_matcher import calculate_job_match

st.set_page_config(
    page_title="Resume Job Matcher",
    page_icon="📄"
)

st.title("Resume Job Matcher")
st.write("Check how well your resume matches a job description.")

# Upload resume
uploaded_file = st.file_uploader(
    "Upload your Resume (PDF)",
    type=["pdf"]
)

# Enter job description
job_description = st.text_area(
    "Paste Job Description",
    height=200
)

if st.button("Check Job Match"):

    if uploaded_file is None:
        st.warning("Please upload your resume.")

    elif not job_description.strip():
        st.warning("Please enter a job description.")

    else:
        try:
            resume_data = extract_resume_data(uploaded_file)

            result = calculate_job_match(
                resume_data["skills"],
                job_description
            )

            st.subheader("Resume Details")

            st.write("Email:", resume_data["email"])
            st.write("Phone:", resume_data["phone"])
            st.write("Skills:", ", ".join(resume_data["skills"]) or "None found")

            st.subheader("Job Match Results")

            score = result["score"]

            st.metric("Match Percentage", str(score) + "%")
            st.progress(score / 100)

            col1, col2 = st.columns(2)

            with col1:
                st.subheader("Skills Matched")

                if result["matched"]:
                    for skill in result["matched"]:
                        st.success(skill)
                else:
                    st.write("No matched skills.")

            with col2:
                st.subheader("Missing Required Skills")

                if result["missing"]:
                    for skill in result["missing"]:
                        st.error(skill)
                else:
                    st.write("No missing skills.")

        except Exception as e:
            st.error("Error processing resume: " + str(e))
