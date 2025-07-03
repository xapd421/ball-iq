package dev.xapd421.balliq.backend.repositories;

import org.springframework.data.jpa.repository.JpaRepository;

import dev.xapd421.balliq.backend.entities.Team;

public interface TeamRepository extends JpaRepository<Team, Integer> {
}