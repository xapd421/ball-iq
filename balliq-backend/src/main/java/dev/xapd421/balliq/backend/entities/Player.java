package dev.xapd421.balliq.backend.entities;

import com.fasterxml.jackson.annotation.JsonIgnore;
import jakarta.persistence.*;
import lombok.*;

import java.util.Date;

@Entity
@Table(name="players")
@Getter @Setter @NoArgsConstructor @AllArgsConstructor
public class Player {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "id")
    private Integer id;

    @ManyToOne
    @JoinColumn(name = "team_id")
    private Team team;

    @Column(name = "nba_api_person_id")
    private Integer nbaApiPersonId;

    @Column(name = "first_name")
    private String firstName;

    @Column(name = "last_name")
    private String lastName;

    @Temporal(TemporalType.DATE)
    @Column(name = "birthdate")
    private Date birthdate;

    @Column(name = "school")
    private String school;

    @Column(name = "country")
    private String country;

    @Column(name = "height")
    private String height;

    @Column(name = "weight")
    private Integer weight;

    @Column(name = "season_exp")
    private Integer seasonExp;

    @Column(name = "jersey")
    private Integer jersey;

    @Column(name = "position")
    private String position;

    @Column(name = "roster_status")
    private String rosterStatus;

    @Column(name = "nba_api_team_id")
    private Integer nbaApiTeamId;

    @Column(name = "team_name")
    private String teamName;

    @Column(name = "team_abbreviation", length = 3)
    private String teamAbbreviation;

    @Column(name = "team_code")
    private String teamCode;

    @Column(name = "team_city")
    private String teamCity;

    @Column(name = "player_code")
    private String playerCode;

    @Column(name = "from_year")
    private Integer fromYear;

    @Column(name = "to_year")
    private Integer toYear;

    @Column(name = "dleague_flag")
    private String dleagueFlag;

    @Column(name = "nba_flag")
    private String nbaFlag;

    @Column(name = "games_played_flag")
    private String gamesPlayedFlag;

    @Column(name = "draft_year")
    private Integer draftYear;

    @Column(name = "draft_round")
    private Integer draftRound;

    @Column(name = "draft_number")
    private Integer draftNumber;
}
