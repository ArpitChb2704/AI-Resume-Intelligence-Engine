import re

def extract_email(text):
    match = re.search(r"\S+@\S+\.\S+", text)
    return match.group() if match else None

def extract_phone(text):
    match = re.search(r"\+?\d[\d\s-]{8,15}", text)
    return match.group() if match else None