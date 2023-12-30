from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

ops = webdriver.ChromeOptions()
ops.add_argument("--disable-notifications")
serv_obj = Service("C:\\Users\\Shashikanth\\Desktop\\Selenium\\chromedriver-win64\\chromedriver.exe")

driver = webdriver.Chrome(service= serv_obj, options= ops)
# driver.get("https://en.wikipedia.org/wiki/2019_Indian_general_election")
driver.get("https://practice.expandtesting.com/dynamic-table")
driver.maximize_window()
driver.implicitly_wait(10)
print(driver.title)
print(driver.current_url)

# No_of_Rows = len(driver.find_elements(By.XPATH, "//*[@id='mw-content-text']/div[1]/table[5]/tbody/tr"))
# print(No_of_Rows)

# No_of_Cols = len(driver.find_elements(By.XPATH, "//*[@id='mw-content-text']/div[1]/table[5]/thead/tr/th"))
# print(No_of_Cols)

# for r in range(2, No_of_Rows+1):
#     for c in range(1, No_of_Cols+1):
#         data = driver.find_element(By.XPATH, "//*[@id='mw-content-text']/div[1]/table[5]/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
#         print(data, end= ", ")
#     print()    


# """Reading Data Based Condition"""
# for r in range(2, No_of_Rows + 1):
#     state = driver.find_element(By.XPATH,"//*[@id='mw-content-text']/div[1]/table[5]/tbody/tr["+str(r)+"]/td[1]").text
#     if state == "Karnataka":
#         electors = driver.find_element(By.XPATH, "//*[@id='mw-content-text']/div[1]/table[5]/tbody/tr["+str(r)+"]/td[2]").text
#         print(electors, " ", state)
#         voters = driver.find_element(By.XPATH, "//*[@id='mw-content-text']/div[1]/table[5]/tbody/tr["+str(r)+"]/td[3]").text
#         turnout = driver.find_element(By.XPATH, "//*[@id='mw-content-text']/div[1]/table[5]/tbody/tr["+str(r)+"]/td[4]").text
#         total_seats = driver.find_element(By.XPATH, "//*[@id='mw-content-text']/div[1]/table[5]/tbody/tr["+str(r)+"]/td[5]").text
#         print(state, " ", electors, " ", voters, " ", turnout, " ", total_seats)
#         karnataka = driver.find_element(By.XPATH, "//*[@id='mw-content-text']/div[1]/table[5]/tbody/tr[16]/td").text
#         print(karnataka, end= " ")


"""Dealing with Dynamic Table"""
rows = len(driver.find_elements(By.XPATH, "//table[@class = 'table table-striped']/tbody/tr"))
print(rows)
count = 0
for r in range(1, rows+1):
    disk = driver.find_element(By.XPATH, "//table[@class = 'table table-striped']/tbody/tr["+str(r)+"]/td").text
    if disk == "0.7 MB/s":
        count += 1
print("Total Number of Users :", rows)
print("Number of Disk is :", count)
print("Number of Disabled users :", rows - count)        
driver.close()