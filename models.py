from pydantic import BaseModel
from typing import List

class StoryRequest(BaseModel):
    story: str
    prompt: str

class InsightsResponse(BaseModel):
    insights: List[str]
