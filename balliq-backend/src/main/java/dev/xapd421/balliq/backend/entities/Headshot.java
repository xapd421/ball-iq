package dev.xapd421.balliq.backend.entities;

import jakarta.persistence.*;

import lombok.*;

@Entity
@Table(name = "headshots")
@Getter @Setter @NoArgsConstructor @AllArgsConstructor
public class Headshot {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "id")
    private Integer id;

    @ManyToOne
    @JoinColumn(name = "player_id", referencedColumnName = "id")
    private Player player;

    @Column(name = "nba_api_person_id")
    private Integer nbaApiPersonId;

    @Column(name = "season_end_year")
    private Integer seasonEndYear;

    @Column(name = "url")
    private String url;
}
