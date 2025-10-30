FROM node:20-alpine AS builder

# Set the working directory
WORKDIR /app

# Copy package.json and package-lock.json
# 有改過路徑，要找到package*.json在哪個資料夾
COPY /package*.json ./

# Install dependencies
RUN npm install

# 2. 複製必要的 public/index.html (獨立複製)
# 確保 public 資料夾的內容被複製到容器內的 /app/public
COPY react-app/public/ ./public

# 複製 react-app 的全部程式碼
COPY react-app/ ./

# Copy the rest of your application's source code
COPY . .

# 建置前端（會產生 /build 資料夾）
RUN npm run build

# 【調試指令 1：列出建置結果】
RUN ls -la /app/build 

# 【調試指令 2：確認 index.html 存在】
RUN cat /app/build/index.html

# ----------------------------------------------------
# 階段二：運行 (Run Stage) - 負責提供靜態檔案 (Nginx)
# ----------------------------------------------------
FROM nginx:stable-alpine

# 1. 移除 Nginx 預設的配置
RUN rm /etc/nginx/conf.d/default.conf

# 2. 複製自訂的 Nginx 配置檔案 (用於代理 API 請求到 Spring Boot)
# 假設您的 Nginx 設定檔在主機的 ./frontend/nginx.conf
# 這裡的路徑需要根據您實際的檔案位置進行調整
COPY nginx.conf /etc/nginx/conf.d/default.conf

# 3. 複製建構好的 React 靜態檔案
# 從 'builder' 階段的 /app/build 複製到 Nginx 的預設網站根目錄
COPY --from=builder /app/build /usr/share/nginx/html

# Expose the port the app runs on
EXPOSE 80

# Start the application
CMD ["nginx", "-g", "daemon off;"]


#官方帳、版本
#WORKDIR 指定工作路徑
#COPY 複製所有命令到鏡像image
#RUN 在創建鏡像image時執行任意shell命令 #鏡像
#CMD 指定當docker容器運行起來後要執行的命令 #容器
#--host 0.0.0.0 允許外部瀏覽器存取容器內的 Vite dev server