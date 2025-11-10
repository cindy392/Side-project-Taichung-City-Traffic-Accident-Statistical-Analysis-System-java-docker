import pandas as pd
import folium
from folium.plugins import MarkerCluster
import requests
import sys
import os

# 假設 CSV 檔案在 /data/ 目錄下
# DATA_DIR = "/data/"
#DATA_DIR = r"C:\Users\cindy\OneDrive\Desktop\專案\台中市交通事故分析系統\backend\traffic-api\python_scripts\data"
# 相對路徑設定 (相對於 search.py)
DATA_DIR = os.path.join(os.path.dirname(__file__), "data")


# 讀取 CSV 檔案
year = str(sys.argv[1])
month = str(sys.argv[2])
#text="臺中市政府警察局"+year+"年"+month+"月份交通事故資料"
#filename=text+'.csv'
#filename = os.path.join(DATA_DIR, text + '.csv')
filename = os.path.join(DATA_DIR, f"{year}{month}.csv")
df = pd.read_csv(filename)
# 資料清洗與處理
df["GPS座標X"] = pd.to_numeric(df["GPS座標X"], errors='coerce')# 後來有改過名稱 原為GPS經度
df["GPS座標Y"] = pd.to_numeric(df["GPS座標Y"], errors='coerce')# 後來有改過名稱 原為GPS緯度

# 建立地圖與設定位置
fmap = folium.Map(location=[24.162065554258085, 120.64685006817835], zoom_start=16)
marker_cluster = MarkerCluster().add_to(fmap)
try:
    # 遍歷 DataFrame
    for index, row in df.iterrows():
        # 提取單個數值
        latitude = row["GPS座標Y"] # 後來有改過名稱 原為GPS緯度
        longitude = row["GPS座標X"] # 後來有改過名稱 原為GPS經度
        print('[',longitude,',',latitude,']')
        # 後來有改過名稱 原為受傷 死
        information = '發生時間：'+str(row["年"])+'年'+str(row["月"])+'月'+str(row["日"])+'日'+str(row["時"])+'時：'+str(row["分"])+'分'+'<br>'+'死亡：'+str(row["死亡數量"])+'<br>'+'受傷：'+str(row["受傷數量"])
        folium.Marker(location=[latitude, longitude],popup = information).add_to(marker_cluster)
except Exception as e:
    print("失敗")
    print(e)
finally:
    # 修正：構造 HTML 檔案的絕對路徑
    #filenamehtml = os.path.join(DATA_DIR, text + '.html') 
    filenamehtml = os.path.join(DATA_DIR, f"{year}{month}.html") 
    fmap.save(filenamehtml)
    print(f"HTML map saved successfully to: {filenamehtml}") # 新增輸出確認

