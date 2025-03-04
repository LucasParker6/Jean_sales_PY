import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import random
import re
import os

'''
建案:Auto_02
'''

# 設定銷售日期
target_day = str(datetime.today().day)

driver = webdriver.Chrome()
driver.get("https://devjeansalesadmin.webtech888.com/login")
driver.maximize_window()

#測試時間
today_date = datetime.today().strftime('%Y-%m-%d')
current_time = datetime.now().strftime('%H-%M-%S')

#CSV檔案名稱
directory = "建商報表比對"  # 資料夾名稱
csv_filename = f"{directory}/建商報表比對_{today_date}_{current_time}.csv"
os.makedirs(directory, exist_ok=True)

#登入
username_input = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH,"/html[1]/body[1]/ngx-app[1]/ngx-login[1]/nb-layout[1]/div[1]/div[1]/div[1]/div[1]/div[1]/nb-layout-column[1]/nb-card[1]/nb-card-body[1]/form[1]/div[1]/input[1]"))
)
username_input.send_keys("Auto02")
password_input=driver.find_element(By.XPATH,"/html[1]/body[1]/ngx-app[1]/ngx-login[1]/nb-layout[1]/div[1]/div[1]/div[1]/div[1]/div[1]/nb-layout-column[1]/nb-card[1]/nb-card-body[1]/form[1]/div[2]/input[1]")
password_input.send_keys("123")
Login=driver.find_element(By.XPATH,"//button[contains(text(),'登入')]")
Login.click()

#銷售前日報表確認
time.sleep(5)
報表管理_01= WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH,"//span[contains(text(),'報表管理')]"))
)
報表管理_01.click()
time.sleep(2)
日報表_01= WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH,"//span[contains(text(),'日報表')]"))
)
日報表_01.click()
新增報表_01= WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH,"//nb-card-body/div[1]/div[1]/div[2]/button[2]"))
)
新增報表_01.click()
廣告媒體_01= WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH,"//textarea[@id='cMediaNote']"))
)
廣告媒體_01.send_keys("TEST")
出勤人員_01=driver.find_element(By.XPATH,"//nb-card-body/div[1]/div[1]/div[1]/div[4]/div[1]/ngx-multiple-sales-selector[1]/nb-select[1]/button[1]")
出勤人員_01.click()
選擇出勤人員_01 = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, "//nb-option[contains(text(), 'Auto_02')]"))
)
選擇出勤人員_01.click()
主委_01=driver.find_element(By.XPATH,"//nb-card-body/div[1]/div[1]/div[1]/div[5]/div[1]/input[1]")
主委_01.send_keys("TEST")
專案_01=driver.find_element(By.XPATH,"//nb-card-body/div[1]/div[1]/div[1]/div[6]/div[1]/input[1]")
專案_01.send_keys("TEST")
確定_01=driver.find_element(By.XPATH,"//button[contains(text(),'確定')]")
確定_01.click()
time.sleep(2)
未結帳報表_01 = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, "//tbody/tr[1]/td[7]/button[3]"))
)
未結帳報表_01.click()
結算_01 = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, "//nb-card-header/button[1]"))
)
A建商銷售前戶數=WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, "//nb-card-body/div[@id='printData']/table[1]/tr[3]/td[4]"))
)
A建商銷售前戶數=A建商銷售前戶數.text
B建商銷售前戶數=WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, "//nb-card-body/div[@id='printData']/table[2]/tr[3]/td[4]"))
)
B建商銷售前戶數=B建商銷售前戶數.text
C建商銷售前戶數=WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, "//nb-card-body/div[@id='printData']/table[3]/tr[3]/td[4]"))
)
C建商銷售前戶數=C建商銷售前戶數.text
A建商銷售前車位數=WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, "//nb-card-body/div[@id='printData']/table[1]/tr[3]/td[5]"))
)
A建商銷售前車位數=A建商銷售前車位數.text
B建商銷售前車位數=WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, "//nb-card-body/div[@id='printData']/table[2]/tr[3]/td[5]"))
)
B建商銷售前車位數=B建商銷售前車位數.text
C建商銷售前車位數=WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, "//nb-card-body/div[@id='printData']/table[3]/tr[3]/td[5]"))
)
C建商銷售前車位數=C建商銷售前車位數.text
with open(csv_filename, mode='w', newline='', encoding='utf-8-sig') as file:
    writer = csv.writer(file)
    current_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    writer.writerow(["","A建商","B建商","C建商","測試時間"])
    writer.writerow(["銷售前戶數",A建商銷售前戶數,B建商銷售前戶數,C建商銷售前戶數,current_datetime])
    writer.writerow(["銷售前車位數",A建商銷售前車位數,B建商銷售前車位數,C建商銷售前車位數,current_datetime])

#銷售戶別、車位
time.sleep(3)
銷控管理_01=driver.find_element(By.XPATH,"//span[contains(text(),'銷控管理')]")
銷控管理_01.click()
time.sleep(2)
銷控表_01=driver.find_element(By.XPATH,"//span[contains(text(),'銷控表')]")
銷控表_01.click()
time.sleep(2)

#購買A建商1戶1車位
A建商戶數_01 = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, "//tbody/tr[3]/td[2]"))
)
A建商戶數_01.click()
time.sleep(1)
客資編號放大鏡_01 = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, "//nb-card-body/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/nb-form-field[1]/div[2]"))
)
客資編號放大鏡_01.click()
客資編號輸入客戶姓名_01 = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, "//nb-card-body/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/ngx-crm-customer-search[1]/input[1]"))
)
客資編號輸入客戶姓名_01.send_keys("建商報表比對人員")
time.sleep(2)
客資編號輸入客戶姓名選擇客戶_01 = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, "//nb-option[contains(text(), ' [11434]建商報表比對人員(0911111111) ')]"))
)
time.sleep(2)
客資編號輸入客戶姓名選擇客戶_01.click()
成交價格_01 = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, "//input[@id='cPrice']"))
)
成交價格_01.send_keys("500")
銷控表業務員_01=driver.find_element(By.XPATH,"//nb-card-body/div[1]/div[1]/div[1]/div[2]/div[8]/div[1]/ngx-sales-selector[1]/nb-select[1]/button[1]")
銷控表業務員_01.click()
選擇銷控表業務員_01 = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, "//nb-option[contains(text(), 'Auto_02')]"))
)
選擇銷控表業務員_01.click()
銷售時間_01=driver.find_element(By.XPATH,"//nb-card-body/div[1]/div[1]/div[1]/div[2]/div[11]/div[2]/input[1]")
銷售時間_01.click()

time.sleep(1)
date_elements = driver.find_elements(By.CSS_SELECTOR, "nb-calendar-day-cell")
for date in date_elements:
    if "bounding-month" not in date.get_attribute("class"):
        day_text = date.text.strip()
        if day_text == target_day:
            date.click()
            break
time.sleep(1)

A建商車位_01=driver.find_element(By.XPATH,"//nb-card-body/div[1]/div[1]/div[1]/div[2]/div[9]/label[1]/button[1]")
A建商車位_01.click()
time.sleep(5)
選擇車位_01=driver.find_element(By.XPATH,"//nb-card-body/div[1]/div[1]/div[1]/div[2]/div[10]/div[2]/ngx-park-selector[1]/nb-select[1]/button[1]")
選擇車位_01.click()
選擇車位B1_1 = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, "//nb-option[contains(text(), 'B1-1')]"))
)
選擇車位B1_1.click()
車位價格_01=driver.find_element(By.XPATH,"//nb-card-body/div[1]/div[1]/div[1]/div[2]/div[10]/div[3]/nb-form-field[1]/div[1]/input[1]")
車位價格_01.send_keys("100")
確定銷售_01=driver.find_element(By.XPATH,"//button[contains(text(),'確定')]")
確定銷售_01.click()

#購買B建商1戶1車位
time.sleep(3)
B建商戶數_02 = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, "//tbody/tr[2]/td[2]"))
)
B建商戶數_02.click()
time.sleep(1)
客資編號放大鏡_02 = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, "//nb-card-body/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/nb-form-field[1]/div[2]"))
)
客資編號放大鏡_02.click()
客資編號輸入客戶姓名_02 = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, "//nb-card-body/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/ngx-crm-customer-search[1]/input[1]"))
)
客資編號輸入客戶姓名_02.send_keys("建商報表比對人員")
time.sleep(2)
客資編號輸入客戶姓名選擇客戶_02 = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, "//nb-option[contains(text(), ' [11434]建商報表比對人員(0911111111) ')]"))
)
time.sleep(2)
客資編號輸入客戶姓名選擇客戶_02.click()
成交價格_02 = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, "//input[@id='cPrice']"))
)
成交價格_02.send_keys("500")
銷控表業務員_02=driver.find_element(By.XPATH,"//nb-card-body/div[1]/div[1]/div[1]/div[2]/div[8]/div[1]/ngx-sales-selector[1]/nb-select[1]/button[1]")
銷控表業務員_02.click()
選擇銷控表業務員_02 = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, "//nb-option[contains(text(), 'Auto_02')]"))
)
選擇銷控表業務員_02.click()
銷售時間_02=driver.find_element(By.XPATH,"//nb-card-body/div[1]/div[1]/div[1]/div[2]/div[11]/div[2]/input[1]")
銷售時間_02.click()

time.sleep(1)
date_elements = driver.find_elements(By.CSS_SELECTOR, "nb-calendar-day-cell")
for date in date_elements:
    if "bounding-month" not in date.get_attribute("class"):
        day_text = date.text.strip()
        if day_text == target_day:
            date.click()
            break
time.sleep(1)

B建商車位_02=driver.find_element(By.XPATH,"//nb-card-body/div[1]/div[1]/div[1]/div[2]/div[9]/label[1]/button[1]")
B建商車位_02.click()
time.sleep(5)
選擇車位_02=driver.find_element(By.XPATH,"//nb-card-body/div[1]/div[1]/div[1]/div[2]/div[10]/div[2]/ngx-park-selector[1]/nb-select[1]/button[1]")
選擇車位_02.click()
time.sleep(1)
選擇車位B1_3 = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, "//nb-option[contains(text(), 'B1-3')]"))
)
選擇車位B1_3.click()
車位價格_02=driver.find_element(By.XPATH,"//nb-card-body/div[1]/div[1]/div[1]/div[2]/div[10]/div[3]/nb-form-field[1]/div[1]/input[1]")
車位價格_02.send_keys("100")
確定銷售_02=driver.find_element(By.XPATH,"//button[contains(text(),'確定')]")
確定銷售_02.click()

#購買C建商1戶1車位
time.sleep(3)
C建商戶數_03 = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, "//tbody/tr[1]/td[2]"))
)
C建商戶數_03.click()
time.sleep(1)
客資編號放大鏡_03 = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, "//nb-card-body/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/nb-form-field[1]/div[2]"))
)
客資編號放大鏡_03.click()
客資編號輸入客戶姓名_03 = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, "//nb-card-body/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/ngx-crm-customer-search[1]/input[1]"))
)
客資編號輸入客戶姓名_03.send_keys("建商報表比對人員")
time.sleep(2)
客資編號輸入客戶姓名選擇客戶_03 = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, "//nb-option[contains(text(), ' [11434]建商報表比對人員(0911111111) ')]"))
)
time.sleep(2)
客資編號輸入客戶姓名選擇客戶_03.click()
成交價格_03 = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, "//input[@id='cPrice']"))
)
成交價格_03.send_keys("500")
銷控表業務員_03=driver.find_element(By.XPATH,"//nb-card-body/div[1]/div[1]/div[1]/div[2]/div[8]/div[1]/ngx-sales-selector[1]/nb-select[1]/button[1]")
銷控表業務員_03.click()
選擇銷控表業務員_03 = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, "//nb-option[contains(text(), 'Auto_02')]"))
)
選擇銷控表業務員_03.click()
銷售時間_03=driver.find_element(By.XPATH,"//nb-card-body/div[1]/div[1]/div[1]/div[2]/div[11]/div[2]/input[1]")
銷售時間_03.click()

time.sleep(1)
date_elements = driver.find_elements(By.CSS_SELECTOR, "nb-calendar-day-cell")
for date in date_elements:
    if "bounding-month" not in date.get_attribute("class"):
        day_text = date.text.strip()
        if day_text == target_day:
            date.click()
            break
time.sleep(1)

B建商車位_03=driver.find_element(By.XPATH,"//nb-card-body/div[1]/div[1]/div[1]/div[2]/div[9]/label[1]/button[1]")
B建商車位_03.click()
time.sleep(5)
選擇車位_03=driver.find_element(By.XPATH,"//nb-card-body/div[1]/div[1]/div[1]/div[2]/div[10]/div[2]/ngx-park-selector[1]/nb-select[1]/button[1]")
選擇車位_03.click()
time.sleep(1)
選擇車位B1_5 = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, "//nb-option[contains(text(), 'B1-5')]"))
)
選擇車位B1_5.click()
車位價格_03=driver.find_element(By.XPATH,"//nb-card-body/div[1]/div[1]/div[1]/div[2]/div[10]/div[3]/nb-form-field[1]/div[1]/input[1]")
車位價格_03.send_keys("100")
確定銷售_03=driver.find_element(By.XPATH,"//button[contains(text(),'確定')]")
確定銷售_03.click()

#銷售後日報表確認
time.sleep(3)
日報表_01= WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH,"//span[contains(text(),'日報表')]"))
)
日報表_01.click()
新增報表_01= WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH,"//nb-card-body/div[1]/div[1]/div[2]/button[2]"))
)
新增報表_01.click()
廣告媒體_01= WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH,"//textarea[@id='cMediaNote']"))
)
廣告媒體_01.send_keys("TEST")
出勤人員_01=driver.find_element(By.XPATH,"//nb-card-body/div[1]/div[1]/div[1]/div[4]/div[1]/ngx-multiple-sales-selector[1]/nb-select[1]/button[1]")
出勤人員_01.click()
選擇出勤人員_01 = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, "//nb-option[contains(text(), 'Auto_02')]"))
)
選擇出勤人員_01.click()
主委_01=driver.find_element(By.XPATH,"//nb-card-body/div[1]/div[1]/div[1]/div[5]/div[1]/input[1]")
主委_01.send_keys("TEST")
專案_01=driver.find_element(By.XPATH,"//nb-card-body/div[1]/div[1]/div[1]/div[6]/div[1]/input[1]")
專案_01.send_keys("TEST")
確定_01=driver.find_element(By.XPATH,"//button[contains(text(),'確定')]")
確定_01.click()
time.sleep(2)
未結帳報表_01 = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, "//tbody/tr[1]/td[7]/button[3]"))
)
未結帳報表_01.click()
結算_01 = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, "//nb-card-header/button[1]"))
)
A建商銷售後戶數=WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, "//nb-card-body/div[@id='printData']/table[1]/tr[3]/td[4]"))
)
A建商銷售後戶數=A建商銷售後戶數.text
B建商銷售後戶數=WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, "//nb-card-body/div[@id='printData']/table[2]/tr[3]/td[4]"))
)
B建商銷售後戶數=B建商銷售後戶數.text
C建商銷售後戶數=WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, "//nb-card-body/div[@id='printData']/table[3]/tr[3]/td[4]"))
)
C建商銷售後戶數=C建商銷售後戶數.text
A建商銷售後車位數=WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, "//nb-card-body/div[@id='printData']/table[1]/tr[3]/td[5]"))
)
A建商銷售後車位數=A建商銷售後車位數.text
B建商銷售後車位數=WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, "//nb-card-body/div[@id='printData']/table[2]/tr[3]/td[5]"))
)
B建商銷售後車位數=B建商銷售後車位數.text
C建商銷售後車位數=WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, "//nb-card-body/div[@id='printData']/table[3]/tr[3]/td[5]"))
)
C建商銷售後車位數=C建商銷售後車位數.text

#驗證結果
try:
    assert int(A建商銷售後戶數)==int(A建商銷售前戶數)+1,"A建商戶數未正確增加"
    A建商戶數驗證結果="PASS"
except AssertionError as e:
    A建商戶數驗證結果=f"FAIL:{str(e)}"

try:
    assert int(B建商銷售後戶數)==int(B建商銷售前戶數)+1,"B建商戶數未正確增加"
    B建商戶數驗證結果="PASS"
except AssertionError as e:
    B建商戶數驗證結果=f"FAIL:{str(e)}"

try:
    assert int(C建商銷售後戶數)==int(C建商銷售前戶數) + 1,"C建商戶數未正確增加"
    C建商戶數驗證結果="PASS"
except AssertionError as e:
    C建商戶數驗證結果=f"FAIL:{str(e)}"

try:
    assert int(A建商銷售後車位數)==int(A建商銷售前車位數)+1,"A建商車位數未正確增加"
    A建商車位驗證結果="PASS"
except AssertionError as e:
    A建商車位驗證結果=f"FAIL:{str(e)}"

try:
    assert int(B建商銷售後車位數)==int(B建商銷售前車位數)+1,"B建商車位數未正確增加"
    B建商車位驗證結果="PASS"
except AssertionError as e:
    B建商車位驗證結果=f"FAIL:{str(e)}"

try:
    assert int(C建商銷售後車位數)==int(C建商銷售前車位數)+1, "C建商車位數未正確增加"
    C建商車位驗證結果="PASS"
except AssertionError as e:
    C建商車位驗證結果=f"FAIL:{str(e)}"

current_datetime=datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open(csv_filename, mode='a', newline='', encoding='utf-8-sig') as file:
    writer = csv.writer(file)
    writer.writerow(["","","","",""])
    writer.writerow(["銷售後戶數",A建商銷售後戶數,B建商銷售後戶數,C建商銷售後戶數,current_datetime])
    writer.writerow(["銷售後車位數",A建商銷售後車位數,B建商銷售後車位數,C建商銷售後車位數,current_datetime])
    writer.writerow(["戶數驗證結果",A建商戶數驗證結果,B建商戶數驗證結果,C建商戶數驗證結果,current_datetime])
    writer.writerow(["車位數驗證結果",A建商車位驗證結果,B建商車位驗證結果,C建商車位驗證結果,current_datetime])

#執行退戶退車
time.sleep(3)
退戶銷控表_01=driver.find_element(By.XPATH,"//span[contains(text(),'銷控表')]")
退戶銷控表_01.click()
#退A建商
time.sleep(2)
退戶A1_1_01 = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, "//tbody/tr[3]/td[2]"))
)
退戶A1_1_01.click()
time.sleep(2)
退戶日期_01=WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, "//nb-card-body/div[1]/div[1]/div[1]/div[2]/div[15]/div[2]/input[1]"))
)
退戶日期_01.click()

time.sleep(2)
date_elements = driver.find_elements(By.CSS_SELECTOR, "nb-calendar-day-cell")
for date in date_elements:
    if "bounding-month" not in date.get_attribute("class"):
        day_text = date.text.strip()
        if day_text == target_day:
            date.click()
            break
time.sleep(2)

退戶因素_01=driver.find_element(By.XPATH,"//nb-card-body/div[1]/div[1]/div[1]/div[2]/div[16]/div[1]/ngx-reason-selector[1]/nb-select[1]/button[1]")
退戶因素_01.click()
time.sleep(2)
選擇退戶因素_01 = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, "//nb-option[contains(text(), '單價不認同')]"))
)
選擇退戶因素_01.click()
確定_退戶_01=driver.find_element(By.XPATH,"//button[contains(text(),'確定')]")
確定_退戶_01.click()

#退B建商
time.sleep(3)
退戶A1_2_01 = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, "//tbody/tr[2]/td[2]"))
)
退戶A1_2_01.click()
time.sleep(2)
退戶日期_02=WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, "//nb-card-body/div[1]/div[1]/div[1]/div[2]/div[15]/div[2]/input[1]"))
)
退戶日期_02.click()

time.sleep(2)
date_elements = driver.find_elements(By.CSS_SELECTOR, "nb-calendar-day-cell")
for date in date_elements:
    if "bounding-month" not in date.get_attribute("class"):
        day_text = date.text.strip()
        if day_text == target_day:
            date.click()
            break
time.sleep(2)

退戶因素_02=driver.find_element(By.XPATH,"//nb-card-body/div[1]/div[1]/div[1]/div[2]/div[16]/div[1]/ngx-reason-selector[1]/nb-select[1]/button[1]")
退戶因素_02.click()
time.sleep(2)
選擇退戶因素_02 = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, "//nb-option[contains(text(), '單價不認同')]"))
)
選擇退戶因素_02.click()
確定_退戶_02=driver.find_element(By.XPATH,"//button[contains(text(),'確定')]")
確定_退戶_02.click()

#退C建商
time.sleep(3)
退戶A1_3_01 = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, "//tbody/tr[1]/td[2]"))
)
退戶A1_3_01.click()
time.sleep(2)
退戶日期_03=WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, "//nb-card-body/div[1]/div[1]/div[1]/div[2]/div[15]/div[2]/input[1]"))
)
退戶日期_03.click()

time.sleep(2)
date_elements = driver.find_elements(By.CSS_SELECTOR, "nb-calendar-day-cell")
for date in date_elements:
    if "bounding-month" not in date.get_attribute("class"):
        day_text = date.text.strip()
        if day_text == target_day:
            date.click()
            break
time.sleep(2)

退戶因素_03=driver.find_element(By.XPATH,"//nb-card-body/div[1]/div[1]/div[1]/div[2]/div[16]/div[1]/ngx-reason-selector[1]/nb-select[1]/button[1]")
退戶因素_03.click()
time.sleep(2)
選擇退戶因素_03 = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, "//nb-option[contains(text(), '單價不認同')]"))
)
選擇退戶因素_03.click()
確定_退戶_03=driver.find_element(By.XPATH,"//button[contains(text(),'確定')]")
確定_退戶_03.click()

#退戶後日報表確認
time.sleep(3)
日報表_01= WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH,"//span[contains(text(),'日報表')]"))
)
日報表_01.click()
新增報表_01= WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH,"//nb-card-body/div[1]/div[1]/div[2]/button[2]"))
)
新增報表_01.click()
廣告媒體_01= WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH,"//textarea[@id='cMediaNote']"))
)
廣告媒體_01.send_keys("TEST")
出勤人員_01=driver.find_element(By.XPATH,"//nb-card-body/div[1]/div[1]/div[1]/div[4]/div[1]/ngx-multiple-sales-selector[1]/nb-select[1]/button[1]")
出勤人員_01.click()
選擇出勤人員_01 = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, "//nb-option[contains(text(), 'Auto_02')]"))
)
選擇出勤人員_01.click()
主委_01=driver.find_element(By.XPATH,"//nb-card-body/div[1]/div[1]/div[1]/div[5]/div[1]/input[1]")
主委_01.send_keys("TEST")
專案_01=driver.find_element(By.XPATH,"//nb-card-body/div[1]/div[1]/div[1]/div[6]/div[1]/input[1]")
專案_01.send_keys("TEST")
確定_01=driver.find_element(By.XPATH,"//button[contains(text(),'確定')]")
確定_01.click()
time.sleep(2)
未結帳報表_01 = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, "//tbody/tr[1]/td[7]/button[3]"))
)
未結帳報表_01.click()
結算_01 = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, "//nb-card-header/button[1]"))
)
A建商退戶後戶數=WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, "//nb-card-body/div[@id='printData']/table[1]/tr[3]/td[4]"))
)
A建商退戶後戶數=A建商退戶後戶數.text
B建商退戶後戶數=WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, "//nb-card-body/div[@id='printData']/table[2]/tr[3]/td[4]"))
)
B建商退戶後戶數=B建商退戶後戶數.text
C建商退戶後戶數=WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, "//nb-card-body/div[@id='printData']/table[3]/tr[3]/td[4]"))
)
C建商退戶後戶數=C建商退戶後戶數.text
A建商退戶後車位數=WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, "//nb-card-body/div[@id='printData']/table[1]/tr[3]/td[5]"))
)
A建商退戶後車位數=A建商退戶後車位數.text
B建商退戶後車位數=WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, "//nb-card-body/div[@id='printData']/table[2]/tr[3]/td[5]"))
)
B建商退戶後車位數=B建商退戶後車位數.text
C建商退戶後車位數=WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, "//nb-card-body/div[@id='printData']/table[3]/tr[3]/td[5]"))
)
C建商退戶後車位數=C建商退戶後車位數.text

#驗證結果
try:
    assert int(A建商退戶後戶數)==int(A建商銷售後戶數),"A建商戶數與對退戶前不一致"
    A建商戶數驗證結果="PASS"
except AssertionError as e:
    A建商戶數驗證結果=f"FAIL:{str(e)}"

try:
    assert int(B建商退戶後戶數)==int(B建商銷售後戶數),"B建商戶數與對退戶前不一致"
    B建商戶數驗證結果="PASS"
except AssertionError as e:
    B建商戶數驗證結果=f"FAIL:{str(e)}"

try:
    assert int(C建商退戶後戶數)==int(C建商銷售後戶數),"C建商戶數與對退戶前不一致"
    C建商戶數驗證結果="PASS"
except AssertionError as e:
    C建商戶數驗證結果=f"FAIL:{str(e)}"

try:
    assert int(A建商退戶後車位數)==int(A建商銷售後車位數),"A建商車位數與對退戶前不一致"
    A建商車位驗證結果="PASS"
except AssertionError as e:
    A建商車位驗證結果=f"FAIL:{str(e)}"

try:
    assert int(B建商退戶後車位數)==int(B建商銷售後車位數),"B建商車位數與對退戶前不一致"
    B建商車位驗證結果="PASS"
except AssertionError as e:
    B建商車位驗證結果=f"FAIL:{str(e)}"

try:
    assert int(C建商退戶後車位數)==int(C建商銷售後車位數),"C建商車位數與對退戶前不一致"
    C建商車位驗證結果="PASS"
except AssertionError as e:
    C建商車位驗證結果=f"FAIL:{str(e)}"

current_datetime=datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open(csv_filename, mode='a', newline='', encoding='utf-8-sig') as file:
    writer = csv.writer(file)
    writer.writerow(["","","","",""])
    writer.writerow(["退戶後戶數",A建商退戶後戶數,B建商退戶後戶數,C建商退戶後戶數,current_datetime])
    writer.writerow(["退戶後車位數",A建商退戶後車位數,B建商退戶後車位數,C建商退戶後車位數,current_datetime])
    writer.writerow(["戶數驗證結果",A建商戶數驗證結果,B建商戶數驗證結果,C建商戶數驗證結果,current_datetime])
    writer.writerow(["車位數驗證結果",A建商車位驗證結果,B建商車位驗證結果,C建商車位驗證結果,current_datetime])

#自動化結束，網頁關閉
time.sleep(3)
driver.quit()