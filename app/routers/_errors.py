from typing import NoReturn

from fastapi import HTTPException


def raise_database_error(error: Exception) -> NoReturn:
    raise HTTPException(
        status_code=503,
        detail="Supabase is unavailable",
    ) from error
