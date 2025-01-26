from nba_api.stats.endpoints import commonplayerinfo, teaminfocommon
from nba_api.stats.static import players, teams

from math import ceil
from time import sleep

# import all active players in batches with a slight delay
def getActivePlayers(batch_size=10, sleep_duration=5):
    active_players = players.get_active_players()
    start = 0; length = len(active_players); list = []
    for i in range(ceil(length/batch_size)):
        upperBound = (start + batch_size) if (start + batch_size <= length) else (length)
        for i in range(start, upperBound):
            data = commonplayerinfo.CommonPlayerInfo(player_id=active_players[i]['id']).get_dict()["resultSets"][0]["rowSet"][0]
            list.append(data)
        start += batch_size
        sleep(sleep_duration)
    return list

def getPlayerById(id):
    data = commonplayerinfo.CommonPlayerInfo(player_id=id).get_dict()["resultSets"][0]["rowSet"][0]
    return data


# import all active players in batches with a slight delay
def getCurrentTeams(batch_size=10, sleep_duration=5):
    current_teams = teams.get_teams()
    start = 0; length = len(current_teams); list = []
    for i in range(ceil(length/batch_size)):
        upperBound = (start + batch_size) if (start + batch_size <= length) else (length)
        for i in range(start, upperBound):
            data = teaminfocommon.TeamInfoCommon(team_id=current_teams[i]['id']).get_dict()['resultSets'][0]['rowSet'][0]
            list.append(data)
        start += batch_size
        sleep(sleep_duration)
    return list

def getTeamById(id):
    data = teaminfocommon.TeamInfoCommon(team_id=id).get_dict()['resultSets'][0]['rowSet'][0]
    return data

from basketball_reference_web_scraper import client

# get player season totals (basic stats) from specific season
def getPlayerSeasonTotalsBasic(season_end_year=2025):
    return client.players_season_totals(season_end_year=2025)

from nba_headshot_downloader import headshots
from os import path
from pathlib import Path

# download headshot and return the public url
def saveHeadshot(id, target_directory=''):
    headshot_path = f'{target_directory}/{id}.png'
    if not path.exists(headshot_path):
        headshots.getHeadshotById(id, target_directory)
    return str(Path(headshot_path).resolve())