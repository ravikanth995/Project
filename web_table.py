from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time


ops = webdriver.ChromeOptions()
ops.add_argument("--disable-notifications")
serv_obj = Service("C:\\Users\\Shashikanth\\Desktop\\Selenium\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service= serv_obj, options= ops)

driver.get("https://seleniumpractise.blogspot.com/2021/08/webtable-in-html.html")
driver.maximize_window()
driver.implicitly_wait(10)

No_of_Rows = len(driver.find_elements(By.XPATH, "//table[@id = 'customers']/tbody/tr"))
print(No_of_Rows)

No_of_Cols = len(driver.find_elements(By.XPATH, "//table[@id = 'customers']/tbody/tr[1]/th"))
print(No_of_Cols)

for r in range(2, No_of_Rows+1):
    for c in range(1, No_of_Cols+1):
        data = driver.find_element(By.XPATH, "//table[@id = 'customers']/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
        print(data)
    print()

"""Reading data Based onn condition""" 

for r in range(2, No_of_Rows+1):
    company = driver.find_element(By.XPATH, "//table[@id = 'customers']/tbody/tr["+str(r)+"]/td[2]").text
    if company == "Ola":
        person = driver.find_element(By.XPATH, "//table[@id = 'customers']/tbody/tr["+str(r)+"]/td[3]").text
        print("Person :", person)
        country = driver.find_element(By.XPATH, "//table[@id = 'customers']/tbody/tr["+str(r)+"]/td[4]").text
        print(person, " ", company, " ", country)








driver.close()