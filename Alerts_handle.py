from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

serv_obj = Service("C:\\Users\\Shashikanth\\Desktop\\Selenium\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service= serv_obj)
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")
driver.implicitly_wait(8)

try :
    alert_btn = driver.find_element(By.XPATH, "//button[@onclick = 'myFunctionAlert()']")
    alert_btn.click()
    print("Clicked on Alert Button.")
    time.sleep(4)
    alert_ok = driver.switch_to.alert
    alert_ok.accept()
    time.sleep(7)

except Exception as e:
    print(f"Error found is {e}")

try :
    confirm_btn = driver.find_element(By.XPATH, "//button[@onclick = 'myFunctionConfirm()']")
    confirm_btn.click()
    print("Clicked on Confirm Button.")
    confirm_alert = driver.switch_to.alert
    print(confirm_alert.text)
    confirm_alert.accept()
    time.sleep(5)
    print("Accepted the Ok button.")

except Exception as e:
    print(f" Error is : {e}")

try :
    time.sleep(5)
    prompt_btn = driver.find_element(By.XPATH, "//button[@onclick = 'myFunctionPrompt()']")
    prompt_btn.click()
    prompt = driver.switch_to.alert
    print(prompt.text)
    prompt.send_keys("Hi There....")
    prompt.dismiss()   
    time.sleep(8)
    
    
except Exception as e:
    print(f"{e}")

