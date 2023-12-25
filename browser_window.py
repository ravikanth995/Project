from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

serv_obj = Service("C:\\Users\\Shashikanth\\Desktop\\Selenium\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service= serv_obj)

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
window_id = driver.current_url
print(window_id)
print(driver.title)
print(driver.current_window_handle)
time.sleep(4)

driver.find_element(By.PARTIAL_LINK_TEXT, "OrangeHRM").click()
window_id_1 = driver.window_handles
parent_id = window_id_1[0]
child_id = window_id_1[1]
print("Parent Window Id is :",parent_id)
print("Child Window Id is :",child_id)

"""Swittching to Child Window"""
driver.switch_to.window(child_id)
time.sleep(4)

"""Switchnig to Parent Window"""
driver.switch_to.window(parent_id)
time.sleep(4)

