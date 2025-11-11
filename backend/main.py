from fastapi import FastAPI;
from nba_api.stats import static
from nba_api.stats.endpoints import PlayerCareerStats
from nba_api.stats.static.players import find_players_by_full_name
import pandas as pd

app = FastAPI();

while (True):
    hold = input("Which Player Do You Want To Search?\n")
    if (isinstance(hold, str) != True):
        print("Please enter a valid input\n")
    if (find_players_by_full_name(hold) != None):
        player = find_players_by_full_name(hold)
        id = player[0]["id"]
        frames = PlayerCareerStats(player_id=id).get_data_frames()
        reg_szn = frames[0]
        row = reg_szn[reg_szn["SEASON_ID"] == "2025-26"]
        if (row.empty):
            print("Player Has Not Played This Season")
            exit()
        break
    else:
        print("Please enter a valid input\n")





print(round(row["PTS"].values[0]/row["GP"].values[0], 1))

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id};