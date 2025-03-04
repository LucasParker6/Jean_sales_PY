import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://devjeansalesadmin.webtech888.com/login")
driver.maximize_window()

#測試時間
today_date = datetime.today().strftime('%Y-%m-%d')
current_time = datetime.now().strftime('%H-%M-%S')
csv_filename=f"Daily_Report_{today_date}_{current_time}.csv"

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
銷售前金額_01=WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, "//tbody/tr[3]/td[4]"))
)
欄位數值_01=銷售前金額_01.text
測試結果 = "通過" if 欄位數值_01 == "0萬" else "失敗"
with open(csv_filename, mode='w', newline='', encoding='utf-8-sig') as file:
    writer = csv.writer(file)
    current_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    writer.writerow(["測試項目", "期望值", "實際值", "測試結果", "測試時間"])
    writer.writerow(["銷售前金額", "0萬", 欄位數值_01, 測試結果, current_datetime])

# #建立客戶
# time.sleep(3)
# 客戶資料管理_01 = WebDriverWait(driver, 20).until(
#     EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'賞屋(客戶資料)管理')]"))
# )
# 客戶資料管理_01.click()
# time.sleep(3)
# 賞屋管理_01 = WebDriverWait(driver, 20).until(
#     EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'賞屋管理')]"))
# )
# 賞屋管理_01.click()
# time.sleep(3)
# 新增_01 = WebDriverWait(driver, 20).until(
#     EC.presence_of_element_located((By.XPATH, "//nb-card-body/div[1]/div[2]/div[1]/button[6]"))
# )
# 新增_01.click()
# 賞屋日期_01=WebDriverWait(driver, 20).until(
#     EC.presence_of_element_located((By.XPATH, "//nb-card-body/div[@id='dataToExport']/div[1]/div[1]/div[2]/div[1]/input[1]"))
# )
# 賞屋日期_01.click()
# 選擇賞屋日期_01=WebDriverWait(driver, 20).until(
#     EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'22')]"))
# )
# 選擇賞屋日期_01.click()
# 客戶姓名_01=driver.find_element(By.XPATH,"//nb-card-body/div[@id='dataToExport']/div[1]/div[1]/div[3]/div[1]/input[1]")
# 客戶姓名_01.send_keys("TEST123")
# 市話_01=driver.find_element(By.XPATH,"//nb-card-body/div[@id='dataToExport']/div[1]/div[1]/div[5]/div[1]/input[1]")
# 市話_01.send_keys("0212345678")
# 手機號碼_02=driver.find_element(By.XPATH,"//nb-card-body/div[@id='dataToExport']/div[1]/div[1]/div[6]/div[1]/input[1]")
# 手機號碼_02.send_keys("0912345678")
# 資料確認_01=driver.find_element(By.XPATH,"//nb-card-body/div[@id='dataToExport']/div[1]/div[1]/div[9]/div[1]/nb-select[1]/button[1]")
# 資料確認_01.click()
# 資料確認_是_01=WebDriverWait(driver, 20).until(
#     EC.presence_of_element_located((By.XPATH, "//nb-option[contains(text(), '是')]"))
# )
# 資料確認_是_01.click()
# 第一次來訪是否購買_01=driver.find_element(By.XPATH,"//nb-card-body/div[4]/div[1]/nb-select[1]/button[1]")
# 第一次來訪是否購買_01.click()
# 第一次來訪是否購買_已購_01=WebDriverWait(driver, 20).until(
#     EC.presence_of_element_located((By.XPATH, "//nb-option[contains(text(), '已購')]"))
# )
# 第一次來訪是否購買_已購_01.click()
# 業務員_01=driver.find_element(By.XPATH,"//nb-card-body/div[@id='dataToExport']/div[1]/div[1]/div[13]/div[1]/ngx-sales-selector[1]/nb-select[1]/button[1]")
# 業務員_01.click()
# 選擇業務人員_01 = WebDriverWait(driver, 20).until(
#     EC.presence_of_element_located((By.XPATH, "//nb-option[contains(text(), 'Auto_02')]"))
# )
# 選擇業務人員_01.click()
# 確定新增客資_01=driver.find_element(By.XPATH,"//button[contains(text(),'確定')]")
# 確定新增客資_01.click()

#銷售二房二車
#銷售第一戶
time.sleep(3)
銷控管理_01=driver.find_element(By.XPATH,"//span[contains(text(),'銷控管理')]")
銷控管理_01.click()
time.sleep(1)
銷控表_01=driver.find_element(By.XPATH,"//span[contains(text(),'銷控表')]")
銷控表_01.click()
time.sleep(2)
A1_1_01 = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, "//tbody/tr[3]/td[2]"))
)
A1_1_01.click()
time.sleep(1)
客資編號放大鏡_01 = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, "//nb-card-body/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/nb-form-field[1]/div[2]"))
)
客資編號放大鏡_01.click()
客資編號輸入客戶姓名_01 = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, "//nb-card-body/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/ngx-crm-customer-search[1]/input[1]"))
)
客資編號輸入客戶姓名_01.send_keys("TEST123")
time.sleep(2)
客資編號輸入客戶姓名選擇客戶_01 = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, "//nb-option[contains(text(), ' [10407]TEST123(0912345678) ')]"))
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
選擇銷售時間_01 = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'3')]"))
)
選擇銷售時間_01.click()
車位_01=driver.find_element(By.XPATH,"//nb-card-body/div[1]/div[1]/div[1]/div[2]/div[9]/label[1]/button[1]")
車位_01.click()
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

#銷售第二戶
time.sleep(2)
A2_1_01 = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, "//tbody/tr[3]/td[3]"))
)
A2_1_01.click()
time.sleep(1)
客資編號放大鏡_02 = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, "//nb-card-body/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/nb-form-field[1]/div[2]"))
)
客資編號放大鏡_02.click()
客資編號輸入客戶姓名_02 = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, "//nb-card-body/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/ngx-crm-customer-search[1]/input[1]"))
)
客資編號輸入客戶姓名_02.send_keys("TEST123")
time.sleep(2)
客資編號輸入客戶姓名選擇客戶_02 = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, "//nb-option[contains(text(), ' [10407]TEST123(0912345678) ')]"))
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
選擇銷售時間_02 = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'3')]"))
)
選擇銷售時間_02.click()
車位_02=driver.find_element(By.XPATH,"//nb-card-body/div[1]/div[1]/div[1]/div[2]/div[9]/label[1]/button[1]")
車位_02.click()
time.sleep(5)
選擇車位_02=driver.find_element(By.XPATH,"//nb-card-body/div[1]/div[1]/div[1]/div[2]/div[10]/div[2]/ngx-park-selector[1]/nb-select[1]/button[1]")
選擇車位_02.click()
選擇車位B1_2 = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, "//nb-option[contains(text(), 'B1-2')]"))
)
選擇車位B1_2.click()
車位價格_02=driver.find_element(By.XPATH,"//nb-card-body/div[1]/div[1]/div[1]/div[2]/div[10]/div[3]/nb-form-field[1]/div[1]/input[1]")
車位價格_02.send_keys("100")
確定銷售_02=driver.find_element(By.XPATH,"//button[contains(text(),'確定')]")
確定銷售_02.click()

#銷售後日報表確認
time.sleep(2)
日報表_02= WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH,"//span[contains(text(),'日報表')]"))
)
日報表_02.click()
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
結算_02 = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, "//nb-card-header/button[1]"))
)
time.sleep(5)
銷售後金額=WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, "//body[1]/ngx-app[1]/ngx-pages[1]/ngx-one-column-layout[1]/nb-layout[1]/div[1]/div[1]/div[1]/div[1]/div[1]/nb-layout-column[1]/ngx-report1-detial[1]/div[1]/nb-card[1]/nb-card-body[1]/div[1]/div[2]/table[1]/tbody[1]/tr[3]/td[4]"))
)
欄位數值_02=銷售後金額.text
測試結果 = "失敗" if 欄位數值_01 == "1,200萬" else "通過"
with open(csv_filename, mode='a', newline='', encoding='utf-8-sig') as file:
    writer = csv.writer(file)
    current_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    writer.writerow(["銷售後金額", "1,200萬", 欄位數值_02, 測試結果, current_datetime])

#退第一戶
time.sleep(2)
退戶銷控表_01=driver.find_element(By.XPATH,"//span[contains(text(),'銷控表')]")
退戶銷控表_01.click()
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
選擇退戶日期_01=WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'3')]"))
)
選擇退戶日期_01.click()
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

#退第二戶
time.sleep(2)
退戶A2_1_01 = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, "//tbody/tr[3]/td[3]"))
)
退戶A2_1_01.click()
time.sleep(2)
退戶日期_02=WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, "//nb-card-body/div[1]/div[1]/div[1]/div[2]/div[15]/div[2]/input[1]"))
)
退戶日期_02.click()
time.sleep(2)
選擇退戶日期_02=WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'3')]"))
)
選擇退戶日期_02.click()
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

#退戶後日報表確認
time.sleep(5)
報表管理_03= WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH,"//span[contains(text(),'報表管理')]"))
)
報表管理_03.click()
日報表_03= WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH,"//span[contains(text(),'日報表')]"))
)
日報表_03.click()
新增報表_03= WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH,"//nb-card-body/div[1]/div[1]/div[2]/button[2]"))
)
新增報表_03.click()
廣告媒體_03= WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH,"//textarea[@id='cMediaNote']"))
)
廣告媒體_03.send_keys("TEST")
出勤人員_03=driver.find_element(By.XPATH,"//nb-card-body/div[1]/div[1]/div[1]/div[4]/div[1]/ngx-multiple-sales-selector[1]/nb-select[1]/button[1]")
出勤人員_03.click()
選擇出勤人員_03 = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, "//nb-option[contains(text(), 'Auto_02')]"))
)
選擇出勤人員_03.click()
主委_03=driver.find_element(By.XPATH,"//nb-card-body/div[1]/div[1]/div[1]/div[5]/div[1]/input[1]")
主委_03.send_keys("TEST")
專案_03=driver.find_element(By.XPATH,"//nb-card-body/div[1]/div[1]/div[1]/div[6]/div[1]/input[1]")
專案_03.send_keys("TEST")
確定_03=driver.find_element(By.XPATH,"//button[contains(text(),'確定')]")
確定_03.click()
time.sleep(2)
未結帳報表_03 = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, "//tbody/tr[1]/td[7]/button[3]"))
)
未結帳報表_03.click()
結算_03 = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, "//nb-card-header/button[1]"))
)
退戶後金額_03=WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, "//body[1]/ngx-app[1]/ngx-pages[1]/ngx-one-column-layout[1]/nb-layout[1]/div[1]/div[1]/div[1]/div[1]/div[1]/nb-layout-column[1]/ngx-report1-detial[1]/div[1]/nb-card[1]/nb-card-body[1]/div[1]/div[2]/table[1]/tbody[1]/tr[3]/td[4]"))
)
欄位數值_03=退戶後金額_03.text
測試結果 = "通過" if 欄位數值_03 == "0萬" else "失敗"
with open(csv_filename, mode='a', newline='', encoding='utf-8-sig') as file:
    writer = csv.writer(file)
    current_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    writer.writerow(["退戶後金額", "0萬", 欄位數值_01, 測試結果, current_datetime])


#自動化結束，網頁關閉
time.sleep(3)
driver.quit()