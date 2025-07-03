package dev.xapd421.balliq.backend.entities;

import com.fasterxml.jackson.annotation.JsonIgnore;
import com.fasterxml.jackson.annotation.JsonIgnoreProperties;
import jakarta.persistence.*;

import lombok.*;

import java.util.List;

@Entity
@Table(name = "teams")
@Getter @Setter @NoArgsConstructor @AllArgsConstructor
public class Team {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "id")
    private Integer id;

//    @JsonIgnoreProperties("team")
//    @OneToMany(mappedBy = "team")
//    private List<Player> players;

    @Column(name = "nba_api_team_id")
    private Integer nbaApiTeamId;

    @Column(name = "season_year")
    private String seasonYear;

    @Column(name = "team_city")
    private String teamCity;

    @Column(name = "team_name")
    private String teamName;

    @Column(name = "team_abbreviation", length = 3)
    private String teamAbbreviation;

    @Column(name = "team_conference")
    private String teamConference;

    @Column(name = "team_division")
    private String teamDivision;

    @Column(name = "team_code")
    private String teamCode;

    @Column(name = "team_slug")
    private String teamSlug;

    @Column(name = "wins")
    private Integer wins;

    @Column(name = "losses")
    private Integer losses;

    @Column(name = "percentage")
    private Float percentage;

    @Column(name = "conference_rank")
    private Integer conferenceRank;

    @Column(name = "division_rank")
    private Integer divisionRank;

    @Column(name = "min_year")
    private Integer minYear;

    @Column(name = "max_year")
    private Integer maxYear;
}
