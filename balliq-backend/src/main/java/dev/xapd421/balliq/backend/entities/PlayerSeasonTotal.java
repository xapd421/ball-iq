package dev.xapd421.balliq.backend.entities;

import jakarta.persistence.*;

import lombok.*;

@Entity
@Table(name = "players_season_totals")
@Getter @Setter @NoArgsConstructor @AllArgsConstructor
public class PlayerSeasonTotal {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "id")
    private Integer id;

    @ManyToOne
    @JoinColumn(name = "player_id", referencedColumnName = "id")
    private Player player;

    @Column(name = "season_end_year")
    private Integer season_end_year;

    @Column(name = "slug")
    private String slug;

    @Column(name = "name")
    private String name;

    @Column(name = "positions")
    private String positions;

    @Column(name = "age")
    private Integer age;

    @Column(name = "team")
    private String team;

    @Column(name = "games_played")
    private Integer gamesPlayed;

    @Column(name = "games_started")
    private Integer gamesStarted;

    @Column(name = "minutes_played")
    private Integer minutesPlayed;

    @Column(name = "made_field_goals")
    private Integer madeFieldGoals;

    @Column(name = "attempted_field_goals")
    private Integer attemptedFieldGoals;

    @Column(name = "offensive_rebounds")
    private Integer offensiveRebounds;

    @Column(name = "defensive_rebounds")
    private Integer defensiveRebounds;

    @Column(name = "assists")
    private Integer assists;

    @Column(name = "steals")
    private Integer steals;

    @Column(name = "blocks")
    private Integer blocks;

    @Column(name = "turnovers")
    private Integer turnovers;

    @Column(name = "personal_fouls")
    private Integer personalFouls;

    @Column(name = "points")
    private Integer points;
}
