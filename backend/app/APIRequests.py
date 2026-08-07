from fastapi import FastAPI

from backend.app.GetMethods import getSearchedPlayers, getCareerSeasons

app = FastAPI()

@app.get("/search")
def returnSearchedPlayers(name: str):
    return getSearchedPlayers(name)
@app.get("/player")
def returnPlayerStats(id: int):
    return getCareerSeasons(id)