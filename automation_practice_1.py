from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
import time

serv_obj = Service("C:\\Users\\Shashikanth\\Desktop\\Selenium\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service= serv_obj)
driver.implicitly_wait(10)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

driver.execute_script("window.scrollBy(0, 400)")
value = driver.execute_script("return window.pageYOffset;")
print(f"Pixels scrolled are  : {value}")

male = driver.find_element(By.ID, "male")
print("Is Male attribute there :", male.is_displayed())
print("Is Male attribute enabled..:", male.is_enabled())
print("Is Male attribute selected..:", male.is_selected())
male.click()
print("Is Male attribute selected..:", male.is_selected())

driver.execute_script("window.scrollBy(400, 500)")
value_1 = driver.execute_script("return window.pageYOffset;")
print(f"Pixels Scrolled down by : {value_1}")

orange_HRM = driver.find_element(By.LINK_TEXT, "orange HRM")
orange_HRM.click()

driver.back()
open_cart = driver.find_element(By.XPATH, "//a[normalize-space()='open cart']")
open_cart.click()

driver.execute_script("window.scrollBy(0, 850)")
value_2 = driver.execute_script("return window.pageYOffset;")
print(f"Page Scrolled by {value_2}")

footer = driver.find_elements(By.XPATH, "/html/body/footer//li/a")
print("How many Footer found :", len(footer))
# print(footer[4].text)

# for ele in footer:
#     print(ele.text)
for ele in footer :
    print(ele.text)



driver.close()