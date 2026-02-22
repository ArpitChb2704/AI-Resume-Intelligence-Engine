from pydantic import BaseModel
from typing import Optional

class JDRequest(BaseModel):
    resume_text: str
    job_description: str