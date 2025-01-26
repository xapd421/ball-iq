from database import Session
session = Session()

# import players
from import_data import *
from models import Players, Teams, PlayersSeasonTotals, Headshots

def add_player(session, new_player):
    player = session.query(Players).filter(Players.nba_api_person_id == new_player[0]).first()
    if (player != None):
        player.nba_api_person_id = new_player[0] if (new_player[0]) else None
        player.first_name = new_player[1] if (new_player[1]) else None
        player.last_name = new_player[2] if (new_player[2]) else None
        player.birthdate = new_player[7] if (new_player[7]) else None
        player.school = new_player[8] if (new_player[8]) else None
        player.country = new_player[9] if (new_player[9]) else None
        player.height = new_player[11] if (new_player[11]) else None
        player.weight = new_player[12] if (new_player[12]) else None
        player.season_exp=new_player[13] if (new_player[13]) else None
        player.jersey = new_player[14] if (new_player[14]) else None
        player.position = new_player[15] if (new_player[15]) else None
        player.roster_status = new_player[16] if (new_player[16]) else None
        player.nba_api_team_id = new_player[18] if (new_player[18]) else None
        player.team_name = new_player[19] if (new_player[19]) else None
        player.team_abreviation = new_player[20] if (new_player[20]) else None
        player.team_code = new_player[21] if (new_player[21]) else None
        player.team_city = new_player[22] if (new_player[22]) else None
        player.player_code = new_player[23] if (new_player[23]) else None
        player.from_year = new_player[24] if (new_player[24]) else None
        player.to_year = new_player[25] if (new_player[25]) else None
        player.dleague_flag = new_player[26] if (new_player[26]) else None
        player.nba_flag = new_player[27] if (new_player[27]) else None
        player.games_played_flag = new_player[28] if (new_player[28]) else None
        player.draft_year = new_player[29] if type(new_player[29]) == int else 0
        player.draft_round = new_player[30] if type(new_player[30]) == int else 0
        player.draft_number = new_player[31] if type(new_player[31]) == int else 0
    else:
        player = Players(
            nba_api_person_id=new_player[0] if (new_player[0]) else None,
            first_name=new_player[1] if (new_player[1]) else None,
            last_name=new_player[2] if (new_player[2]) else None,
            birthdate=new_player[7] if (new_player[7]) else None,
            school=new_player[8] if (new_player[8]) else None,
            country=new_player[9] if (new_player[9]) else None,
            height=new_player[11] if (new_player[11]) else None,
            weight=new_player[12] if (new_player[12]) else None,
            season_exp=new_player[13] if (new_player[13]) else None,
            jersey=new_player[14] if (new_player[14]) else None,
            position=new_player[15] if (new_player[15]) else None,
            roster_status=new_player[16] if (new_player[16]) else None,
            nba_api_team_id=new_player[18] if (new_player[18]) else None,
            team_name=new_player[19] if (new_player[19]) else None,
            team_abreviation=new_player[20] if (new_player[20]) else None,
            team_code=new_player[21] if (new_player[21]) else None,
            team_city=new_player[22] if (new_player[22]) else None,
            player_code=new_player[23] if (new_player[23]) else None,
            from_year=new_player[24] if (new_player[24]) else None,
            to_year=new_player[25] if (new_player[25]) else None,
            dleague_flag=new_player[26] if (new_player[26]) else None,
            nba_flag=new_player[27] if (new_player[27]) else None,
            games_played_flag=new_player[28] if (new_player[28]) else None,
            draft_year=new_player[29] if type(new_player[29]) == int else 0,
            draft_round=new_player[30] if type(new_player[30]) == int else 0,
            draft_number=new_player[31] if type(new_player[31]) == int else 0)
        session.add(player)

# import teams
def add_team(session, new_team):
    team = session.query(Teams).filter(Teams.nba_api_team_id == new_team[0]).first()
    if (team != None):
        team.nba_api_team_id = new_team[0]
        team.season_year = new_team[1]
        team.team_city = new_team[2]
        team.team_name = new_team[3]
        team.team_abbreviation = new_team[4]
        team.team_conference = new_team[5]
        team.team_division = new_team[6]
        team.team_code = new_team[7]
        team.team_slug = new_team[8]
        team.wins = new_team[9]
        team.losses = new_team[10]
        team.percentage = new_team[11]
        team.conference_rank = new_team[12]
        team.division_rank = new_team[13]
        team.min_year = new_team[14]
        team.max_year = new_team[15]
    else:
        team = Teams(
            nba_api_team_id=new_team[0],
            season_year=new_team[1],
            team_city=new_team[2],
            team_name=new_team[3],
            team_abbreviation=new_team[4],
            team_conference=new_team[5],
            team_division=new_team[6],
            team_code=new_team[7],
            team_slug=new_team[8],
            wins=new_team[9],
            losses=new_team[10],
            percentage=new_team[11],
            conference_rank=new_team[12],
            division_rank=new_team[13],
            min_year=new_team[14],
            max_year=new_team[15]
        )
        session.add(team)

# import season totals
def add_season_total(session, new_season_total, season_end_year):
    season_total = session.query(PlayersSeasonTotals).filter(PlayersSeasonTotals.name == new_season_total['name']).first()
    if (season_total != None):
        season_total.season_end_year = season_end_year
        season_total.slug = new_season_total['slug']
        season_total.name = new_season_total['name']
        season_total.positions = new_season_total['positions']
        season_total.age = new_season_total['age']
        season_total.team = new_season_total['team']
        season_total.games_played = new_season_total['games_played']
        season_total.games_started = new_season_total['games_started']
        season_total.minutes_played = new_season_total['minutes_played']
        season_total.made_field_goals = new_season_total['made_field_goals']
        season_total.attempted_field_goals = new_season_total['attempted_field_goals']
        season_total.made_three_point_field_goals = new_season_total['made_three_point_field_goals']
        season_total.attempted_three_point_field_goals = new_season_total['attempted_three_point_field_goals']
        season_total.made_free_throws = new_season_total['made_free_throws']
        season_total.attempted_free_throws = new_season_total['attempted_free_throws']
        season_total.offensive_rebounds = new_season_total['offensive_rebounds']
        season_total.defensive_rebounds = new_season_total['defensive_rebounds']
        season_total.assists = new_season_total['assists']
        season_total.steals = new_season_total['steals']
        season_total.blocks = new_season_total['blocks']
        season_total.turnovers = new_season_total['turnovers']
        season_total.personal_fouls = new_season_total['personal_fouls']
        season_total.points = new_season_total['points']
    else:
        season_total = PlayersSeasonTotals(
            season_end_year=season_end_year,
            slug=new_season_total['slug'],
            name=new_season_total['name'],
            positions=new_season_total['positions'],
            age=new_season_total['age'],
            team=new_season_total['team'],
            games_played=new_season_total['games_played'],
            games_started=new_season_total['games_started'],
            minutes_played=new_season_total['minutes_played'],
            made_field_goals=new_season_total['made_field_goals'],
            attempted_field_goals=new_season_total['attempted_field_goals'],
            made_three_point_field_goals=new_season_total['made_three_point_field_goals'],
            attempted_three_point_field_goals=new_season_total['attempted_three_point_field_goals'],
            made_free_throws=new_season_total['made_free_throws'],
            attempted_free_throws=new_season_total['attempted_free_throws'],
            offensive_rebounds=new_season_total['offensive_rebounds'],
            defensive_rebounds=new_season_total['defensive_rebounds'],
            assists=new_season_total['assists'],
            steals=new_season_total['steals'],
            blocks=new_season_total['blocks'],
            turnovers=new_season_total['turnovers'],
            personal_fouls=new_season_total['personal_fouls'],
            points=new_season_total['points']
        )
        session.add(season_total)

# import headshots
def add_headshot(session, nba_api_person_id, season_end_year, url):
    headshot = session.query(Headshots).filter(Headshots.nba_api_person_id == nba_api_person_id).first()
    if (headshot != None):
        headshot.season_end_year = season_end_year
        headshot.url = url
    else:
        headshot = Headshots(
            nba_api_person_id=nba_api_person_id,
            season_end_year=season_end_year,
            url=url
        )
        session.add(headshot)

# sets foreign keys
def link_foreign_keys():
    all_players = session.query(Players).all()
    all_teams = session.query(Teams).all()
    all_season_totals = session.query(PlayersSeasonTotals).all()
    all_headshots = session.query(Headshots).all()
    # set players.team_id foreign key to team.id
    for player in all_players:
        for team in all_teams:
            if player.nba_api_team_id == team.nba_api_team_id:
                player.team_id = team.id
    # set players_season_totals.player_id foreign key to player.id
    for season_total in all_season_totals:
        for player in all_players:
            if (player.first_name in season_total.name) and (player.last_name in season_total.name):
                season_total.player_id = player.id
    # set headshots.player_id foreign key to player.id
    for headshot in all_headshots:
        for player in all_players:
            if headshot.nba_api_person_id == player.nba_api_person_id:
                headshot.player_id = player.id

active_players = getActivePlayers()
for active_player in active_players:
    add_player(session, active_player)

current_teams = getCurrentTeams()
for current_team in current_teams:
    add_team(session, current_team)

current_season_end_year = 2025
season_totals = getPlayerSeasonTotalsBasic(current_season_end_year)
for season_total in season_totals:
    add_season_total(session, season_total, current_season_end_year)    

for active_player in active_players:
    id = active_player[0]
    url = saveHeadshot(id, "./assets")
    add_headshot(session, id, current_season_end_year, url)

link_foreign_keys()

session.commit()