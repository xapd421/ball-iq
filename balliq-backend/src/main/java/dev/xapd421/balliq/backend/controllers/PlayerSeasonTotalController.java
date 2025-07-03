package dev.xapd421.balliq.backend.controllers;

import dev.xapd421.balliq.backend.entities.PlayerSeasonTotal;
import dev.xapd421.balliq.backend.services.PlayerSeasonTotalService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RestController
@RequestMapping("/playerseasontotal")
public class PlayerSeasonTotalController {
    @Autowired
    private PlayerSeasonTotalService playerSeasonTotalService;

    @GetMapping
    private List<PlayerSeasonTotal> getAllPlayerSeasonTotals() {
        return playerSeasonTotalService.getAllTotals();
    }

    @GetMapping("/{id}")
    private PlayerSeasonTotal getPlayerSeasonTotalById(@PathVariable int id) {
        return playerSeasonTotalService.getTotalById(id);
    }
}
