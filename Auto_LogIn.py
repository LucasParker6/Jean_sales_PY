#角色:分行經辦、分行襄理、分行副理、分行經理/協理、總行經辦、總行副科、總行科長、總行副理、總行協理
#情境:檢查登入後角色權限是否正確，並將權限、比對結果寫入CSV

import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import os

# 路徑
expected_csv_filename = os.path.join(os.getcwd(), "Login_Test_Report_02.csv")

driver = webdriver.Chrome()
driver.get("http://192.168.0.131:8788/login")
driver.maximize_window()

# 測試時間
today_date = datetime.today().strftime('%Y-%m-%d')
current_time = datetime.now().strftime('%H-%M-%S')
csv_filename = f"Login_Test_Report_{today_date}_{current_time}.csv"

# 角色
B1_1 = ("分行經辦")
B2_1 = ("分行襄理")
B3_1 = ("分行副理")
B4_1 = ("分行經理")

H1_1 = ("總行經辦")
H2_1 = ("總行副科")
H3_1 = ("總行科長")
H4_1 = ("總行副理")
H5_1 = ("總行協理")

# 帳號、密碼
B1 = ("admin")
B2 = ("Alice123")
B3 = ("xx123123")
B4 = ("E7777")

H1 = ("jeremyfog")
H2 = ("E1111")
H3 = ("E3333")
H4 = ("E4444")
H5 = ("E5555")

P1 = ("123")

AF = ("//input[@id='exampleInputEmail1']")
PF = ("//input[@id='exampleInputPassword1']")
LIB = ("//button[contains(text(),'登入')]")
LOB = ("//button[contains(text(),'登出')]")

# 用於處理重複的代碼段
def login_and_collect_titles(account, password, role):
    username_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, AF))
    )
    username_input.send_keys(account)
    password_input = driver.find_element(By.XPATH, PF)
    password_input.send_keys(password)
    login_button = driver.find_element(By.XPATH, LIB)
    login_button.click()

    time.sleep(5)

    # 找到所有class為menu-items的元素
    menu_items = driver.find_elements(By.CLASS_NAME, "menu-items")

    # 初始化列表來存儲標題文本
    titles = []

    # 迭代所有menu-items元素
    for menu_item in menu_items:
        # 找到此元素下所有href="#"的子元素
        href_elements = menu_item.find_elements(By.XPATH, ".//a[@href='#']")
        for href_element in href_elements:
            # 檢查是否有title屬性
            if "title" in href_element.get_attribute("outerHTML"):
                # 檢查元素是否可見
                if href_element.is_displayed():
                    # 獲取title屬性的文本
                    title_text = href_element.get_attribute("title")
                    # 將文本添加到列表中
                    titles.append(title_text)

    # 寫入CSV文件
    with open(csv_filename, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for title in titles:
            writer.writerow([role, title])  # 將角色和 title 作為列表寫入CSV的每一行

    # 登出
    time.sleep(1)
    logout_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, LOB))
    )
    logout_button.click()

# 使用帳號和角色進行登入和標題收集
login_and_collect_titles(B1, P1, B1_1)
login_and_collect_titles(B2, P1, B2_1)
login_and_collect_titles(B3, P1, B3_1)
login_and_collect_titles(B4, P1, B4_1)
login_and_collect_titles(H1, P1, H1_1)
login_and_collect_titles(H2, P1, H2_1)
login_and_collect_titles(H3, P1, H3_1)
login_and_collect_titles(H4, P1, H4_1)
login_and_collect_titles(H5, P1, H5_1)

# 自動化結束，網頁關閉
time.sleep(2)
driver.quit()

# 設定兩個 CSV 檔案的檔名
expected_csv_filename = "Login_Test_Report_02.csv"  # 預期的權限文件名
actual_csv_filename = csv_filename  # 實際生成的權限文件名

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