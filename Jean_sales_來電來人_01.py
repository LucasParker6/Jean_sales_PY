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

driver = webdriver.Chrome()
driver.get("https://devjeansalesadmin.webtech888.com/login")
driver.maximize_window()

# 設定日期
target_day = str(datetime.today().day)

#隨機手機號碼
def generate_tw_mobile():
    prefix = random.choice([
        "0910", "0911", "0912", "0913", "0914", "0915", "0916", "0917", "0918", "0919",
        "0920", "0921", "0922", "0923", "0924", "0925", "0926", "0927", "0928", "0929",
        "0930", "0931", "0932", "0933", "0934", "0935", "0936", "0937", "0938", "0939",
        "0952", "0953", "0954", "0955", "0956", "0958", "0959",
        "0960", "0961", "0963", "0965", "0966", "0967", "0968", "0970", "0971", "0972",
        "0973", "0974", "0975", "0976", "0977", "0978", "0979", "0980", "0981", "0982",
        "0983", "0984", "0985", "0986", "0987", "0988", "0989", "0990", "0991", "0992",
        "0993", "0994", "0995", "0996", "0997", "0998", "0999"
    ])
    suffix = random.randint(100000, 999999)
    #return f"{prefix}{suffix//1000}{suffix%1000}"
    return f"{prefix}{suffix:06d}"
random_phone_number_01=generate_tw_mobile()
random_phone_number_02=generate_tw_mobile()

#提取數字
def extract_total_count(driver, xpath):
    element = driver.find_element(By.XPATH, xpath)
    text = element.text.strip()
    if not text:
        return None
    match = re.search(r'\d+', text)
    return int(match.group()) if match else None

#測試時間
today_date = datetime.today().strftime('%Y-%m-%d')
current_time = datetime.now().strftime('%H-%M-%S')

#CSV檔案名稱
directory = "來電來人總筆數比對"  # 資料夾名稱
csv_filename = f"{directory}/來人總筆數比對_{today_date}_{current_time}.csv"
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

#新增來電
time.sleep(3)
每日來電管理_first=WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH,"//body/ngx-app[1]/ngx-pages[1]/ngx-one-column-layout[1]/nb-layout[1]/div[1]/div[1]/div[1]/nb-sidebar[1]/div[1]/div[1]/nb-menu[1]/ul[1]/li[2]/a[1]/span[1]"))
)
每日來電管理_first.click()
time.sleep(3)
每日來電管理_second=WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH,"//body/ngx-app[1]/ngx-pages[1]/ngx-one-column-layout[1]/nb-layout[1]/div[1]/div[1]/div[1]/nb-sidebar[1]/div[1]/div[1]/nb-menu[1]/ul[1]/li[2]/ul[1]/li[1]/a[1]/span[1]"))
)
每日來電管理_second.click()
time.sleep(3)
新增_01=WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH,"//nb-card-body/div[1]/div[2]/div[1]/button[6]/i[1]"))
)
新增_01.click()
客戶姓名_01=WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH,"//nb-card-body/div[1]/div[1]/div[1]/div[3]/div[1]/input[1]"))
)
客戶姓名_01.send_keys("TEST123")
手機號碼_01=driver.find_element(By.XPATH,"//input[@id='cMobile']")
手機號碼_01.send_keys(random_phone_number_01)
市話_01=driver.find_element(By.XPATH,"//input[@id='cPhone']")
市話_01.send_keys("0223456789")
確定_01=driver.find_element(By.XPATH,"//button[contains(text(),'確定')]")
確定_01.click()
time.sleep(3)
新增_02=WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH,"//nb-card-body/div[1]/div[2]/div[1]/button[6]/i[1]"))
)
新增_02.click()
客戶姓名_02=WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH,"//nb-card-body/div[1]/div[1]/div[1]/div[3]/div[1]/input[1]"))
)
客戶姓名_02.send_keys("TEST123")
手機號碼_02=driver.find_element(By.XPATH,"//input[@id='cMobile']")
手機號碼_02.send_keys(random_phone_number_02)
市話_02=driver.find_element(By.XPATH,"//input[@id='cPhone']")
市話_02.send_keys("0223456789")
確定_02=driver.find_element(By.XPATH,"//button[contains(text(),'確定')]")
確定_02.click()

#提取每日來電管理頁面來電總比數
time.sleep(3)
來電總比數_01 = extract_total_count(driver, "//div[contains(text(),'總筆數：')]")

#提取日報表頁面來電總比數
time.sleep(3)
報表管理_01= WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH,"//span[contains(text(),'報表管理')]"))
)
報表管理_01.click()
time.sleep(2)
日報表_01= WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH,"//span[contains(text(),'日報表')]"))
)
日報表_01.click()
time.sleep(2)
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
time.sleep(3)
日報總比數_01=extract_total_count(driver, "//nb-card-body/div[@id='printData']/div[1]/div[4]/table[1]/tr[1]/td[2]")

測試結果 = "通過" if 來電總比數_01 == 日報總比數_01 else "失敗"
with open(csv_filename, mode='w', newline='', encoding='utf-8-sig') as file:
    writer = csv.writer(file)
    current_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    writer.writerow(["測試項目", "總比數", "日報總比數", "測試結果", "測試時間"])
    writer.writerow(["來電總比數", 來電總比數_01, 日報總比數_01, 測試結果, current_datetime])

#新增來人
賞屋管理_first=driver.find_element(By.XPATH,"//span[contains(text(),'賞屋(客戶資料)管理')]")
賞屋管理_first.click()
time.sleep(3)
賞屋管理_second=driver.find_element(By.XPATH,"//span[contains(text(),'賞屋管理')]")
賞屋管理_second.click()
time.sleep(3)
新增_02=driver.find_element(By.XPATH,"//nb-card-body/div[1]/div[2]/div[1]/button[6]")
新增_02.click()
time.sleep(3)
賞屋日期_02=driver.find_element(By.XPATH,"//nb-card-body/div[@id='dataToExport']/div[1]/div[1]/div[2]/div[1]/input[1]")
賞屋日期_02.click()

# 找到所有日期元素
time.sleep(1)
date_elements = driver.find_elements(By.CSS_SELECTOR, "nb-calendar-day-cell")
for date in date_elements:
    # 過濾掉其他月份
    if "bounding-month" not in date.get_attribute("class"):
        day_text = date.text.strip()
        if day_text == target_day:  # 用變數代替硬編碼
            date.click()
            break
time.sleep(1)

客戶姓名_03=driver.find_element(By.XPATH,"//nb-card-body/div[@id='dataToExport']/div[1]/div[1]/div[3]/div[1]/input[1]")
客戶姓名_03.send_keys("TEST123")
手機號碼_03=driver.find_element(By.XPATH,"//nb-card-body/div[@id='dataToExport']/div[1]/div[1]/div[6]/div[1]/input[1]")
手機號碼_03.send_keys(random_phone_number_01)
市話_03=driver.find_element(By.XPATH,"//nb-card-body/div[@id='dataToExport']/div[1]/div[1]/div[5]/div[1]/input[1]")
市話_03.send_keys("0223456789")
資料確認_03=driver.find_element(By.XPATH,"//nb-card-body/div[@id='dataToExport']/div[1]/div[1]/div[9]/div[1]/nb-select[1]/button[1]")
資料確認_03.click()
time.sleep(1)
資料確認選擇是_03=driver.find_element(By.XPATH,"//nb-option[contains(text(),'是')]")
資料確認選擇是_03.click()
time.sleep(1)
業務員_03=driver.find_element(By.XPATH,"//nb-card-body/div[@id='dataToExport']/div[1]/div[1]/div[13]/div[1]/ngx-sales-selector[1]/nb-select[1]/button[1]")
業務員_03.click()
time.sleep(1)
選擇業務員_03=driver.find_element(By.XPATH,"//nb-option[contains(text(),'Auto_02')]")
選擇業務員_03.click()
time.sleep(1)
第一次來訪是否購買_03=driver.find_element(By.XPATH,"//nb-card-body/div[4]/div[1]/nb-select[1]/button[1]")
第一次來訪是否購買_03.click()
time.sleep(1)
第一次來訪是否購買選擇已購_03=driver.find_element(By.XPATH,"//nb-option[contains(text(),'已購')]")
第一次來訪是否購買選擇已購_03.click()
time.sleep(1)
確定_03=driver.find_element(By.XPATH,"//button[contains(text(),'確定')]")
確定_03.click()
time.sleep(2)
新增_04=driver.find_element(By.XPATH,"//nb-card-body/div[1]/div[2]/div[1]/button[6]")
新增_04.click()
time.sleep(3)
賞屋日期_03=driver.find_element(By.XPATH,"//nb-card-body/div[@id='dataToExport']/div[1]/div[1]/div[2]/div[1]/input[1]")
賞屋日期_03.click()
time.sleep(1)

# 找到所有日期元素
date_elements = driver.find_elements(By.CSS_SELECTOR, "nb-calendar-day-cell")
for date in date_elements:
    # 過濾掉其他月份
    if "bounding-month" not in date.get_attribute("class"):
        day_text = date.text.strip()
        if day_text == target_day:  # 用變數代替硬編碼
            date.click()
            break
time.sleep(1)
客戶姓名_04=driver.find_element(By.XPATH,"//nb-card-body/div[@id='dataToExport']/div[1]/div[1]/div[3]/div[1]/input[1]")
客戶姓名_04.send_keys("TEST123")
手機號碼_04=driver.find_element(By.XPATH,"//nb-card-body/div[@id='dataToExport']/div[1]/div[1]/div[6]/div[1]/input[1]")
手機號碼_04.send_keys(random_phone_number_02)
市話_04=driver.find_element(By.XPATH,"//nb-card-body/div[@id='dataToExport']/div[1]/div[1]/div[5]/div[1]/input[1]")
市話_04.send_keys("0223456789")
資料確認_04=driver.find_element(By.XPATH,"//nb-card-body/div[@id='dataToExport']/div[1]/div[1]/div[9]/div[1]/nb-select[1]/button[1]")
資料確認_04.click()
time.sleep(1)
資料確認選擇是_04=driver.find_element(By.XPATH,"//nb-option[contains(text(),'是')]")
資料確認選擇是_04.click()
time.sleep(1)
業務員_04=driver.find_element(By.XPATH,"//nb-card-body/div[@id='dataToExport']/div[1]/div[1]/div[13]/div[1]/ngx-sales-selector[1]/nb-select[1]/button[1]")
業務員_04.click()
time.sleep(1)
選擇業務員_04=driver.find_element(By.XPATH,"//nb-option[contains(text(),'Auto_02')]")
選擇業務員_04.click()
time.sleep(1)
第一次來訪是否購買_04=driver.find_element(By.XPATH,"//nb-card-body/div[4]/div[1]/nb-select[1]/button[1]")
第一次來訪是否購買_04.click()
time.sleep(1)
第一次來訪是否購買選擇已購_04=driver.find_element(By.XPATH,"//nb-option[contains(text(),'已購')]")
第一次來訪是否購買選擇已購_04.click()
time.sleep(1)
確定_04=driver.find_element(By.XPATH,"//button[contains(text(),'確定')]")
確定_04.click()

#提取賞屋管理頁面來人筆數
time.sleep(3)
來人總比數_01 = extract_total_count(driver, "//div[contains(text(),'總筆數：')]")

#提取日報表頁面來人筆數筆數
time.sleep(3)
日報表_02= WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH,"//span[contains(text(),'日報表')]"))
)
日報表_02.click()
time.sleep(2)
新增報表_02= WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH,"//nb-card-body/div[1]/div[1]/div[2]/button[2]"))
)
新增報表_02.click()
廣告媒體_02= WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH,"//textarea[@id='cMediaNote']"))
)
廣告媒體_02.send_keys("TEST")
出勤人員_02=driver.find_element(By.XPATH,"//nb-card-body/div[1]/div[1]/div[1]/div[4]/div[1]/ngx-multiple-sales-selector[1]/nb-select[1]/button[1]")
出勤人員_02.click()
選擇出勤人員_02 = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, "//nb-option[contains(text(), 'Auto_02')]"))
)
選擇出勤人員_02.click()
主委_02=driver.find_element(By.XPATH,"//nb-card-body/div[1]/div[1]/div[1]/div[5]/div[1]/input[1]")
主委_02.send_keys("TEST")
專案_02=driver.find_element(By.XPATH,"//nb-card-body/div[1]/div[1]/div[1]/div[6]/div[1]/input[1]")
專案_02.send_keys("TEST")
確定_02=driver.find_element(By.XPATH,"//button[contains(text(),'確定')]")
確定_02.click()
time.sleep(2)
未結帳報表_02 = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, "//tbody/tr[1]/td[7]/button[3]"))
)
未結帳報表_02.click()
time.sleep(3)
日報總比數_02=extract_total_count(driver, "//nb-card-body/div[@id='printData']/div[1]/div[4]/table[1]/tr[2]/td[2]")

測試結果 = "通過" if 來人總比數_01 == 日報總比數_02 else "失敗"
with open(csv_filename, mode='a', newline='', encoding='utf-8-sig') as file:
    writer = csv.writer(file)
    current_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    writer.writerow(["來人總比數", 來人總比數_01, 日報總比數_02, 測試結果, current_datetime])

#自動化結束，網頁關閉
time.sleep(3)
driver.quit()