package com.example.traffic_api.service;

import org.springframework.stereotype.Service;

import java.io.File;
import java.io.IOException;

@Service
public class AccidentService {
    
    // 假設地圖檔案的目標路徑，需要與 React 的公共目錄或 Nginx 的靜態資源路徑一致
    //private static final String DATA_DIR = "/data/"; // Docker Volume 掛載的路徑

     // ✅ 改成本機實際的 data 資料夾路徑
    private static final String DATA_DIR = "C:\\Users\\cindy\\OneDrive\\Desktop\\專案\\台中市交通事故分析系統\\backend\\traffic-api\\python_scripts\\data";

    // ✅ 改成本機的 scripts 路徑
    private static final String SCRIPTS_DIR = "C:\\Users\\cindy\\OneDrive\\Desktop\\專案\\台中市交通事故分析系統\\backend\\traffic-api\\python_scripts";

    // 執行 Python 腳本的邏輯 (map.python 替代了 map.py)
    public void executePythonScripts(String year, String month) throws IOException, InterruptedException {
        // 1. 執行 search.py (爬蟲/資料獲取)
        System.out.println("Executing search.py for " + year + "/" + month);
        ProcessBuilder pbSearch = new ProcessBuilder("python", SCRIPTS_DIR + "\\search.py", year, month);
        // 設定工作目錄
        pbSearch.directory(new File(DATA_DIR));
        
        // 設定工作目錄，如果 Python 腳本有任何相對路徑讀寫，會從這裡開始
        // 這裡設為 null 讓它從應用程式的當前工作目錄開始，但建議在 Python 腳本內使用 /data/ 絕對路徑
        
        Process processSearch = pbSearch.start();
        int exitCodeSearch = processSearch.waitFor();
        
        // 【重要：讀取並打印 Python 輸出和錯誤流，方便調試】
        // 這是 Java 呼叫外部程式碼最容易失敗的地方，必須捕獲輸出
        printProcessOutput(processSearch);

        if (exitCodeSearch != 0) {
            throw new RuntimeException("AccidentService.java->search.py/Search Python script failed with exit code: " + exitCodeSearch);
        }
        
        
        // 2. 執行 map.python
        // 假設 map.python 腳本已經被複製到 /scripts/map.python
        // year 和 month 作為命令行參數，供 Python 腳本使用 (sys.argv[1] 和 sys.argv[2])
        ProcessBuilder pbMap = new ProcessBuilder("python", SCRIPTS_DIR + "\\map.py", year, month);

        // 設定工作目錄
        pbMap.directory(new File(DATA_DIR));
        
        // **重要：設定環境變數或工作目錄**
        // 如果 Python 腳本需要讀取 CSV 檔案，它必須知道檔案在哪裡。
        // 假設 CSV 檔案在 /data/ 目錄下。你需要確保 search.py 將 CSV 檔案存到 /data/。
        
        //啟動 Python 程式
        Process processMap = pbMap.start();
        printProcessOutput(processMap);
        
        // 捕獲 Python 腳本的輸出（如果需要調試）
        // new Thread(() -> { try { new BufferedReader(new InputStreamReader(processMap.getInputStream())).lines().forEach(System.out::println); } catch (IOException e) { e.printStackTrace(); } }).start();
        // new Thread(() -> { try { new BufferedReader(new InputStreamReader(processMap.getErrorStream())).lines().forEach(System.err::println); } catch (IOException e) { e.printStackTrace(); } }).start();

        int exitCode = processMap.waitFor(); // 等待執行完成
        if (exitCode != 0) {
            throw new RuntimeException("AccidentService.java->Map.py/Map Python script failed with exit code: " + exitCode);
        }
    }

    // 檢查地圖 HTML 檔案是否存在 (現在檢查的是 .html)
    public boolean checkDataFileExists(String year, String month) {
        String htmlFileName = "臺中市政府警察局" + year + "年" + month + "月份交通事故資料.html";
        File file = new File(DATA_DIR + "\\" + htmlFileName); 
        return file.exists();
    }

    // 新增一個輔助方法來讀取 Python 腳本的輸出
    private void printProcessOutput(Process process) throws IOException {
        // 讀取標準輸出
        try (java.io.BufferedReader reader = new java.io.BufferedReader(new java.io.InputStreamReader(process.getInputStream()))) {
            String line;
            while ((line = reader.readLine()) != null) {
                System.out.println("Python STDOUT: " + line);
            }
        }
        
        // 讀取標準錯誤
        try (java.io.BufferedReader reader = new java.io.BufferedReader(new java.io.InputStreamReader(process.getErrorStream()))) {
            String line;
            while ((line = reader.readLine()) != null) {
                System.err.println("Python STDERR: " + line);
            }
        }
    }
}