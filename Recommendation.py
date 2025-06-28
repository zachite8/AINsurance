from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class RecommendationRequest(BaseModel):
    location: str
    insuranceType: str
    userPreferences: str | None = None

@router.post("/recommend")
def get_recommendation(req: RecommendationRequest):
    return {
        "message": f"Mock recommendation for {req.insuranceType} in {req.location}"
    }
