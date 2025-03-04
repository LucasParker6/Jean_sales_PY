import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://tcb-bank-sit.webtech888.com/login")
driver.maximize_window()

#測試時間
today_date = datetime.today().strftime('%Y-%m-%d')
current_time = datetime.now().strftime('%H-%M-%S')
csv_filename=f"Login_Test_Report_{today_date}_{current_time}.csv"

#角色
B1_1=("分行經辦")
B2_1=("分行襄理")
B3_1=("分行副理")
B4_1=("分行經理")

H1_1=("總行經辦")
H2_1=("總行副科")
H3_1=("總行科長")
H4_1=("總行副理")
H5_1=("總行協理")

#帳號、密碼
B1=("admin")
B2=("Alice123")
B3=("xx123123")
B4=("E7777")

H1=("jeremyfog")
H2=("E1111")
H3=("E3333")
H4=("E4444")
H5=("E5555")

P1=("123")

AF=("//input[@id='exampleInputEmail1']")
PF=("//input[@id='exampleInputPassword1']")
LIB=("//button[contains(text(),'登入')]")
LOB=("//button[contains(text(),'登出')]")

#B1開始
username_input_1 = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, AF))
)
username_input_1.send_keys(B1)
password_input_1=driver.find_element(By.XPATH,PF)
password_input_1.send_keys(P1)
Login=driver.find_element(By.XPATH,LIB)
Login.click()

time.sleep(3)
#開啟特店管理列表
list_manage=WebDriverWait(driver,20).until(
    EC.presence_of_element_located((By.XPATH,"//body/ngx-app[1]/ngx-pages[1]/ngx-one-column-layout[1]/nb-layout[1]/div[1]/div[1]/div[1]/nb-sidebar[1]/div[1]/div[1]/nb-menu[1]/ul[1]/li[1]/a[1]/span[1]"))
)
list_manage.click()
#特店基本資料查詢
time.sleep(1)
Basic_information_inquiry=WebDriverWait(driver,20).until(
    EC.presence_of_element_located((By.XPATH,"//span[contains(text(),'特店基本資料查詢')]"))
)
Basic_information_inquiry.click()

#查詢
inquiry_button=WebDriverWait(driver,20).until(
    EC.presence_of_element_located((By.XPATH,"//nb-card-body/div[1]/div[19]/button[1]"))
)
inquiry_button.click()

# 等待 TotalRecords 出現
total_records_element = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'TotalRecords')]"))
)
total_records_text = total_records_element.text
# 提取 TotalRecords 數字
total_records_number = total_records_text.split('：')[1]
with open(csv_filename, 'a', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow([B1_1, total_records_number])

#登出
time.sleep(1)
logout_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, LOB))
)
logout_button.click()

#B2開始
username_input_1 = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, AF))
)
username_input_1.send_keys(B2)
password_input_1=driver.find_element(By.XPATH,PF)
password_input_1.send_keys(P1)
Login=driver.find_element(By.XPATH,LIB)
Login.click()

time.sleep(3)
#開啟特店管理列表
list_manage=WebDriverWait(driver,20).until(
    EC.presence_of_element_located((By.XPATH,"//body/ngx-app[1]/ngx-pages[1]/ngx-one-column-layout[1]/nb-layout[1]/div[1]/div[1]/div[1]/nb-sidebar[1]/div[1]/div[1]/nb-menu[1]/ul[1]/li[1]/a[1]/span[1]"))
)
list_manage.click()
#特店基本資料查詢
time.sleep(1)
Basic_information_inquiry=WebDriverWait(driver,20).until(
    EC.presence_of_element_located((By.XPATH,"//span[contains(text(),'特店基本資料查詢')]"))
)
Basic_information_inquiry.click()

#查詢
inquiry_button=WebDriverWait(driver,20).until(
    EC.presence_of_element_located((By.XPATH,"//nb-card-body/div[1]/div[19]/button[1]"))
)
inquiry_button.click()

# 等待 TotalRecords 出現
total_records_element = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'TotalRecords')]"))
)
total_records_text = total_records_element.text
# 提取 TotalRecords 數字
total_records_number = total_records_text.split('：')[1]
with open(csv_filename, 'a', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow([B2_1, total_records_number])

#登出
time.sleep(1)
logout_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, LOB))
)
logout_button.click()

#H1開始
username_input_1 = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, AF))
)
username_input_1.send_keys(H1)
password_input_1=driver.find_element(By.XPATH,PF)
password_input_1.send_keys(P1)
Login=driver.find_element(By.XPATH,LIB)
Login.click()

time.sleep(3)
#開啟特店管理列表
list_manage=WebDriverWait(driver,20).until(
    EC.presence_of_element_located((By.XPATH,"//body/ngx-app[1]/ngx-pages[1]/ngx-one-column-layout[1]/nb-layout[1]/div[1]/div[1]/div[1]/nb-sidebar[1]/div[1]/div[1]/nb-menu[1]/ul[1]/li[2]/a[1]/span[1]"))
)
list_manage.click()
#特店基本資料查詢
time.sleep(1)
Basic_information_inquiry=WebDriverWait(driver,20).until(
    EC.presence_of_element_located((By.XPATH,"//span[contains(text(),'特店基本資料查詢')]"))
)
Basic_information_inquiry.click()

#查詢
inquiry_button=WebDriverWait(driver,20).until(
    EC.presence_of_element_located((By.XPATH,"//nb-card-body/div[1]/div[19]/button[1]"))
)
inquiry_button.click()

# 等待 TotalRecords 出現
total_records_element = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'TotalRecords')]"))
)
total_records_text = total_records_element.text
# 提取 TotalRecords 數字
total_records_number = total_records_text.split('：')[1]
with open(csv_filename, 'a', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow([H1_1, total_records_number])



#自動化結束，網頁關閉
time.sleep(3)
driver.quit()