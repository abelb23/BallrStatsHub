from fastapi import FastAPI
from nba_api.stats import static
from nba_api.stats.endpoints import PlayerCareerStats
from nba_api.stats.static import players as pcs
import pandas as pd

app = FastAPI()

@app.get("/search")
def getListPlayers(name: str):
    names = pcs.get_players(name)
    playerList = []
    for player in names:
        playerList.append(player["name"])
    return playerList