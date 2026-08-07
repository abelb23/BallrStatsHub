from nba_api.stats import static
from nba_api.stats import endpoints as end
from nba_api.stats.static import players as pcs
import pandas as pd




def getSearchedPlayers(name: str):
    names = pcs.get_players()
    playerList = {}
    for dicts in names:
        if (name.lower() in dicts["full_name"].lower()):
            playerList[dicts["full_name"]] = dicts["id"]

    return playerList


def getCareerTotals(id: int):
    frame = end.PlayerCareerStats(player_id=id).get_data_frames()[0]

    gp = frame["GP"].sum()

    stats = {"Points": round(frame["PTS"].sum()/gp, 1), "Assists": round(frame["AST"].sum()/gp, 1), "Rebounds": round(frame["REB"].sum()/gp, 1)}

    return stats

def getCareerSeasons(id: int):
    frame = end.PlayerCareerStats(player_id=id).get_data_frames()[0]
    return frame["SEASON_ID"].unique().tolist()





