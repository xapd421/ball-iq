package dev.xapd421.balliq.backend.services;

import java.util.List;
import dev.xapd421.balliq.backend.entities.Player;
import dev.xapd421.balliq.backend.repositories.PlayerRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class PlayerService {
    @Autowired
    private PlayerRepository playerRepository;

    public List<Player> getAllPlayers() {
        return playerRepository.findAll();
    }

//    public List<Player> getAllPlayersByOptionalParameters(String firstName, String lastName, String teamName) {
//        return playerRepository.findByOptionalParameters(firstName, lastName, teamName);
//    }

    public Player getPlayerById(int id) {
        return playerRepository.findById(id).get();
    }

//    public List<Player> getPlayerByTeamName(String teamName) {
//        return playerRepository.findByTeamNameIgnoreCase(teamName);
//    }
}