from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options as ChromeOptions # 修正導入名稱
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import requests
import time
import os
import csv
import sys
import pandas as pd
#import Options
import time



# ==========================================================
# 1. Docker 環境變數設定
# ==========================================================
# 在 Docker 環境中，ChromeDriver 應該在 PATH 中或指定絕對路徑
# 許多 Docker 映像檔（例如 selenium/standalone-chrome）已經包含它，
# 或者我們使用 /usr/bin/chromedriver，具體取決於您的後端 Dockerfile
CHROME_DRIVER_PATH = '/usr/bin/chromedriver' 
DATA_DIR = '/data/' # 輸出檔案必須存到 /data/ Volume 裡

# ==========================================================
# 2. WebDriver 設定 (Headless Mode)
# ==========================================================
# 使用 ChromeOptions 
#chrome_options = ChromeOptions()
chrome_options = Options()
chrome_options.binary_location = "/usr/bin/chromium"
'''chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")        # 必須用於 Docker 環境
chrome_options.add_argument("--disable-dev-shm-usage") # 必須用於 Docker 環境

chrome_options.add_argument("--disable-gpu")  # 防止 GPU 問題
chrome_options.add_argument("--remote-debugging-port=9222")  # 避免 DevToolsActivePort 問題
'''
chrome_options.add_argument("--headless=new")      # 或 "--headless" 依版本
chrome_options.add_argument("--no-sandbox")        # 必須
chrome_options.add_argument("--disable-dev-shm-usage")  # 避免 /dev/shm 空間不足
chrome_options.add_argument("--disable-gpu")       # 防止 GPU 問題
chrome_options.add_argument("--remote-debugging-port=9222") # 避免 DevToolsActivePort
chrome_options.add_argument("--disable-software-rasterizer") # 避免 Vulkan/GL 問題
chrome_options.add_argument("--disable-extensions") # 簡化環境
chrome_options.add_argument("--window-size=1920,1080") # 有些網站需要尺寸
chrome_options.add_argument("--disable-infobars")
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument("--disable-translate")
chrome_options.add_argument("--single-process")  
chrome_options.add_argument("--enable-logging")
chrome_options.add_argument("--v=1")
chrome_options.add_argument("--disable-setuid-sandbox")

def run_scraper(year, month):
    try:
        # 嘗試使用指定的驅動路徑啟動 WebDriver
        # 注意：如果您的 Dockerfile 已經將 chromedriver 加入 PATH，可以省略第一個參數
        #driver = webdriver.Chrome(options=chrome_options)

        #chrome_options = webdriver.ChromeOptions()
        #service = Service(ChromeDriverManager().install())
        #service = Service('/usr/bin/chromedriver')
        # chrome_options.add_argument('--headless')  # 暫時先不要 headless
        #driver = webdriver.Chrome(service=service, options=chrome_options)
        driver = webdriver.Chrome(options=chrome_options)
        print("ChromeDriver 啟動成功！")

    except Exception as e:
        # 如果找不到 WebDriver，請確認後端 Dockerfile 已經正確安裝了它
        print(f"Error starting ChromeDriver: {e} error in search.py")
        print(f"ChromeDriver 啟動失敗: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
        return False # 返回失敗狀態



    # ==========================================================
    # 3. 爬蟲主邏輯
    # ==========================================================

    try:
        
        print(f'Starting search for year: {year}, month: {month}')

        text = f"臺中市政府警察局{year}年{month}月份交通事故資料"
        
        # 前往特定網址->政府資料公開平台
        default_url = "https://data.gov.tw/"
        driver.get(default_url)
        print(f"Page title: {driver.title}")

        # 定位並輸入搜尋字串
        element = driver.find_element(By.ID, "searchbar-input")
        element.send_keys(text)

        # 按搜尋鍵
        button = driver.find_element(By.CLASS_NAME, 'searchbar-submit-btn')
        button.click()
        
        time.sleep(3) # 等待結果載入


        try:
            # 等待包含年與月的超連結出現
            link = WebDriverWait(driver, 15).until(
                EC.presence_of_element_located(
                    (By.XPATH, f"//a[contains(text(), '{year}年{month}月份交通事故資料')]")
                )
            )
            print("找到連結：", link.text)
            link.click()
        except Exception as e:
            print("找不到連結，可能是頁面還沒載入或文字不同。")
            print("目前頁面 HTML 前 500 字：")
            print(driver.page_source[:500])

        # 按要找的標題
        link = driver.find_element(By.PARTIAL_LINK_TEXT, year + "年" + month + "月份交通事故資料")
        webname = link.get_attribute('href')
        
        # 進入資料頁面
        driver.get(webname)
        time.sleep(5) # 等待頁面載入下載連結

        # 查詢 CSV 檔的網址
        download_csv = driver.find_element(By.CSS_SELECTOR, 'a[title="CSV下載檔案"]')
        url = download_csv.get_attribute('href')
        print(f'找到 CSV 下載網址: {url}')

        # 下載並寫入檔案到 /data/ Volume
        response = requests.get(url)
        
        if response.status_code == 200:
            # 修正：將檔案寫入到 /data/ 目錄
            filename = os.path.join(DATA_DIR, f"{text}.csv")
            
            with open(filename, 'wb') as f:
                f.write(response.content)
                
            print(f'CSV 檔案下載完成，儲存於: {filename}')
            
        else:
            print(f'無法下載 CSV 檔案。HTTP Status Code: {response.status_code}')
            sys.exit(1) # 下載失敗視為錯誤

    except NoSuchElementException:
        print(f'找不到網頁元素，可能是資料不存在或網頁結構變更: {text}')
        sys.exit(1) # 找不到資料視為錯誤

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1) # 其他錯誤

    finally:
        driver.quit()


if __name__ == "__main__":
    if len(sys.argv) < 3:
                print("Usage: python3 search.py <year> <month>")
                sys.exit(1)

    year = str(sys.argv[1])
    month = str(sys.argv[2])

    if run_scraper(year, month):
        sys.exit(0) # 成功
    else:
        sys.exit(1) # 失敗