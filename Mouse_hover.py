from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
import time

ops = webdriver.ChromeOptions()
ops.add_argument("--disable-notifications")
serv_obj = Service("C:\\Users\\Shashikanth\\Desktop\\Selenium\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service= serv_obj, options= ops)

driver.get("https://www.flipkart.com/")
driver.maximize_window()
driver.implicitly_wait(10)

def MouseHOver():
    fashion = driver.find_element(By.XPATH, "//div[@class = 'YBLJE4']/div/div/img[@alt = 'Fashion']")
    act = ActionChains(driver)
    act.move_to_element(fashion).click().perform()
    time.sleep(5)
    
    
MouseHOver()    
