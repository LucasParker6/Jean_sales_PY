import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime

driver = webdriver.Chrome()
driver.get("https://tcb-bank-sit.webtech888.com/login")
driver.maximize_window()

# 測試時間
today_date = datetime.today().strftime('%Y-%m-%d')
current_time = datetime.now().strftime('%H-%M-%S')
csv_filename = f"Login_Test_Report_{today_date}_{current_time}.csv"

# 角色
roles = {
    "分行經辦": "admin",
    "分行襄理": "Alice123",
    "分行副理": "xx123123",
    "分行經理": "E7777",
    "總行經辦": "jeremyfog",
    "總行副科": "E1111",
    "總行科長": "E3333",
    "總行副理": "E4444",
    "總行協理": "E5555"
}

password = "123"

AF = "//input[@id='exampleInputEmail1']"
PF = "//input[@id='exampleInputPassword1']"
LIB = "//button[contains(text(),'登入')]"
LOB = "//button[contains(text(),'登出')]"

# 用於處理重複的代碼段的函數
def login_and_inquire(account, password, role):
    username_input = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, AF))
    )
    username_input.send_keys(account)
    password_input = driver.find_element(By.XPATH, PF)
    password_input.send_keys(password)
    login_button = driver.find_element(By.XPATH, LIB)
    login_button.click()

    time.sleep(5)

    # 開啟特店管理列表
    list_manage = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//body/ngx-app[1]/ngx-pages[1]/ngx-one-column-layout[1]/nb-layout[1]/div[1]/div[1]/div[1]/nb-sidebar[1]/div[1]/div[1]/nb-menu[1]/ul[1]/li[1]/a[1]/span[1]"))
    )
    list_manage.click()

    # 特店基本資料查詢
    time.sleep(1)
    Basic_information_inquiry = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'特店基本資料查詢')]"))
    )
    Basic_information_inquiry.click()

    # 查詢
    time.sleep(1)
    inquiry_button = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//nb-card-body/div[1]/div[19]/button[1]"))
    )
    inquiry_button.click()

    # 等待 TotalRecords 出現
    time.sleep(1)
    total_records_element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'TotalRecords')]"))
    )
    total_records_text = total_records_element.text

    # 提取 TotalRecords 數字
    total_records_number = total_records_text.split('：')[1]

    # 將結果寫入CSV文件
    with open(csv_filename, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([role, total_records_number])

    # 登出
    time.sleep(1)
    logout_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, LOB))
    )
    logout_button.click()

# 使用帳號和角色進行登入和查詢
for role, account in roles.items():
    login_and_inquire(account, password, role)

# 自動化結束，網頁關閉
time.sleep(3)
driver.quit()
