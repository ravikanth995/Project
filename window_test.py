from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchWindowException
from selenium.webdriver.chrome.options import Options
import time

ops = webdriver.ChromeOptions()
ops.add_argument("--disable-notifications")
serv_obj = Service("C:\\Users\\Shashikanth\\Desktop\\Selenium\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service= serv_obj, options= ops)
driver.get("https://www.irctc.co.in/nget/train-search")
driver.maximize_window()
driver.implicitly_wait(10)

driver.execute_script("window.scrollBy(0, 750)")
driver.execute_script("return window.pageYOffset;")
time.sleep(5)

parent_id = driver.current_window_handle
print(parent_id)
print(driver.title)

driver.find_element(By.XPATH, "//*[@id='flight']/a/span").click()
window_id = driver.window_handles

for win in window_id:
    print(win)
    driver.switch_to.window(win)
    print(driver.title)
time.sleep(5)        


driver.switch_to.window(parent_id)
time.sleep(5)





driver.close()