package dev.xapd421.balliq.backend.services;

import java.util.List;
import dev.xapd421.balliq.backend.entities.Headshot;
import dev.xapd421.balliq.backend.repositories.HeadshotRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class HeadshotService {
    @Autowired
    private HeadshotRepository headshotRepository;

    public List<Headshot> getAllHeadshots() { return headshotRepository.findAll(); }
    public Headshot getHeadshotById(int id) { return headshotRepository.findById(id).get() ; }
}
