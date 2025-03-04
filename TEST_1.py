import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://tcb-bank-sit.webtech888.com/login")
driver.maximize_window()

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
menu_titles_text_1 = []
menu_titles_1 = driver.find_elements(By.XPATH, "//body/ngx-app[1]/ngx-pages[1]/ngx-one-column-layout[1]/nb-layout[1]/div[1]/div[1]/div[1]/nb-sidebar[1]/div[1]/div[1]/nb-menu[1]/ul[1]/li[1]/a[1]/span[1]")
for title in menu_titles_1:
    menu_titles_text_1.append(title.text)

menu_titles_text_2 = []
menu_titles_2 = driver.find_elements(By.XPATH, "//body/ngx-app[1]/ngx-pages[1]/ngx-one-column-layout[1]/nb-layout[1]/div[1]/div[1]/div[1]/nb-sidebar[1]/div[1]/div[1]/nb-menu[1]/ul[1]/li[2]/a[1]/span[1]")
for title in menu_titles_2:
    menu_titles_text_2.append(title.text)

menu_titles_text_3 = []
menu_titles_3 = driver.find_elements(By.XPATH, "//span[contains(text(),'代收代付特店管理')]")
for title in menu_titles_3:
    menu_titles_text_3.append(title.text)

menu_titles_text_4 = []
menu_titles_4 = driver.find_elements(By.XPATH, "//span[contains(text(),'管理性報表')]")
for title in menu_titles_4:
    menu_titles_text_4.append(title.text)

menu_titles_text_5 = []
menu_titles_5 = driver.find_elements(By.XPATH, "//body/ngx-app[1]/ngx-pages[1]/ngx-one-column-layout[1]/nb-layout[1]/div[1]/div[1]/div[1]/nb-sidebar[1]/div[1]/div[1]/nb-menu[1]/ul[1]/li[5]/a[1]/span[1]")
for title in menu_titles_5:
    menu_titles_text_5.append(title.text)

with open('login_records.csv', 'a', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['角色', "功能項"])
    writer.writerow([B1, menu_titles_text_1+menu_titles_text_2+menu_titles_text_3+menu_titles_text_4+menu_titles_text_5])

time.sleep(999)
driver.quit()