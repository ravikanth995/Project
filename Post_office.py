from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import requests
import time

serv_obj = Service("C:\\Users\\Shashikanth\\Desktop\\Selenium\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service= serv_obj)
driver.implicitly_wait(8)
driver.get("https://www.indiapost.gov.in/vas/Pages/IndiaPostHome.aspx")
driver.maximize_window()

links = driver.find_elements(By.XPATH, "//div[@class = 'levelHolderClass ltr']/ul/li/a")
print("Number of Links Present here is :", len(links))

all_links = driver.find_elements(By.TAG_NAME, "a")
count = 0
for link in all_links:
    url = link.get_attribute("href")
    try :
        None
        res = requests.head(url)
        if res.status_code>= 400:
            print(url, ": is a Broken Link.")
            count += 1

        else:
            print(url, ": is a Valid Link.")
    except Exception as e:
        print(f": Checking error in {url} : {e}")
        count += 1            



driver.close()