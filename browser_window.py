from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

serv_obj = Service("C:\\Users\\Shashikanth\\Desktop\\Selenium\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service= serv_obj)

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
driver.implicitly_wait(10)
# window_id = driver.current_url
# print(window_id)
# print(driver.title)
# print(driver.current_window_handle)
# time.sleep(4)

# driver.find_element(By.PARTIAL_LINK_TEXT, "OrangeHRM").click()
# window_id_1 = driver.window_handles
# parent_id = window_id_1[0]
# child_id = window_id_1[1]
# print("Parent Window Id is :",parent_id)
# print("Child Window Id is :",child_id)

# """Swittching to Child Window"""
# driver.switch_to.window(child_id)
# time.sleep(4)

# """Switchnig to Parent Window"""
# driver.switch_to.window(parent_id)
# time.sleep(4)



window_id = driver.current_window_handle
print(window_id)
print(driver.current_url)
print(driver.title)

driver.execute_script("window.scrollBy(0, 500)")
driver.execute_script("return pageYOffset;")
driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[3]/div[2]/p[2]/a").click()
parent_id = window_id[0]
child_id = window_id[1]
print("Parent Id is :",parent_id)
print("Child Id is :", child_id)
time.sleep(4)

time.sleep(3)
