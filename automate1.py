from selenium import webdriver
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.by import By
import time
import requests

serv_obj = Service("C:\\Users\\Shashikanth\\Desktop\\Selenium\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service= serv_obj)
driver.implicitly_wait(10)

driver.get("https://the-internet.herokuapp.com/")
driver.maximize_window()

links = driver.find_elements(By.XPATH, "//div[@id = 'content']/ul/li")
print("Number of Links is : ", len(links))

for link in links:
    print(link.text)

# all_links = driver.find_elements(By.TAG_NAME, "a")
# count = 0
# for link in links:
#     url = link.get_attribute('href')
#     try :
#         res = requests.head(url)  
#         if res.status_code>=400:
#             print(url, "Is Broken Link")
#             count += 1
#         else:
#             print(url, "is a valid link")       

#     except Exception as e :
#         print(e)       

# print("Total number of Broken Links are  :", count)                    

all_links = driver.find_elements(By.TAG_NAME, "a")

    # Counter for broken links
count = 0

    # Iterate over the links
for link in all_links:
        url = link.get_attribute('href')

        try:
            # Send a HEAD request to check the status code
            res = requests.head(url)

            if res.status_code >= 400:
                print(url, "Is a Broken Link")
                count += 1
            else:
                print(url, "is a Valid Link")

        except Exception as e:
            # Handle exceptions if the request fails
            print(f"Error checking link {url}: {e}")
            count += 1







driver.close()