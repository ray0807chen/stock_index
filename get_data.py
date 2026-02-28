import yfinance as yf
import pandas as pd
import pandas_datareader.data as web
import datetime

import os

# 1. 確保儲存資料的資料夾存在
os.makedirs('data', exist_ok=True)

# 2. 設定資料抓取的時間範圍 (過去 5 年)
end_date = datetime.datetime.now()
start_date = end_date - datetime.timedelta(days=5*365)

# 3. 抓取美股每日指數資料 (使用 yfinance)
# 定義欲抓取的指數與易讀的名稱
stock_index = {
    '^GSPC': 'S&P_500',      # 標普 500 指數 (美股大盤)
    '^IXIC': 'NASDAQ',       # 納斯達克指數 (科技股)
    '^VIX': 'VIX',           # 恐慌指數 (市場波動度)
    '^TNX': 'US_10Y_Bond'    # 10年期美債殖利率 (無風險利率)
}

print("正在下載每日股市資料...")
df_stocks = yf.download(list(stock_index.keys()), start=start_date, end=end_date)['Close']
df_stocks.rename(columns=stock_index, inplace=True)

# 4. 抓取美國總體經濟月資料 (使用 FRED 資料庫)
# UNRATE: 失業率, CPIAUCSL: CPI 消費者物價指數
print("正在下載每月總經資料...")
df_cpi = web.DataReader(['UNRATE', 'CPIAUCSL'], 'fred', start_date, end_date)
df_cpi.rename(columns={'UNRATE': 'Unemployment_Rate', 'CPIAUCSL': 'CPI'}, inplace=True)

# 5. 資料合併與對齊
# 將「月資料」對齊到「日資料」的時間軸上 (outer join)
df_combined = df_stocks.join(df_cpi, how='outer')
 
# 向前填補 (ffill)：在下一次公佈總經數據前，市場均假定數據維持上次公佈的水準
df_combined = df_combined.ffill().dropna()

# 6. 匯出成 CSV 檔案，存入專屬的 data 資料夾
filename = 'data/us_market_macro_5yrs.csv'
df_combined.to_csv(filename)
print(f"處理完畢！成功儲存至 {filename}")
