package dev.xapd421.balliq.backend.controllers;

import dev.xapd421.balliq.backend.entities.Headshot;
import dev.xapd421.balliq.backend.services.HeadshotService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import java.util.List;

import java.util.List;

@RestController
@RequestMapping("/headshot")
public class HeadshotController {
    @Autowired
    private HeadshotService headshotService;

    @GetMapping
    public List<Headshot> getAllHeadshots() {
        return headshotService.getAllHeadshots();
    }

    @GetMapping("/{id}")
    public Headshot getHeadshotById(@PathVariable int id) {
        return headshotService.getHeadshotById(id);
    }
}
