package dev.xapd421.balliq.backend.repositories;

import org.springframework.data.jpa.repository.JpaRepository;

import dev.xapd421.balliq.backend.entities.Player;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;

import java.util.List;

public interface PlayerRepository extends JpaRepository<Player, Integer> {
//   List<Player> findByFirstNameIgnoreCase(String firstName);
//   List<Player> findByLastNameIgnoreCase(String lastName);
//   List<Player> findByFirstNameIgnoreCaseAndLastNameIgnoreCase(String firstName, String lastName);
//   List<Player> findByTeamNameIgnoreCase(String teamName);

//   @Query("SELECT p FROM Player p WHERE " +
//           "(:firstName IS NULL OR  p.firstName = :firstName) AND " +
//           "(:lastName IS NULL OR p.lastName = :lastName) AND " +
//           "(:teamName IS NULL OR p.teamName = :teamName)")
//   List<Player> findByOptionalParameters(
//           @Param("firstName") String firstName,
//           @Param("lastName") String lastName,
//           @Param("teamName") String teamName
//   );
}