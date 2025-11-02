package com.example.traffic_api.controller;

//爬蟲->下載csv->生成map.html->前端顯示

import com.example.traffic_api.service.AccidentService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletResponse;
import java.io.IOException;

@RestController
@RequestMapping("/api/map")
@CrossOrigin(origins = "http://localhost:3001") // <-- 允許來自 Port 3001 的請求
public class MapController {

    @Autowired
    private AccidentService accidentService;

    // 處理表單提交 (替代 home_confirm.php)
    @PostMapping("/confirm")
    public ResponseEntity<?> confirmAndProcess(
            @RequestParam("year") String year,
            @RequestParam("month") String month,
            HttpServletResponse response) {

        
        
        // 原始 PHP 邏輯: setcookie("year",$year,time()+17280);
        // 在這裡可以用 Spring Session 或 JWT 處理，但簡單起見，我們先著重於業務邏輯。

        String fileName = "臺中市政府警察局" + year + "年" + month + "月份交通事故資料.csv";

        try {
            // 執行 Python 腳本
            accidentService.executePythonScripts(year, month);
            
            // 檢查地圖 HTML 檔案是否存在 (使用新的檢查方法)
            if (accidentService.checkDataFileExists(year, month)) {
                // 成功，返回檔案名稱，讓前端知道要載入哪個地圖
                String htmlFileName = "臺中市政府警察局" + year + "年" + month + "月份交通事故資料.html";
                return ResponseEntity.ok().body("{\"message\": \"資料處理完成，正在載入地圖\", \"status\": \"success\", \"filename\": \"" + htmlFileName + "\"}");
            } else {
                return ResponseEntity.badRequest().body("{\"message\": \"查無資料，請重新查詢或選擇其他月份\", \"status\": \"no_data\"}");
            }
        } catch (IOException | InterruptedException e) {
            return ResponseEntity.internalServerError().body("{\"message\": \"系統處理錯誤: " + e.getMessage() + "\", \"status\": \"error\"}");
        }
    }
    
    // 取得使用者設定的年份和月份 (替代 home.php 中讀取 cookie 的部分)
    // 假設我們在後端用 Session 或其他方式記住使用者的偏好
    @GetMapping("/preferences")
    public ResponseEntity<PreferenceResponse> getUserPreferences() {
        // 實際應用中，會從 Session 或資料庫讀取
        // 這裡暫時模擬：
        // 原始 PHP 邏輯: if(isset($_COOKIE["year"])...) 則顯示歡迎訊息
        boolean hasPreference = false; // 模擬是否已儲存偏好
        String year = "112";
        String month = "3";
        
        // 如果有偏好，可以從 Session/Token 中取得
        // 這裡先寫死，實際需替換為 Session 或資料庫讀取
        if (hasPreference) {
            return ResponseEntity.ok(new PreferenceResponse(year, month, true));
        } else {
            // 如果沒有，使用預設值
            return ResponseEntity.ok(new PreferenceResponse("112", "3", false));
        }
    }
    
    // 簡單的回傳類，用於 /preferences
    static class PreferenceResponse {
        public String year;
        public String month;
        public boolean hasVisited;

        public PreferenceResponse(String year, String month, boolean hasVisited) {
            this.year = year;
            this.month = month;
            this.hasVisited = hasVisited;
        }
    }
}

