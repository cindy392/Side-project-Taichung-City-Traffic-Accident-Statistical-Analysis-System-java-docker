package com.example.traffic_api.repository; // <-- 注意：這裡是 repository 套件

import java.util.Optional;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import com.example.traffic_api.entity.TrafficMap; // <-- 匯入您要操作的 Entity

// @Repository 註解是可選的，但加上可以讓語意更清晰
@Repository
public interface TrafficMapRepository extends JpaRepository<TrafficMap, Integer> {
    // 裡面是空的！所有神奇的功能都來自於繼承 JpaRepository
    Optional<TrafficMap> findByDistrict(String district);
}
