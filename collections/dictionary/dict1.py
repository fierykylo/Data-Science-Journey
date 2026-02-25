players = {
    1: {
        "name": "Sachin Tendulkar",
        "age": 47,
        "team": "India",
        "role": "Batsman",
        "statistics": {
            "games": 15,
            "runs": 1230,
            "wickets": 11
        },
        "avg_run": 0.0
    },
    2: {
        "name": "Ricky Ponting",
        "age": 49,
        "team": "Australia",
        "role": "Batsman",
        "statistics": {
            "games": 17,
            "runs": 1300,
            "wickets": 15
        },
        "avg_run": 0.0
    },
    3: {
        "name": "Virat Kohli",
        "age": 32,
        "team": "India",
        "role": "Batsman",
        "statistics": {
            "games": 13,
            "runs": 1130,
            "wickets": 12
        },
        "avg_run": 0.0
    },
    4: {
        "name": "Trent Boult",
        "age": 35,
        "team": "New Zealand",
        "role": "Bowler",
        "statistics": {
            "games": 16,
            "runs": 934,
            "wickets": 23
        },
        "avg_run": 0.0
    }
}

#average runs
for player in players.values():
    games = player["statistics"]["games"]
    runs = player["statistics"]["runs"]
    player["avg_run"] = runs / games

#player with highest average run 
maxavg = 0
maxavgtm = ""
for player in players.values():
    runs = player["avg_run"]
    if runs > maxavg:
        maxavg = runs
        maxavgtm = player["team"]
print(maxavgtm)

#sorted by avg

def getAvg(p):
    return p[1]["avg_run"] 

playerList = list(players.items())
playerList.sort(key=getAvg ,reverse = True)

for name,info in playerList:
    print(name, info)