package dev.xapd421.balliq.backend.services;

import dev.xapd421.balliq.backend.repositories.TeamRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import dev.xapd421.balliq.backend.entities.Team;
import java.util.List;

@Service
public class TeamService {
    @Autowired
    private TeamRepository teamRepository;

    public List<Team> getAllTeams() { return teamRepository.findAll(); }
    public Team getTeamById(int id) { return teamRepository.findById(id).get(); }
}
