package com.example.traffic_api.entity;

//import lombok.Data;
//import lombok.Getter;
//import lombok.Setter;
import jakarta.persistence.*;
import java.time.LocalDate;
import java.time.LocalTime;
//import lombok.Data; // 推薦使用 Lombok 簡化 Getter/Setter

//@Getter
//@Setter
//@Data
//Lombok套件會自動產生 getters, setters, toString, equals, hashCode

@Entity
@Table(name = "map")
public class TrafficMap {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Integer id;

    @Column(name = "date", nullable = false)
    private LocalDate date = LocalDate.now();

    @Column(name = "time", nullable = false)
    private LocalTime time = LocalTime.now(); // 自動設當前時間

    @Column(name = "district", length = 50, nullable = false)
    private String district = "未設定";

    @Column(name = "latitude", nullable = false)
    private Double latitude = 0.0;

    @Column(name = "longitude", nullable = false)
    private Double longitude = 0.0;

    @Column(name = "injuries", nullable = false)
    private Integer injuries = 0;

    @Column(name = "deaths", nullable = false)
    private Integer deaths= 0;

    // Getter / Setter
    public Integer getId() { return id; }
    public void setId(Integer id) { this.id = id; }

    public LocalDate getDate() { return date; }
    public void setDate(LocalDate date) { this.date = date; }

    public LocalTime getTime() { return time; }
    public void setTime(LocalTime time) { this.time = time; }

    public String getDistrict() { return district; }
    public void setDistrict(String district) { this.district = district; }

    public Double getLatitude() { return latitude; }
    public void setLatitude(Double latitude) { this.latitude = latitude; }

    public Double getLongitude() { return longitude; }
    public void setLongitude(Double longitude) { this.longitude = longitude; }

    public Integer getInjuries() { return injuries; }
    public void setInjuries(Integer injuries) { this.injuries = injuries; }

    public Integer getDeaths() { return deaths; }
    public void setDeaths(Integer deaths) { this.deaths = deaths; }
}