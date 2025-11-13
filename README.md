# 專案名稱：台中市交通事故分析系統  

---
**專案介紹：**  
- 本系統以**Java、JavaScript 與 Python**開發一套全端系統，使用**框架Springboot和React**，並利用**docker**進行部屬。
- 系統提供事故資料的統計分析與可視化功能，用於即時讀取、統計分析與可視化臺中市的交通事故數據。
- 用戶可選擇年份與月份查詢台中市交通事故，並透過地圖呈現事故細節（時間、地點、傷亡數）。
- 比較當月與上月、去年同月的數據，生成事故趨勢圖與地區分佈直方圖，協助用戶快速掌握交通事故發生趨勢。
- 用於即時讀取、統計分析與可視化臺中市的交通事故數據。
  
---
## 核心價值
- 將政府開放的CSV數據轉換為具備地區熱點分析、時間趨勢對比的互動式儀表板，為交通安全決策提供數據依據。  
- 可協助交通管理單位分析高風險地點與時間，支援政策制定與安全改善。

---

## 技術架構

| 類別 | 使用技術 |
|------|-----------|
| 前端 | React / JavaScript |
| 後端 | Spring Boot / Restful API |
| 資料庫 | MySQL |
| 部署 | Docker / GitHub |

## 功能介紹

a. 地圖顯示：可以選擇想查詢的年份與月份，送出後顯示這個時間段的台中市發生交通事故的地點，並且會顯示發生時間、死亡數與受傷數

![image](https://github.com/cindy392/Side-project-Taichung-City-Traffic-Accident-Statistical-Analysis-System/assets/91950203/e46d8d14-713d-4559-af25-b94a0ed50142)

b. 統計分析與數據比較：
   
1.顯示將選擇的時間資料，顯示事件數、死亡數和受傷數  

![image](https://github.com/cindy392/Side-project-Taichung-City-Traffic-Accident-Statistical-Analysis-System/assets/91950203/219bccb2-ff61-4b4c-9bae-0578aa9e9759)
   
2.將選擇的時間資料去跟上月和去年同月的時間資料做比較  
   
![image](https://github.com/cindy392/Side-project-Taichung-City-Traffic-Accident-Statistical-Analysis-System/assets/91950203/3d87680e-0ba3-45ab-b720-6a1f2fc695bc)
   
3.分析2022/04-2023/03 期間資料，並且將數據可視化成統計圖表，其中包含事件數一年內趨勢折線圖、死亡數一年內趨勢折線圖、受傷數一年內趨勢折線圖和事件數地區直方圖  
![image](https://github.com/cindy392/Side-project-Taichung-City-Traffic-Accident-Statistical-Analysis-System/assets/91950203/14efe4ea-2ae8-4145-b208-c9a60d44f577)
   
![image](https://github.com/cindy392/Side-project-Taichung-City-Traffic-Accident-Statistical-Analysis-System/assets/91950203/f504c51f-922f-44aa-ad65-f8b4cc58aea4)
