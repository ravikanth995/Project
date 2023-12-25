
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
import time

ser_obj = Service("C:\\Users\\Shashikanth\\Desktop\\Selenium\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service= ser_obj)

# driver.get("https://seleniumbase.io/demo_page/")
# driver.maximize_window()

# driver.execute_script("window.scrollBy(0, 200)")
# value = driver.execute_script("return window.pageYOffset;")
# print("Number of Pixels scrolled is :",value)

# input_ele = driver.find_element(By.ID, "myTextInput")
# input_ele.send_keys("Hi Hello")

# time.sleep(2)

# input_2 = driver.find_element(By.ID, "myTextInput2")
# input_2.clear()

# place = driver.find_element(By.ID, "placeholderText")
# place.send_keys("Hi Bro...")
# time.sleep(4)

# driver.find_element(By.ID, "svgRect").click()

# driver.switch_to.frame("myFrame3")
# driver.find_element(By.ID, "checkBox6").click()
# time.sleep(3)


driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

driver.execute_script("window.scrollBy(0, 1200)")
value = driver.execute_script("return window.pageYOffset;")
print("Number of Pixels scrolled is :",value)
time.sleep(4)

driver.switch_to.frame("frame-one796456169")
name = driver.find_element(By.ID, "RESULT_TextField-0")
name.click()
name.send_keys("Ravikanth")
time.sleep(4)

driver.find_element(By.XPATH, "//label[@for = 'RESULT_RadioButton-1_0']").click()

driver.find_element(By.XPATH, "//input[@id='RESULT_TextField-2']").send_keys("03/05/1995")

# day = "05"
# month = "March"
# year = "2023"

# all_link = driver.find_elements(By.XPATH, "//span[@class = 'ui-datepicker-month']")
# print("Number of Months :", len(all_link))

# years_drp = driver.find_elements(By.XPATH, "//select[@class = 'ui-datepicker-year']/option")
# print("Number of Years is :", len(years_drp))

# calender_icon = driver.find_element(By.XPATH, "//*[@id='q4']/span")
# calender_icon.click()


# while True :
#     months = driver.find_element(By.XPATH, "//span[@class = 'ui-datepicker-month']").text

#     years_element = driver.find_element(By.XPATH, "//select[@aria-label='Select year']")
#     years_selected = Select(years_element)
#     years_selected_1 = years_selected.first_selected_option.text

#     if months == month and  years_selected_1 == year:
#         break
#     else:
#         driver.find_element(By.XPATH, "//div[@id = 'ui-datepicker-div']//div/a/span[text() = 'Prev']").click()


# dates = driver.find_elements(By.XPATH, "//table[@class = 'ui-datepicker-calendar']/tbody/tr/td/a")
# print("Number of Dates are :", len(dates))
# for date in dates :
#    if date.text  == day :
#       date.click()
#       break

occupation_drp = driver.find_element(By.XPATH, "//select[@id='RESULT_RadioButton-3']")
drp_down = Select(occupation_drp)
drp_down.select_by_visible_text("Automation Engineer")

   
time.sleep(5)   
driver.close()