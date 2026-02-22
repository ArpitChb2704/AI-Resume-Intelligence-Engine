import spacy
from models.skill_db import SKILL_CATEGORIES
from app.utils import extract_email, extract_phone

nlp = spacy.load("en_core_web_sm")

def extract_name(text):
    doc = nlp(text)
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            return ent.text
    return None

def extract_skills(text):
    text = text.lower()
    skills = {}
    for cat, skill_list in SKILL_CATEGORIES.items():
        skills[cat] = [s for s in skill_list if s in text]
    return skills

def parse_resume(text):
    return {
        "name": extract_name(text),
        "email": extract_email(text),
        "phone": extract_phone(text),
        "skills": extract_skills(text),
    }