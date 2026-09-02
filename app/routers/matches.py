from uuid import UUID

from fastapi import APIRouter, HTTPException

from app.routers._errors import raise_database_error
from app.schemas.match import MatchResponse
from app.services import match_service

router = APIRouter(prefix="/matches", tags=["Matches"])


@router.get("", response_model=list[MatchResponse])
def list_matches() -> list[dict]:
    try:
        return match_service.get_matches()
    except Exception as error:
        raise_database_error(error)


@router.get("/{match_id}", response_model=MatchResponse)
def read_match(match_id: UUID) -> dict:
    try:
        match = match_service.get_match(match_id)
    except Exception as error:
        raise_database_error(error)

    if match is None:
        raise HTTPException(status_code=404, detail="Match not found")
    return match
