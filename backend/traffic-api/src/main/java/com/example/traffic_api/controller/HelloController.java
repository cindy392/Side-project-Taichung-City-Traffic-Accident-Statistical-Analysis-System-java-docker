package com.example.traffic_api.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import com.example.traffic_api.entity.*;
import com.example.traffic_api.repository.TrafficMapRepository;

import java.time.LocalDate;
import java.util.List;

@RestController
public class HelloController {

    @Autowired
    private TrafficMapRepository mapRepository;

    @GetMapping("/")//API：http://localhost:8081/
    public String root() {
        return "HelloController Backend is running!";
    }

    @GetMapping("/api/hello")
    public String hello() {
        return "HelloController from Backend!";
    }

    //連接資料庫
    @GetMapping("/test-db")
    public String testDbConnection() {
        try {
            // 1. 建立一個新部門物件
            TrafficMap newDept = new TrafficMap();
            newDept.setDistrict("測試");
            newDept.setDate(LocalDate.now()); // 給今天的日期
            newDept.setDeaths(0); // <- 這裡給預設值

            // 2. 透過 JPA 存入資料庫
            mapRepository.save(newDept);

            // 3. 透過 JPA 查詢所有資料
            List<TrafficMap> map = mapRepository.findAll();

            return "成功連接資料庫並寫入/讀取資料！目前有 " + map.size() + " 個部門。";
        } catch (Exception e) {
            e.printStackTrace();
            return "資料庫操作失敗: " + e.getMessage();
            
        }
    }

}