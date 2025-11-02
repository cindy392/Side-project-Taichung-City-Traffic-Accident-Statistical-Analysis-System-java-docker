# FROM openjdk:17-jdk-slim
# WORKDIR /app
# COPY target/*.jar app.jar
# ENTRYPOINT ["java", "-jar", "app.jar"]

# =========================================================
# 階段二：運行程式 (Run Stage)
# =========================================================
# Dockerfile (後端)

# =========================================================
# 階段一：建構 Java 程式 (Build Stage)
# 確保您的專案編譯工具 (如 Maven 或 Gradle) 能夠運行
# 如果您在外面編譯好 JAR，則可以移除此階段，直接跳到運行階段
# 假設您是在外面編譯好，然後把 target/ 資料夾放到 Dockerfile 的同級目錄
# =========================================================
# FROM maven:3.8.7-jdk-17 AS build
# WORKDIR /app
# COPY . .
# RUN mvn clean package -DskipTests

# =========================================================
# 階段二：運行程式 (Run Stage)
# =========================================================
FROM openjdk:17-jdk-slim

# 【新增：安裝 Chrome 瀏覽器和 ChromeDriver】
# 這裡是一個適用於 Alpine Linux (slim 版本的基礎) 的通用安裝步驟，但可能會因基礎映像檔而異
# 由於 openjdk:17-jdk-slim 是基於 Debian/Ubuntu，我們使用以下指令

# 安裝系統層套件：chromium + chromedriver + 依賴庫(search.py需要的套件)
RUN apt-get update && apt-get install -y \
    chromium \
    chromium-driver \
    libglib2.0-0 \
    libnss3 \
    libgconf-2-4 \
    libxi6 \
    libxrender1 \
    libxtst6 \
    libxss1 \
    libxcomposite1 \
    libatk1.0-0 \
    libasound2 \
    fonts-liberation \
    && rm -rf /var/lib/apt/lists/*
# 【新增：設定 Python 腳本執行權限】(search.py需要的套件)
COPY python_scripts /scripts
RUN chmod +x /scripts/*.py  # 確保 Python 腳本可執行
RUN chmod +x /scripts/chromedriver.exe


# 1. 安裝 Python 3 和 pip，這是運行 Python 腳本的先決條件
# 使用 apt-get 安裝必要的套件
RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    rm -rf /var/lib/apt/lists/*

# 2. 設定工作目錄
WORKDIR /app

# 3. 複製 Python 腳本和依賴
# 假設您的 Python 腳本放在主機的 `./python_scripts` 資料夾內
COPY python_scripts /scripts
COPY python_scripts/requirements.txt /scripts/

# 【暫時新增：複製內含 CSV 檔案的 data 資料夾到 /scripts/data】
COPY python_scripts/data /scripts/data

# 4. 安裝 Python 依賴 (folium, pandas 等)
RUN pip3 install --no-cache-dir -r /scripts/requirements.txt

# 5. 複製 Spring Boot JAR 檔案
# 假設您已經將編譯好的 JAR 放在主機的 `./target` 資料夾
COPY target/*.jar app.jar

# 6. (可選但推薦) 創建資料目錄，雖然 Docker Compose 的 volume 會覆蓋它
RUN mkdir -p /data 

# 7. 設定啟動指令
ENTRYPOINT ["java", "-jar", "app.jar"]

# 提醒：在 Spring Boot 3.x 環境中，請確保您的 Java 程式碼已經從 `javax.servlet` 
# 遷移到 `jakarta.servlet`，以避免運行時錯誤。