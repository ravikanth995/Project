from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
import time

serv_obj = Service("C:\\Users\\Shashikanth\\Desktop\\Selenium\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service= serv_obj)

driver.get("https://demo.automationtesting.in/Frames.html")
driver.maximize_window()
driver.implicitly_wait(10)

driver.execute_script("window.scrollBy(0, 400)")
value = driver.execute_script("return window.pageYOffset;")

driver.find_element(By.XPATH, "//div[@class = 'tabpane']/ul/li[1]/a").click()

driver.switch_to.frame("SingleFrame")
iframe = driver.find_element(By.XPATH, "/html/body/section/div/div/div/input[@type = 'text']")
iframe.send_keys("Hi Helo man")

print("Entered in iFrame")


driver.switch_to.default_content()

iframe_2 = driver.find_element(By.XPATH, "//div[@class = 'tabpane']/ul/li[2]/a")
iframe_2.click()


outerframe = driver.find_element(By.XPATH, "//iframe[@src='MultipleFrames.html']")
driver.switch_to.frame(outerframe)
print("Entered in OuterFrame")


inner_frame = driver.find_element(By.XPATH, "/html/body/section/div/div/iframe")
driver.switch_to.frame(inner_frame)
print("Entered in InnerFrame")

inner_most = driver.find_element(By.XPATH, "//input[@type='text']")
inner_most.send_keys("Hi Hello Handsome... Kaisa hai Baila")
driver.switch_to.parent_frame()
driver.switch_to.default_content()

driver.find_element(By.XPATH, "//div[@class = 'tabpane']/ul/li[1]/a").click()
driver.back()
time.sleep(4)




