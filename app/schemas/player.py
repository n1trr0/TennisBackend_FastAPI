from datetime import date
from uuid import UUID

from pydantic import BaseModel


class PlayerResponse(BaseModel):
    id: UUID
    name_full: str
    dob: date
    hand: str
    height: int
    name_first: str
    name_last: str
    ioc3: str
    ioc2: str
