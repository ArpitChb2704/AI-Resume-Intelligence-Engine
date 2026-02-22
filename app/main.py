from fastapi import FastAPI, UploadFile, File
import pdfplumber
from app.parser import parse_resume
from app.matcher import match_resume_to_jd
from pydantic import BaseModel

app = FastAPI(title="Resume Parser + Job Matcher")

class JDRequest(BaseModel):
    resume_text: str
    job_desc: str

@app.post("/parse")
def parse_resume_endpoint(file: UploadFile = File(...)):
    text = ""
    with pdfplumber.open(file.file) as pdf:
        for page in pdf.pages:
            content = page.extract_text()
            if content:
                text += content + "\n"
    result = parse_resume(text)
    result["raw_text"] = text
    return result

@app.post("/match")
def match_jd(req: JDRequest):
    return match_resume_to_jd(req.resume_text, req.job_desc)