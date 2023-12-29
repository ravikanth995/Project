from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

ops = webdriver.ChromeOptions()
ops.add_argument("--disable-notifications")

serv_obj = Service("C:\\Users\\Shashikanth\\Desktop\\Selenium\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service= serv_obj, options= ops)

driver.get("https://cosmocode.io/automation-practice-webtable/")
driver.maximize_window()
driver.implicitly_wait(10)

print(driver.title)
print(driver.current_url)

# No_of_rows = len(driver.find_elements(By.XPATH, "//table[@id = 'countries']/tbody/tr"))
# print(No_of_rows)

# No_of_Cols = len(driver.find_elements(By.XPATH, "//table[@id = 'countries']/tbody/tr/td"))
# print(No_of_Cols)

# for r in range(2, No_of_rows+1):
#     for c in range(1, No_of_Cols+1):
#         data = driver.find_element(By.XPATH, "//table[@id = 'countries']/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
#         print(data)
#     print()

No_of_rows = len(driver.find_elements(By.XPATH, "//table[@id='countries']/tbody/tr"))
print("Number of Rows:", No_of_rows)

# Assuming the number of columns is the same for all rows, pick any row to count the columns
# In this example, I'm using the first row (index 1)
No_of_Cols = len(driver.find_elements(By.XPATH, "//table[@id='countries']/tbody/tr[1]/td"))
print("Number of Columns:", No_of_Cols)

for r in range(2, No_of_rows+1):
    for c in range(1, No_of_Cols+1):
        data = driver.find_element(By.XPATH, "//table[@id='countries']/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
        print(data)
    print()

"""This is Web Table By Selenium"""



