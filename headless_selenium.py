def headless_mode():

    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.common.keys import Keys
    import time
    import os

    ops = Options()
    ops.add_argument("--start-maximized")
    ops.add_argument('--headless')
    # ops.headless = True

    chrome_driver_path = "C:\\Users\\Shashikanth.DESKTOP-9G7BEQK\\Desktop\\Selenium\\chromedriver-win64\\chromedriver.exe"
    ops.binary_location = chrome_driver_path

    driver = webdriver.Chrome(options=ops)
    return driver

driver =  headless_mode()
driver.get("https://www.browserstack.com/")
print(driver.title)
print(driver.current_url)


