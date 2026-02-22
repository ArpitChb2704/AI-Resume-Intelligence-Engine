import streamlit as st
import requests

st.set_page_config(page_title="AI Resume Parser", layout="wide")

st.title("📄 AI Resume Parser + Job Matcher")

# --------------------------
# Resume Upload Section
# --------------------------
st.header("1️⃣ Upload Resume")

uploaded_file = st.file_uploader("Upload Resume (PDF only)", type=["pdf"])

parsed_data = None

if uploaded_file is not None:
    files = {"file": uploaded_file}
    response = requests.post("http://localhost:8000/parse", files=files)

    if response.status_code == 200:
        parsed_data = response.json()
        st.success("Resume Parsed Successfully ✅")
        st.json(parsed_data)
    else:
        st.error("Backend Error")
        st.text(response.text)

# --------------------------
# Job Description Matching
# --------------------------
st.header("2️⃣ Job Description Matching")

job_desc = st.text_area("Paste Job Description Here")

if st.button("Match Resume with Job Description"):

    if parsed_data is None:
        st.warning("Please upload and parse a resume first.")
    elif not job_desc.strip():
        st.warning("Please paste a job description.")
    else:
        resume_text = parsed_data.get("raw_text", "")

        data = {
            "resume_text": resume_text,
            "job_desc": job_desc
        }

        match_response = requests.post(
            "http://localhost:8000/match",
            json=data
        )

        if match_response.status_code == 200:
            score = match_response.json()["match_score"]
            st.success(f"Match Score: {score}%")
        else:
            st.error("Matching Failed")
            st.text(match_response.text)