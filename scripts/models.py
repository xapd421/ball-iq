from sqlalchemy import ForeignKey, Column, String, Integer, CHAR, DATE, FLOAT
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Players(Base):
    __tablename__ = "players"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    team_id = Column("team_id", Integer, ForeignKey("teams.id"))
    nba_api_person_id = Column("nba_api_person_id", Integer)
    first_name = Column("first_name", String)
    last_name = Column("last_name", String)
    birthdate = Column("birthdate", DATE)
    school = Column("school", String)
    country = Column("country", String)
    height = Column("height", String)
    weight = Column("weight", Integer)
    season_exp = Column("season_exp", String)
    jersey = Column("jersey", Integer)
    position = Column("position", String)
    roster_status = Column("roster_status", String)
    nba_api_team_id = Column("nba_api_team_id", Integer)
    team_name = Column("team_name", String)
    team_abbreviation = Column("team_abbreviation", CHAR)
    team_code = Column("team_code", String)
    team_city = Column("team_city", String)
    player_code = Column("player_code", String)
    from_year = Column("from_year", Integer)
    to_year = Column("to_year", Integer)
    dleague_flag = Column("dleague_flag", String)
    nba_flag = Column("nba_flag", String)
    games_played_flag = Column("games_played_flag", String)
    draft_year = Column("draft_year", Integer)
    draft_round = Column("draft_round", Integer)
    draft_number = Column("draft_number", Integer)

    def __init__(self, nba_api_person_id=None, first_name=None, last_name=None, birthdate=None, school=None, country=None, height=None, weight=None, season_exp=None, jersey=None, position=None, roster_status=None, nba_api_team_id=None, team_name=None,team_abreviation=None, team_code=None, team_city=None, player_code=None, from_year=None, to_year=None, dleague_flag=None, nba_flag=None, games_played_flag=None, draft_year=None, draft_round=None, draft_number=None):
        self.nba_api_person_id = nba_api_person_id
        self.first_name = first_name
        self.last_name = last_name
        self.birthdate = birthdate
        self.school = school
        self.country = country
        self.height = height
        self.weight = weight
        self.season_exp = season_exp
        self.jersey = jersey
        self.position = position
        self.roster_status = roster_status
        self.nba_api_team_id = nba_api_team_id
        self.team_name = team_name
        self.team_abbreviation = team_abreviation
        self.team_code = team_code
        self.team_city = team_city
        self.player_code = player_code
        self.from_year = from_year
        self.to_year = to_year
        self.dleague_flag = dleague_flag
        self.nba_flag = nba_flag
        self.games_played_flag = games_played_flag
        self.draft_year = draft_year
        self.draft_round = draft_round
        self.draft_number = draft_number

class Teams(Base):
    __tablename__ = "teams"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nba_api_team_id = Column("nba_api_team_id", Integer)
    season_year = Column("season_year", String)
    team_city = Column("team_city", String)
    team_name = Column("team_name", String)
    team_abbreviation = Column("team_abbreviation", String)
    team_conference = Column("team_conference", String)
    team_division = Column("team_division", String)
    team_code = Column("team_code", String)
    team_slug = Column("team_slug", String)
    wins = Column("wins", Integer)
    losses = Column("losses", Integer)
    percentage = Column("percentage", FLOAT)
    conference_rank = Column("conference_rank", Integer)
    division_rank = Column("division_rank", Integer)
    min_year = Column("min_year", Integer)
    max_year = Column("max_year", Integer)

    def __init__(self, nba_api_team_id, season_year, team_city, team_name, team_abbreviation, team_conference, team_division, team_code, team_slug, wins, losses, percentage, conference_rank, division_rank, min_year, max_year):
        self.nba_api_team_id = nba_api_team_id
        self.season_year = season_year
        self.team_city = team_city
        self.team_name = team_name
        self.team_abbreviation = team_abbreviation
        self.team_conference = team_conference
        self.team_division = team_division
        self.team_code = team_code
        self.team_slug = team_slug
        self.wins = wins
        self.losses = losses
        self.percentage = percentage
        self.conference_rank = conference_rank
        self.division_rank = division_rank
        self.min_year = min_year
        self.max_year = max_year

class PlayersSeasonTotals(Base):
    __tablename__ = "players_season_totals"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    player_id = Column("player_id", Integer, ForeignKey("players.id"))
    season_end_year = Column("season_end_year", Integer)
    slug = Column("slug", String)
    name = Column("name", String)
    positions = Column("positions", String)
    age = Column("age", Integer)
    team = Column("team", String)
    games_played = Column("games_played", Integer)
    games_started = Column("games_started", Integer)
    minutes_played = Column("minutes_played", Integer)
    made_field_goals = Column("made_field_goals", Integer)
    attempted_field_goals = Column("attempted_field_goals", Integer)
    made_three_point_field_goals = Column("made_three_point_field_goals", Integer)
    attempted_three_point_field_goals = Column("attempted_three_point_field_goals", Integer)
    made_free_throws = Column("made_free_throws", Integer)
    attempted_free_throws = Column("attempted_free_throws", Integer)
    offensive_rebounds = Column("offensive_rebounds", Integer)
    defensive_rebounds = Column("defensive_rebounds", Integer)
    assists = Column("assists", Integer)
    steals = Column("steals", Integer)
    blocks = Column("blocks", Integer)
    turnovers = Column("turnovers", Integer)
    personal_fouls = Column("personal_fouls", Integer)
    points = Column("points", Integer)

    def __init__(self, season_end_year, slug, name, positions, age, team, games_played, games_started, minutes_played, made_field_goals, attempted_field_goals, made_three_point_field_goals, attempted_three_point_field_goals, made_free_throws, attempted_free_throws, offensive_rebounds, defensive_rebounds, assists, steals, blocks, turnovers, personal_fouls, points):
        self.season_end_year = season_end_year
        self.slug = slug
        self.name = name
        self.positions = positions
        self.age = age
        self.team = team
        self.games_played = games_played
        self.games_started = games_started
        self.minutes_played = minutes_played
        self.made_field_goals = made_field_goals
        self.attempted_field_goals = attempted_field_goals
        self.made_three_point_field_goals = made_three_point_field_goals
        self.attempted_three_point_field_goals = attempted_three_point_field_goals
        self.made_free_throws = made_free_throws
        self.attempted_free_throws = attempted_free_throws
        self.offensive_rebounds = offensive_rebounds
        self.defensive_rebounds = defensive_rebounds
        self.assists = assists
        self.steals = steals
        self.blocks = blocks
        self.turnovers = turnovers
        self.personal_fouls = personal_fouls
        self.points = points

class Headshots(Base):
    __tablename__ = "headshots"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    player_id = Column("player_id", Integer, ForeignKey("players.id"))
    nba_api_person_id = Column("nba_api_person_id", Integer)
    season_end_year = Column("season_end_year", Integer)
    url = Column("url", String)

    def __init__(self, nba_api_person_id, season_end_year, url):
        self.nba_api_person_id = nba_api_person_id
        self.season_end_year = season_end_year
        self.url = url