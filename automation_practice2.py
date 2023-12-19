
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException


import time

driver = webdriver.Chrome()
driver.get("https://www.google.com/search?q=automation+testing+practice&sca_esv=591685144&sxsrf=AM9HkKku5amdFj3-EcKJXOQ7-nXm9Ne--Q%3A1702831419113&ei=OyV_Zc3BBp_04-EPzvqFwAY&ved=0ahUKEwiNy-Su9ZaDAxUf-jgGHU59AWgQ4dUDCBA&uact=5&oq=automation+testing+practice&gs_lp=Egxnd3Mtd2l6LXNlcnAiG2F1dG9tYXRpb24gdGVzdGluZyBwcmFjdGljZTIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABDIGEAAYFhgeMgYQABgWGB4yBhAAGBYYHjIGEAAYFhgeSOB3UOIBWOhzcAJ4AZABBJgBiQKgAbAjqgEGMS4zMC4yuAEDyAEA-AEBqAIUwgIKEAAYRxjWBBiwA8ICDxAAGIAEGIoFGEMYsAMYCsICExAuGIAEGIoFGEMYxwEY0QMYsAPCAgoQIxiABBiKBRgnwgILEAAYgAQYsQMYgwHCAg0QABiABBiKBRhDGLEDwgIOEAAYgAQYigUYsQMYgwHCAggQABiABBixA8ICBxAjGOoCGCfCAhkQLhiABBiKBRhDGMcBGNEDGOoCGLQC2AEBwgITEAAYgAQYigUYQxjqAhi0AtgBAcICBBAjGCfCAhcQLhiABBiKBRiRAhixAxiDARjHARjRA8ICCxAuGIMBGLEDGIAEwgIREC4YgAQYsQMYgwEYxwEY0QPCAgsQLhiABBixAxiDAcICJhAuGIAEGIoFGJECGLEDGIMBGMcBGNEDGJcFGNwEGN4EGOAE2AECwgIKEAAYgAQYigUYQ8ICEBAAGIAEGIoFGEMYsQMYgwHCAhAQLhiABBiKBRhDGMcBGNEDwgIKEC4YgAQYigUYQ8ICEBAAGIAEGBQYhwIYsQMYgwHCAgoQABiABBgUGIcCwgITEC4YgAQYigUYQxixAxjHARjRA8ICDhAuGIAEGLEDGMcBGNED4gMEGAAgQYgGAZAGCroGBggBEAEYAboGBggCEAEYFA&sclient=gws-wiz-serp")
driver.implicitly_wait(10)
driver.maximize_window()

test = driver.find_element(By.NAME, "q")
test.clear()
test.send_keys("Automation testing Practice")

driver.find_element(By.XPATH, "//span[@class='z1asCe MZy1Rb']//*[name()='svg']").click()


driver.find_element(By.XPATH, "//h3[text() = 'Automation Testing Practice']").click()

input = driver.find_element(By.ID, "name")
input.click()
input.send_keys("Ravikanth")

email = driver.find_element(By.ID, "email")
email.click()
email.send_keys("Ravikanthchauhan95@gmail.com")

phone = driver.find_element(By.ID, "phone")
phone.click()
phone.send_keys("99082727")

driver.execute_script("window.scrollBy(0, 300)")
value = driver.execute_script("return window.pageYOffset;")
print("No. of Pixels moved is :", value)

address = driver.find_element(By.ID, "textarea")
address.click()
address.send_keys("Railways station area Chittapur")

male = driver.find_element(By.ID, "male")
male.click()

driver.execute_script("window.scrollBy(0, 100)")
values = driver.execute_script("return window.pageYOffset;")
print("NUmber of Pixels scrolled is :", values)

check_box = driver.find_elements(By.XPATH, "//div[@class = 'form-group']/div/input[@type = 'checkbox']")
print("Number of Checkboxes are :",len(check_box))
for i in range(len(check_box)):
    check_box[i].click()
    
    
drpdown = driver.find_element(By.XPATH, "//select[@id = 'country']")
drp_country = Select(drpdown)
drp_country.select_by_visible_text("India")

color = driver.find_element(By.ID, "colors")
color_select = Select(color)
color_select.select_by_visible_text("Green")
color_option = len(color_select.options)
print(f"Number of color options are :{color_option}")


year = "1995"
month = "March"
date = "5"

driver.find_element(By.ID, "datepicker").click()

try :
    dates = driver.find_elements(By.XPATH, "//table[@class ='ui-datepicker-calendar']/tbody/tr/td/a")
    for ele in dates:
        if ele.text ==  date :
            ele.click()
            break
    time.sleep(3)
except Exception :
    print("Error in Loop.")       

finally:
    print("Looping of Clicking Date Successful.....")

link = driver.find_element(By.XPATH, "//a[normalize-space()='open cart']")
link.click()

search = driver.find_element(By.NAME, "search")
search.click()
search.send_keys("iPhone 12")

driver.execute_script("window.scrollBy(200, 500)")
valued = driver.execute_script("return window.pageYOffset;")
print("Number of Pixels scrolled is :", valued)
time.sleep(2)

MacBook = driver.find_element(By.XPATH, "//a[normalize-space()='MacBook']")
MacBook.click()
time.sleep(1)

driver.execute_script("window.scrollBy(0, 200)")
value1 = driver.execute_script("return window.pageYOffset;")
print("Number of Pixels are :", value1)

quantity = driver.find_element(By.NAME, "quantity")
quantity.clear()
quantity.send_keys("5")

cart_button = driver.find_element(By.ID, "button-cart")
cart_button.click()
try :
    review = driver.find_element(By.LINK_TEXT, "Write a review")
    review.click()
    print("Succeded in Clicking review button but Button is not working.......")
except Exception :
    print("Error in XPATH Locator.")

driver.back()
print("Browser reversed to earlier page.......")

driver.execute_script("window.scrollBy(200, 500)")
valued2 = driver.execute_script("return window.pageYOffset;")
print("Number of Pixels scrolled is :", valued2)
time.sleep(2)

iphone = driver.find_element(By.XPATH, "//a[text() = 'iPhone']")
iphone.click()

driver.execute_script("window.scrollBy(0, 200)")
valued3 = driver.execute_script("return window.pageYOffset;")
print(f"The Number of pixels scrolled is {valued3} ")

driver.back()
driver.refresh()
print("Done Back and Refreshing...................")

# iphone_quantity = driver.find_element(By.NAME, 'quantity')
# iphone_quantity.send_keys("4")
# time.sleep(1)

# button_cart = driver.find_element(By.ID, "button-cart")
# button_cart.click()
# time.sleep(1)

driver.execute_script("window.scrollBy(0, 300)")
driver.execute_script("return window.pageYOffset;")
time.sleep(2)

link_text = driver.find_element(By.LINK_TEXT, "My Account")
link_text.click()
time.sleep(3)
