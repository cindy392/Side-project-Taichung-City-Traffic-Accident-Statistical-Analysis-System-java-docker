import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import json
import seaborn as sns
from matplotlib.font_manager import FontProperties

# 設定中文字型檔案路徑
font_path = 'C:/Users/cindy/OneDrive/Desktop/四下/中文字型/jf-openhuninn-2.0.ttf'  # 替換為您的中文字型檔案路徑
# 設定字型屬性
font_prop = FontProperties(fname=font_path)

# 讀取數據
data11203 = pd.read_csv("臺中市政府警察局112年3月份交通事故資料.csv")
data11202 = pd.read_csv("臺中市政府警察局112年2月份交通事故資料.csv")
data11201 = pd.read_csv("臺中市政府警察局112年1月份交通事故資料.csv")
data11112 = pd.read_csv("臺中市政府警察局111年12月份交通事故資料.csv")
data11111 = pd.read_csv("臺中市政府警察局111年11月份交通事故資料.csv")
data11110 = pd.read_csv("臺中市政府警察局111年10月份交通事故資料.csv")
data11109 = pd.read_csv("臺中市政府警察局111年9月份交通事故資料.csv")
data11108 = pd.read_csv("臺中市政府警察局111年8月份交通事故資料.csv")
data11107 = pd.read_csv("臺中市政府警察局111年7月份交通事故資料.csv")
data11106 = pd.read_csv("臺中市政府警察局111年6月份交通事故資料.csv")
data11105 = pd.read_csv("臺中市政府警察局111年5月份交通事故資料.csv")
data11104 = pd.read_csv("臺中市政府警察局111年4月份交通事故資料.csv")
data11103 = pd.read_csv("臺中市政府警察局111年3月份交通事故資料.csv")
#計算死亡數，受傷數，跟事件數
death11203 = data11203['死'].sum()
hurt11203 = data11203['受傷'].sum()
count11203 = data11203['年'].count()
death11202 = data11202['死'].sum()
hurt11202 = data11202['受傷'].sum()
count11202 = data11202['年'].count()
death11201 = data11201['死'].sum()
hurt11201 = data11201['受傷'].sum()
count11201 = data11201['年'].count()
death11112 = data11112['死'].sum()#111/12
hurt11112 = data11112['受傷'].sum()
count11112 = data11112['年'].count()
death11111 = data11111['死'].sum()
hurt11111 = data11111['受傷'].sum()
count11111 = data11111['年'].count()
death11110 = data11110['死'].sum()
hurt11110 = data11110['受傷'].sum()
count11110 = data11110['年'].count()
death11109 = data11109['死'].sum()
hurt11109 = data11109['受傷'].sum()
count11109 = data11109['年'].count()
death11108 = data11108['死'].sum()
hurt11108 = data11108['受傷'].sum()
count11108 = data11108['年'].count()
death11107 = data11107['死'].sum()
hurt11107 = data11107['受傷'].sum()
count11107 = data11107['年'].count()
death11106 = data11106['死'].sum()
hurt11106 = data11106['受傷'].sum()
count11106 = data11106['年'].count()
death11105 = data11105['死'].sum()
hurt11105 = data11105['受傷'].sum()
count11105 = data11105['年'].count()
death11104 = data11104['死'].sum()
hurt11104 = data11104['受傷'].sum()
count11104 = data11104['年'].count()
death11103 = data11103['死'].sum()
hurt11103 = data11103['受傷'].sum()
count11103 = data11103['年'].count()

data = {
    '事件數': [count11104, count11105, count11106, count11107, count11108, count11109, count11110, count11111, count11112, count11201, count11202, count11203],
    '死亡數': [death11104, death11105, death11106, death11107, death11108, death11109, death11110, death11111, death11112, death11201, death11202, death11203],
    '受傷數': [hurt11104, hurt11105, hurt11106, hurt11107, hurt11108, hurt11109, hurt11110, hurt11111, hurt11112, hurt11201, hurt11202, hurt11203],
    '月份': ['4','5','6','7','8','9','10','11','12','1','2','3']
}

# 建立DataFrame
df = pd.DataFrame(data)



#112年3月與上個月事件數，死亡數，受傷數的差異
differencedeath = death11203-death11202
differencehurt = hurt11203-hurt11202
differencecount = count11203-count11202

#112年3月與去年同個月事件數，死亡數，受傷數的差異
diffyeardeath = death11203-death11103
diffyearhurt = hurt11203-hurt11103
diffyearcount = count11203-count11103

print(death11203)
print(hurt11203)
print(count11203)
print('+',differencedeath)
print('+',differencehurt)
print('+',differencecount)
print(diffyeardeath)
print('+',diffyearhurt)
print('+',diffyearcount)

# 繪製事件數折線圖
plt.plot('月份','事件數', data=df, linestyle='-', marker='o')
# 設定x軸和y軸標籤
plt.xlabel('月份(從2022/04-2023/03)', fontproperties=font_prop)
plt.ylabel('事件數', fontproperties=font_prop)
# 保存圖表為圖片文件
plt.savefig('C:/xampp/htdocs/plot.png')  # 替換為您要保存的圖片文件路徑和文件名稱
# 顯示圖形
#plt.show()
plt.close()

# 繪製死亡數折線圖
plt.plot('月份','死亡數',color='orange', data=df, linestyle='-', marker='o')
# 設定x軸和y軸標籤
plt.xlabel('月份(從2022/04-2023/03)', fontproperties=font_prop)
plt.ylabel('死亡數', fontproperties=font_prop)
# 保存圖表為圖片文件
plt.savefig('C:/xampp/htdocs/plot_d.png')  # 替換為您要保存的圖片文件路徑和文件名稱
# 顯示圖形
#plt.show()
plt.close()

# 繪製受傷數折線圖
plt.plot('月份','受傷數',color='green', data=df, linestyle='-', marker='o')
# 設定x軸和y軸標籤
plt.xlabel('月份(從2022/04-2023/03)', fontproperties=font_prop)
plt.ylabel('受傷數', fontproperties=font_prop)
# 保存圖表為圖片文件
plt.savefig('C:/xampp/htdocs/plot_h.png')  # 替換為您要保存的圖片文件路徑和文件名稱
# 顯示圖形
#plt.show()
plt.close()

# 繪製地區直方圖
plt.figure(figsize=(8, 8))
sns.histplot(x='區',data=data11203,palette="husl", edgecolor="white")
# 將 x 軸選項標題旋轉為垂直方向
plt.xticks(rotation=90, fontproperties=font_prop)  
# 設定x軸和y軸標籤
plt.xlabel('地區', fontproperties=font_prop)
# 保存圖表為圖片文件
plt.savefig('C:/xampp/htdocs/plot_place.png', dpi=100)  # 替換為您要保存的圖片文件路徑和文件名稱
# 顯示圖形
#plt.show()
plt.close()