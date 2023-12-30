from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

ops = webdriver.ChromeOptions()
ops.add_argument("--disable-notifications")

serv_obj = Service("C:\\Users\\Shashikanth\\Desktop\\Selenium\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service= serv_obj, options= ops)

# driver.get("https://www.indiainfoline.com/markets/hot-stocks")
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
driver.implicitly_wait(8)
print(driver.title)
print(driver.current_url)

driver.execute_script("window.scrollBy(0, 2000)")
driver.execute_script("return window.pageYOffset;")

# rows = len(driver.find_elements(By.XPATH, "//div[@class = 'content']/table/tbody/tr"))
# print(rows)
# count = 0
# for r in range(1, rows+1):
#     change = driver.find_element(By.XPATH, "//div[@class = 'content']/table/tbody/tr["+str(r)+"]/td[1]").text
#     print(change)
#     if change == "Hero Motocorp" :
#         count += 1

# print("Number of Change Table is :", count)
# print("Number of Change Took Place :", rows - count)
time.sleep(5)
# check_boxes = driver.find_elements(By.XPATH, "//table[@id = 'productTable']/tbody/tr/td/input")
# print(len(check_boxes))
# for i in range(len(check_boxes)):
#         check_boxes[i].click()
#         if driver.find_element(By.XPATH, "//ul[@id = 'pagination']/li[2]").click() :
#             for i in range(len(check_boxes)):
#                 check_boxes[i].click()
#                 time.sleep(2)
#         else:
#                 print("Error")    

# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time

# # Assuming 'driver' is your WebDriver instance

# # Function to click checkboxes on the current page
# def click_checkboxes():
#     check_boxes = driver.find_elements(By.XPATH, "//table[@id='productTable']/tbody/tr/td/input")
#     print(f"Number of checkboxes on the current page: {len(check_boxes)}")

#     for checkbox in check_boxes:
#         checkbox.click()

#     return check_boxes  # Return check_boxes to access it outside the function

# # Click checkboxes on the initial page
# check_boxes = click_checkboxes()

# # Check if there is a next page (pagination)
# pagination_elements = driver.find_elements(By.XPATH, "//ul[@id='pagination']/li[2]")
# if pagination_elements and len(pagination_elements) > 0:
#     # Click the next page button
#     pagination_elements[0].click()

#     # Wait for the next page to load (adjust wait time as needed)
#     WebDriverWait(driver, 10).until(EC.staleness_of(check_boxes[0]))

#     # Click checkboxes on the next page
#     check_boxes = click_checkboxes()
#     time.sleep(4)

# else:
#     print("No pagination or error in pagination")



from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Assuming 'driver' is your WebDriver instance

# Function to click checkboxes on the current page
def click_checkboxes():
    check_boxes = driver.find_elements(By.XPATH, "//table[@id='productTable']/tbody/tr/td/input")
    print(f"Number of checkboxes on the current page: {len(check_boxes)}")

    for checkbox in check_boxes:
        checkbox.click()

    return check_boxes  # Return check_boxes to access it outside the function

# Loop through each page
for page in range(4):  # Assuming there are 4 pages, adjust the range accordingly
    # Click checkboxes on the current page
    check_boxes = click_checkboxes()

    # Check if there is a next page (pagination)
    pagination_elements = driver.find_elements(By.XPATH, "//ul[@id='pagination']/li[2]")
    if pagination_elements and len(pagination_elements) > 0:
        # Click the next page button
        pagination_elements[0].click()

        # Wait for the next page to load (adjust wait time as needed)
        WebDriverWait(driver, 10).until(EC.staleness_of(check_boxes[0]))

    else:
        print(f"No pagination on page {page + 1} or error in pagination")

# Close the browser window
driver.quit()


driver.close()
