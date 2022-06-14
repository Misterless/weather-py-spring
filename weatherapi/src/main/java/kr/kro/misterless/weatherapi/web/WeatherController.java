package kr.kro.misterless.weatherapi.web;

import org.springframework.data.domain.PageRequest;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;

import kr.kro.misterless.weatherapi.domain.WeatherRepository;
import lombok.RequiredArgsConstructor;

@RequiredArgsConstructor
@Controller
public class WeatherController {
    
    private final WeatherRepository weatherRepository;

    @GetMapping("/weather")
    public  String we (@RequestParam(defaultValue = "0") Integer page, Model model) {
        PageRequest pq = PageRequest.of(page, 25);
        model.addAttribute("weathers", weatherRepository.findAll(pq));

        return "/weather";
    }
    @GetMapping("/test")
    public String test () {
        return "test";
    }
}
