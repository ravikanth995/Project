from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import requests
import time

serv_obj = Service("C:\\Users\\Shashikanth\\Desktop\\Selenium\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service= serv_obj)

driver.get("https://www.indiapost.gov.in/vas/Pages/IndiaPostHome.aspx")
driver.maximize_window()
driver.implicitly_wait(8)

all_link = driver.find_elements(By.XPATH, "//div[@class = 'row']/div/figure/a")
print("Number of Links are :", len(all_link))

a_link = driver.find_elements(By.XPATH, "//a")
print("All Links :", len(a_link))

broken_links = 0
valid_links = 0
for link in a_link:
    url = link.get_attribute('href')
    try :
        res = requests.head(url)
        if res.status_code>=400:
            print(url,": is a broken link.")
            
            broken_links += 1
        else:
            print(url, ": is a valid link.")
            valid_links += 1
    except Exception as e:
        print(f" Error checking {url} in {e}")
        broken_links += 1  

print("Summary")
print("Total Links:", len(a_link))
print(f"Number of Broken Links : {broken_links}")
print(f"Number of Valid Links : {valid_links}")                      