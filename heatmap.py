import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 1. 解決 macOS 的畫圖字體顯示問題 (讓圖片能顯示中文)
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS', 'Heiti TC', 'PingFang HK'] 
plt.rcParams['axes.unicode_minus'] = False 

# 2. 讀取剛剛抓好的歷史資料 (將第一欄位設定為日期索引)
df_data = pd.read_csv('data/us_market_macro_5yrs.csv', index_col=0, parse_dates=True)

# 3. 計算「相關係數」矩陣 (數值介於 -1 到 1 之間：越接近 1 代表高度正相關)
df_corr = df_data.corr()

# 4. 設定圖表大小並繪製熱力圖
plt.figure(figsize=(10, 8))
# annot=True 會在格子上顯示數字，cmap 設定好看的顏色風格
sns.heatmap(df_corr, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)

# 5. 加上標題並把熱力圖顯示出來
plt.title('美國股市與總體經濟指標相關性 (過去 5 年)', fontsize=16)
plt.show()