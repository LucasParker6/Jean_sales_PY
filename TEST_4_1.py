import csv

# 設定兩個 CSV 檔案的檔名
csv_filename = "Login_Test_Report.csv"  # 請替換為你的 CSV 檔案名稱
other_csv_filename = "Login_Test_Report_2024-05-09_13-50-30.csv"  # 請替換為另一個 CSV 檔案的名稱

# 讀取兩個 CSV 檔案的所有行
current_rows = []
other_rows = []

# 讀取 csv_filename 的所有行
with open(csv_filename, 'r', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        current_rows.append(row)

# 讀取 other_csv_filename 的所有行
with open(other_csv_filename, 'r', newline='') as other_csvfile:
    reader = csv.reader(other_csvfile)
    for row in reader:
        other_rows.append(row)

# 找出在 other_csv_filename 中多出的行
additional_rows = []
for row in other_rows:
    if row not in current_rows:
        additional_rows.append(row)

# 找出在 csv_filename 中多出的行
missing_rows = []
for row in current_rows:
    if row not in other_rows:
        missing_rows.append(row)

# 顯示在 other_csv_filename 中多出的行
if additional_rows:
    print(f"在 {other_csv_filename} 中比 {csv_filename} 多出的權限:")
    for row in additional_rows:
        print(row)
else:
    print("權限對應正確")

# 顯示在 csv_filename 中少了的行
if missing_rows:
    print(f"在 {csv_filename} 中比 {other_csv_filename} 少的權限:")
    for row in missing_rows:
        print(row)
else:
    print("權限對應正確")
