from fastapi import FastAPI
from nba_api.stats import static
from nba_api.stats import endpoints as end
from nba_api.stats.static import players as pcs
import pandas as pd

from backend.GetMethods import getSearchedPlayers, getCareerSeasons

app = FastAPI()

@app.get("/search")
def returnSearchedPlayers(name: str):
    return getSearchedPlayers(name)
@app.get("/player")
def returnPlayerStats(id: int):
    return getCareerSeasons(id)