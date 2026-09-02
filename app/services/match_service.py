from uuid import UUID

from app.database import supabase

MATCH_COLUMNS = (
    "surface,tourney_id,w_1stIn,w_1stWon,w_2ndWon,w_bpSaved,w_bpFaced,"
    "l_1stIn,w_SvGms,match_id,tourney_name,tourney_year,winner_id,winner_seed,"
    "winner_entry,loser_id,loser_seed,loser_entry,score,best_of,round,minutes,"
    "w_ace,w_df,w_svpt,l_ace,l_df,l_svpt,winner_rank,loser_rank,"
    "winner_rank_points,loser_rank_points,l_1stWon,l_2ndWon,l_bpSaved,"
    "l_bpFaced,l_SvGms"
)


def get_matches() -> list[dict]:
    return supabase.table("matches").select(MATCH_COLUMNS).execute().data


def get_match(match_id: UUID) -> dict | None:
    data = (
        supabase.table("matches")
        .select(MATCH_COLUMNS)
        .eq("match_id", str(match_id))
        .limit(1)
        .execute()
        .data
    )
    return data[0] if data else None


def get_player_matches(player_id: UUID) -> list[dict]:
    return (
        supabase.table("matches")
        .select(MATCH_COLUMNS)
        .or_(f"winner_id.eq.{player_id},loser_id.eq.{player_id}")
        .execute()
        .data
    )
