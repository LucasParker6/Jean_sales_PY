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

username_input_1 = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, AF))
)
username_input_1.send_keys(B1)
password_input_1=driver.find_element(By.XPATH,PF)
password_input_1.send_keys(P1)
Login=driver.find_element(By.XPATH,LIB)
Login.click()

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
with open(csv_filename, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["帳號", 'Title'])  # 將 "帳號" 和 'Title' 作為列表寫入CSV的一行
    for title in titles:
        writer.writerow([B1_1, title])  # 將 B1 和 title 作為列表寫入CSV的每一行

#B1登出
time.sleep(1)
logout_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, LOB))
)
logout_button.click()

username_input_1 = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, AF))
)
username_input_1.send_keys(B2)
password_input_1=driver.find_element(By.XPATH,PF)
password_input_1.send_keys(P1)
Login=driver.find_element(By.XPATH,LIB)
Login.click()

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
        writer.writerow([B2_1, title])  # 將 B2 和 title 作為列表寫入CSV的每一行

#B2登出
time.sleep(1)
logout_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, LOB))
)
logout_button.click()

username_input_1 = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, AF))
)
username_input_1.send_keys(B3)
password_input_1=driver.find_element(By.XPATH,PF)
password_input_1.send_keys(P1)
Login=driver.find_element(By.XPATH,LIB)
Login.click()

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
        writer.writerow([B3_1, title])  # 將 B2 和 title 作為列表寫入CSV的每一行

#B3登出
time.sleep(1)
logout_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, LOB))
)
logout_button.click()

username_input_1 = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, AF))
)
username_input_1.send_keys(B4)
password_input_1=driver.find_element(By.XPATH,PF)
password_input_1.send_keys(P1)
Login=driver.find_element(By.XPATH,LIB)
Login.click()

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
        writer.writerow([B4_1, title])  # 將 B2 和 title 作為列表寫入CSV的每一行

#B4登出
time.sleep(1)
logout_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, LOB))
)
logout_button.click()

username_input_1 = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, AF))
)
username_input_1.send_keys(H1)
password_input_1=driver.find_element(By.XPATH,PF)
password_input_1.send_keys(P1)
Login=driver.find_element(By.XPATH,LIB)
Login.click()

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
        writer.writerow([H1_1, title])  # 將 B2 和 title 作為列表寫入CSV的每一行

#H1登出
time.sleep(1)
logout_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, LOB))
)
logout_button.click()

username_input_1 = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, AF))
)
username_input_1.send_keys(H2)
password_input_1=driver.find_element(By.XPATH,PF)
password_input_1.send_keys(P1)
Login=driver.find_element(By.XPATH,LIB)
Login.click()

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
        writer.writerow([H2_1, title])  # 將 B2 和 title 作為列表寫入CSV的每一行

#H2登出
time.sleep(1)
logout_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, LOB))
)
logout_button.click()

username_input_1 = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, AF))
)
username_input_1.send_keys(H3)
password_input_1=driver.find_element(By.XPATH,PF)
password_input_1.send_keys(P1)
Login=driver.find_element(By.XPATH,LIB)
Login.click()

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
        writer.writerow([H3_1, title])  # 將 B2 和 title 作為列表寫入CSV的每一行

#H3登出
time.sleep(1)
logout_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, LOB))
)
logout_button.click()

username_input_1 = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, AF))
)
username_input_1.send_keys(H4)
password_input_1=driver.find_element(By.XPATH,PF)
password_input_1.send_keys(P1)
Login=driver.find_element(By.XPATH,LIB)
Login.click()

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
        writer.writerow([H4_1, title])  # 將 B2 和 title 作為列表寫入CSV的每一行

#H4登出
time.sleep(1)
logout_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, LOB))
)
logout_button.click()

username_input_1 = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, AF))
)
username_input_1.send_keys(H5)
password_input_1=driver.find_element(By.XPATH,PF)
password_input_1.send_keys(P1)
Login=driver.find_element(By.XPATH,LIB)
Login.click()

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
        writer.writerow([H5_1, title])  # 將 B2 和 title 作為列表寫入CSV的每一行

#H5登出
time.sleep(1)
logout_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, LOB))
)
logout_button.click()

#自動化結束，網頁關閉
time.sleep(2)
driver.quit()


# 設定兩個 CSV 檔案的檔名
csv_filename = "Login_Test_Report.csv"  # 替換為實際測試生成的CSV文件名
other_csv_filename = "Expected_Permissions.csv"  # 替換為對比的預期結果CSV文件名

# 讀取兩個 CSV 檔案的所有行
current_rows = []
other_rows = []

# 讀取 csv_filename 的所有行
with open(csv_filename, 'r', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        current_rows.append([cell.strip() for cell in row])  # 去除每個單元格的空格

# 讀取 other_csv_filename 的所有行
with open(other_csv_filename, 'r', newline='') as other_csvfile:
    reader = csv.reader(other_csvfile)
    for row in reader:
        other_rows.append([cell.strip() for cell in row])  # 去除每個單元格的空格

# 排序兩個列表以便比對
current_rows.sort()
other_rows.sort()

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
    print("角色權限對應正確")

# 顯示在 csv_filename 中少了的行
if missing_rows:
    print(f"在 {csv_filename} 中比 {other_csv_filename} 少的權限:")
    for row in missing_rows:
        print(row)
else:
    print("角色權限對應正確")