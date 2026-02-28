# 金融分析小專案

這是一個簡單的 Python 程式，可以幫你自動從網路上抓取過去 5 年的美股指數與總體經濟數據。

## 如何使用

1. 安裝環境套件
   請先確保你的 Python 環境已經準備好。在終端機中執行以下指令來安裝所有需要的套件：
   pip install -r requirements.txt

2. 執行程式抓取資料
   在終端機中輸入以下指令：
   python get_data.py

3. 查看結果
   程式執行完畢後，會自動建立一個 data 資料夾，裡面會產生 us_market_macro_5yrs.csv 檔案。你可以用 Excel 打開它來進行後續分析。
