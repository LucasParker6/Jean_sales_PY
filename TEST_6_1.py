import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime

# 設定兩個 CSV 檔案的檔名
expected_csv_filename = "Login_Test_Report_02.csv"  # 預期的權限文件名
actual_csv_filename = "Login_Test_Report_2024-05-15_09-34-34.csv"  # 實際生成的權限文件名

# 讀取兩個 CSV 檔案的所有行
expected_rows = []
actual_rows = []

# 讀取 expected_csv_filename 的所有行
with open(expected_csv_filename, 'r', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        expected_rows.append(row)

# 讀取 actual_csv_filename 的所有行
with open(actual_csv_filename, 'r', newline='') as actual_csvfile:
    reader = csv.reader(actual_csvfile)
    for row in reader:
        actual_rows.append(row)

# 找出在 expected_csv_filename 中多出的行
additional_rows = []
for row in expected_rows:
    if row not in actual_rows:
        additional_rows.append(row)

# 找出在 actual_csv_filename 中多出的行
missing_rows = []
for row in actual_rows:
    if row not in expected_rows:
        missing_rows.append(row)

# 將比對結果寫入原本的 actual_csv_filename 文件
with open(actual_csv_filename, 'a', newline='') as csvfile:
    writer = csv.writer(csvfile)
    
    if additional_rows:
        writer.writerow([""])
        writer.writerow(["驗證結果"])
        writer.writerow(["缺少的權限:"])
        for row in additional_rows:
            writer.writerow(row)
    else:
        writer.writerow([""])
        writer.writerow(["驗證結果"])
        writer.writerow(["角色權限對應正確"])

    if missing_rows:
        writer.writerow(["多出的權限:"])
        for row in missing_rows:
            writer.writerow(row)
    else:
        writer.writerow(["角色權限對應正確"])