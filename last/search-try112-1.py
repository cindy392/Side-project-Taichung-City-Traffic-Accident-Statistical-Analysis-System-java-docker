from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
import requests
import time
import os
import urllib,csv
import sys
import pandas as pd
#import Options
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# 設定 Chrome 選項
chrome_options = Options()
chrome_options.add_argument("--headless")  # 若需要背景執行
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# 由 webdriver-manager 自動下載對應版本的 chromedriver
service = Service(ChromeDriverManager().install())

# 啟動 driver
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("https://data.gov.tw/")
print(driver.title)

# +driver = webdriver.Chrome(,options=chrome_options)可以消除爬蟲開啟視窗的過程
'''chrome_options = Options()
chrome_options.add_argument("--headless")
# 透過Browser Driver 開啟 Chrome
driver = webdriver.Chrome('chromedriver.exe',options=chrome_options)
#driver = webdriver.Chrome('C:/Users/cindy/OneDrive/Desktop/四下/python/期末報告/chromedriver.exe')
# 前往特定網址->政府資料公開平台
default_url = "https://data.gov.tw/"
driver.get(default_url)
print(driver.title)'''

# 定位搜尋框
element = driver.find_element(By.ID, "searchbar-input")
# 傳入字串
year = str(112)
month = str(3)
print('year:',year,month)
text="臺中市政府警察局"+year+"年"+month+"月份交通事故資料"
print(text)
element.send_keys(text)

#按搜尋鍵
button = driver.find_element(By.CLASS_NAME,'searchbar-submit-btn')
button.click()

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
    print("❌ 找不到連結，可能是頁面還沒載入或文字不同。")
    print("目前頁面 HTML 前 500 字：")
    print(driver.page_source[:500])

#按要找的標題
link = driver.find_element(By.PARTIAL_LINK_TEXT, year + "年" + month + "月份交通事故資料")
webname = link.get_attribute('href')

time.sleep(5)

# 獲取當前頁面的網址
current_url = webname
print('當前頁面網址:', current_url)
default_url = current_url
driver.get(default_url)

#查詢csv檔的網址
try:
    download_csv = driver.find_element(By.CSS_SELECTOR, 'a[title="CSV下載檔案"]')
    print(download_csv.tag_name)
    print(download_csv.get_attribute('href'))
    url=download_csv.get_attribute('href')
    webpage = urllib.request.urlopen(url)  #開啟網頁
    data = csv.reader(webpage.read().decode('utf-8').splitlines()) #讀取資料到data陣列中
    print(data)
    # 用網址下載 CSV 檔案
    response = requests.get(url)
    # 檢查 HTTP 回應狀態碼
    if response.status_code == 200:
        filename=text+'.csv'
        # 將檔案寫入到本機
        with open(filename, 'wb') as f:
            f.write(response.content)
        print('CSV 檔案下載完成')
    else:
        print('無法下載 CSV 檔案')
except NoSuchElementException:
    print('無法定位')

driver.quit()

