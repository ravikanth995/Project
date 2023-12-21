from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

import time

# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.support.ui import Select
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# import time

serv_obj = Service("C:\\Users\\Shashikanth\\Desktop\\Selenium\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service = serv_obj)
driver.get("https://testautomationpractice.blogspot.com/")
driver.implicitly_wait(5)
driver.maximize_window()
time.sleep(3)

driver.execute_script("window.scrollBy(0, 500)")
value = driver.execute_script("return window.pageYOffset;")
print(f"The Pixels Scrolled is :{value}")
time.sleep(3)

check_boxes = driver.find_elements(By.XPATH, "//input[@class = 'form-check-input' and @type = 'checkbox']")
print("Number of Checkbox are :", len(check_boxes))

for i in range(len(check_boxes)):
    check_boxes[i].click()
print("Check boxes of Days Selected.")
print("-"*40)

drp_downs = driver.find_element(By.ID, "country")
drp_downs.click()
drp_country = Select(drp_downs)
drp_country.select_by_visible_text("India")
print("Drop down of Countries selected.")
print("-"*40)


driver.execute_script("window.scrollBy(500, 550)")
scroll1 = driver.execute_script("return window.pageYOffset;")
print("Scroll 1 Page Scrolled is --> :", scroll1)

driver.find_element(By.ID, "datepicker").click()
print("Date Input Selected.")
day = "04"
months = "March"
years = "2020"

while True :
    mon = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-month']").text

    yr = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-year']").text

    if mon == months and yr == years :
        break 
    else:
        driver.find_element(By.XPATH, "//div/a[1]/span[text() = 'Prev']").click()
print("Previous Arrow clicked.")

day = "9"
month = "March"
Year = "2021"
driver.find_element(By.ID, "datepicker").click()

while True :
    months = driver.find_element(By.XPATH, "//div/span[@class = 'ui-datepicker-month']").text

    years = driver.find_element(By.XPATH, "//div/span[@class = 'ui-datepicker-year']").text

    if months == month and years == Year :
        break
    else:
        driver.find_element(By.XPATH, "//div/a[1]/span[text() = 'Prev']").click()
        break

dates = driver.find_elements(By.XPATH, "//table[@class = 'ui-datepicker-calendar']/tbody/tr/td/a")
for date in dates :
    if date.text == day :
        date.click()
        time.sleep(3)
        break



    