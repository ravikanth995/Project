from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import csv

serv_obj = Service("C:\\Users\\Shashikanth\\Desktop\\Selenium\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service= serv_obj)
driver.implicitly_wait(3)

driver.get("https://en.wikipedia.org/wiki/Results_of_the_2019_Indian_general_election")
driver.maximize_window()

driver.execute_script("window.scrollBy(0, 2100)")
value = driver.execute_script("return window.pageYOffset;")
print("Number of Pixels scrolled is :", value)


table_data = driver.find_elements(By.XPATH, "//table[@class = 'wikitable sortable jquery-tablesorter']/tbody/tr")
print("Number of Table is :", len(table_data))
for data in table_data:
    results = data.text
    print(results)

    """For Extracting Data"""
    # data_rows = [cell.text for cell in data.find_elements(By.TAG_NAME, "tr")]
    # row_data.append(data_rows)

    # with open('election_data.csv', 'w', newline='') as file:
    #     csv_writer = csv.writer(file)
    #     csv_writer.writerows(data_rows)
    

    
       