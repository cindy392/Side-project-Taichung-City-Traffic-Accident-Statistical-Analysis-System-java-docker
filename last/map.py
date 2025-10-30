import pandas as pd
import folium
from folium.plugins import MarkerCluster
import requests
import sys

# 讀取 CSV 檔案
year = str(sys.argv[1])
month = str(sys.argv[2])
text="臺中市政府警察局"+year+"年"+month+"月份交通事故資料"
filename=text+'.csv'
df = pd.read_csv(filename)
# 資料清洗與處理
df["GPS經度"] = pd.to_numeric(df["GPS經度"], errors='coerce')
df["GPS緯度"] = pd.to_numeric(df["GPS緯度"], errors='coerce')

# 建立地圖與設定位置
fmap = folium.Map(location=[24.162065554258085, 120.64685006817835], zoom_start=16)
marker_cluster = MarkerCluster().add_to(fmap)
try:
    # 遍歷 DataFrame
    for index, row in df.iterrows():
        # 提取單個數值
        latitude = row["GPS緯度"]
        longitude = row["GPS經度"]
        print('[',latitude,',',longitude,']')
        information = '發生時間：'+str(row["年"])+'年'+str(row["月"])+'月'+str(row["日"])+'日'+str(row["時"])+'時：'+str(row["分"])+'分'+'<br>'+'死亡：'+str(row["死"])+'<br>'+'受傷：'+str(row["受傷"])
        folium.Marker(location=[longitude,latitude],popup = information).add_to(marker_cluster)
except Exception as e:
    print("失敗")
    print(e)
finally:
    filenamehtml=text+'.html'
    fmap.save(filenamehtml)

