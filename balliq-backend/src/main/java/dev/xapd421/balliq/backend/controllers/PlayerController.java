package dev.xapd421.balliq.backend.controllers;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import dev.xapd421.balliq.backend.services.PlayerService;
import dev.xapd421.balliq.backend.entities.Player;

import java.util.List;

@RestController
@RequestMapping("/player")
public class PlayerController {
    @Autowired
    private PlayerService playerService;

//    @GetMapping
//    public List<Player> getAllPlayersByOptionalParameters(
//            @RequestParam(name = "firstName", required = false) String firstName,
//            @RequestParam(name = "lastName", required = false) String lastName,
//            @RequestParam(name = "teamName", required = false) String teamName
//    ) {
//        return playerService.getAllPlayersByOptionalParameters(firstName, lastName, teamName);
//    }

    @GetMapping
    public List<Player> getAllPlayers() {
        return playerService.getAllPlayers();
    }
    
    @GetMapping("/{id}")
    public Player getPlayersById(@PathVariable int id) {
        return playerService.getPlayerById(id);
    }
}
