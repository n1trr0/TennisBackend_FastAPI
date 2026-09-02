from datetime import date
from uuid import UUID

from pydantic import BaseModel


class RankingResponse(BaseModel):
    ranking_id: UUID
    player_id: UUID | None
    points: int
    rank: int
    ranking_date: date
