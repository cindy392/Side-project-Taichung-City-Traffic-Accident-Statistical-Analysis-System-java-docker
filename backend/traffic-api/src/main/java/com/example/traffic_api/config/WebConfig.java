package com.example.traffic_api.config;

import org.springframework.context.annotation.Configuration;
import org.springframework.web.servlet.config.annotation.ResourceHandlerRegistry;
import org.springframework.web.servlet.config.annotation.WebMvcConfigurer;

@Configuration
public class WebConfig implements WebMvcConfigurer {

    /*@Override
    public void addResourceHandlers(ResourceHandlerRegistry registry) {
        // 將 /maps/** 對應到 python_scripts/data/
        registry.addResourceHandler("/maps/**")
                .addResourceLocations("file:/python_scripts/data/");

        
    }*/
    @Override
    public void addResourceHandlers(ResourceHandlerRegistry registry) {
        String currentDir = System.getProperty("user.dir");
        System.out.println("Current working directory: " + currentDir);

        // 修正：不重複 backend/traffic-api
        String dataPath = currentDir + "/python_scripts/data/";
        System.out.println("Serving static files from: " + dataPath);

        registry.addResourceHandler("/maps/**")
                .addResourceLocations("file:" + dataPath);
    }
}

