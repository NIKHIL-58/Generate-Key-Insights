from fastapi import APIRouter
from app.services import process_story
from app.models import StoryRequest, InsightsResponse

router = APIRouter()

@router.post("/generate-insights", response_model=InsightsResponse)
def generate_insights(request: StoryRequest):
    """
    Endpoint to generate key insights from a long story.
    """
    insights = process_story(request.story, request.prompt)
    return {"insights": insights}
