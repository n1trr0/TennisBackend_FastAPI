from uuid import UUID

from app.database import supabase

RANKING_COLUMNS = "ranking_id,player_id,points,rank,ranking_date"


def get_rankings() -> list[dict]:
    return supabase.table("rankings").select(RANKING_COLUMNS).execute().data


def get_player_rankings(player_id: UUID) -> list[dict]:
    return (
        supabase.table("rankings")
        .select(RANKING_COLUMNS)
        .eq("player_id", str(player_id))
        .execute()
        .data
    )
