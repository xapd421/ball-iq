CREATE DATABASE IF NOT EXISTS ball_iq_db;

USE ball_iq_db;

CREATE TABLE IF NOT EXISTS teams (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nba_api_team_id INT,
    season_year VARCHAR(255),
    team_city VARCHAR(255),
    team_name VARCHAR(255),
    team_abbreviation CHAR(3),
    team_conference VARCHAR(255),
    team_division VARCHAR(255),
    team_code VARCHAR(255),
    team_slug VARCHAR(255),
    wins INT,
    losses INT,
    percentage FLOAT,
    conference_rank INT,
    division_rank INT,
    min_year INT,
    max_year INT
);

CREATE TABLE IF NOT EXISTS players (
    id INT PRIMARY KEY AUTO_INCREMENT,
    team_id INT,
    nba_api_person_id INT,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    birthdate DATE,
    school VARCHAR(255),
    country VARCHAR(255),
    height VARCHAR(255),
    weight INT,
    season_exp INT,
    jersey INT,
    position VARCHAR(255),
    roster_status VARCHAR(255),
    nba_api_team_id INT,
    team_name VARCHAR(255),
    team_abbreviation CHAR(3),
    team_code VARCHAR(255),
    team_city VARCHAR(255),
    player_code VARCHAR(255),
    from_year INT,
    to_year INT,
    dleague_flag VARCHAR(255),
    nba_flag VARCHAR(255),
    games_played_flag VARCHAR(255),
    draft_year INT,
    draft_round INT,
    draft_number INT,
    FOREIGN KEY (team_id) REFERENCES teams(id)
);

CREATE TABLE IF NOT EXISTS players_season_totals (
    id INT PRIMARY KEY AUTO_INCREMENT,
    player_id INT,
    season_end_year INT,
    slug VARCHAR(255),
    name VARCHAR(255),
    positions VARCHAR(255),
    age INT,
    team VARCHAR(255),
    games_played INT,
    games_started INT,
    minutes_played INT,
    made_field_goals INT,
    attempted_field_goals INT,
    made_three_point_field_goals INT,
    attempted_three_point_field_goals INT,
    made_free_throws INT,
    attempted_free_throws INT,
    offensive_rebounds INT,
    defensive_rebounds INT,
    assists INT,
    steals INT,
    blocks INT,
    turnovers INT,
    personal_fouls INT,
    points INT,
    FOREIGN KEY (player_id) REFERENCES players(id)
);

CREATE TABLE IF NOT EXISTS headshots (
    id INT PRIMARY KEY AUTO_INCREMENT,
    player_id INT,
    nba_api_person_id INT NOT NULL,
    season_end_year INT,
    url TEXT,
    FOREIGN KEY (player_id) REFERENCES players(id)
);