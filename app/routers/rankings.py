from fastapi import APIRouter

from app.routers._errors import raise_database_error
from app.schemas.ranking import RankingResponse
from app.services import ranking_service

router = APIRouter(prefix="/rankings", tags=["Rankings"])


@router.get("", response_model=list[RankingResponse])
def list_rankings() -> list[dict]:
    try:
        return ranking_service.get_rankings()
    except Exception as error:
        raise_database_error(error)
