package dev.xapd421.balliq.backend.services;

import dev.xapd421.balliq.backend.repositories.PlayerSeasonTotalRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import dev.xapd421.balliq.backend.entities.PlayerSeasonTotal;
import java.util.List;

@Service
public class PlayerSeasonTotalService {
    @Autowired
    private PlayerSeasonTotalRepository playerSeasonTotalRepository;

    public List<PlayerSeasonTotal> getAllTotals() { return playerSeasonTotalRepository.findAll(); }
    public PlayerSeasonTotal getTotalById(int id) { return playerSeasonTotalRepository.findById(id).get(); }
}
