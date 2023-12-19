from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

serv_obj = Service("C:\\Users\\Shashikanth\\Desktop\\Selenium\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service= serv_obj)
driver.implicitly_wait(10)
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

name = driver.find_element(By.ID, "name")
name.send_keys("Ravikanth")

email = driver.find_element(By.ID, "email")
email.send_keys("ravikanthchauhan95@gmail.com")

phone = driver.find_element(By.ID, "phone")
phone.send_keys("8095063864")

driver.execute_script("window.scrollBy(0, 200)")
scroll1 = driver.execute_script("return window.pageYOffset;")
print(f"Number of Scrolling pixels of scroll1 is ... {scroll1}")
time.sleep(2)

address = driver.find_element(By.ID, "textarea")
address.send_keys("Railways colony chittapur, dist. Kalburagi PIN 585211")

male_checkbox = driver.find_element(By.ID, "male")
male_checkbox.click()

driver.execute_script("window.scrollBy(200, 400)")
scroll2 = driver.execute_script("return window.pageYOffset;")

check_box = driver.find_elements(By.XPATH, "//div[@class='form-group']/div/input[@type = 'checkbox']")
print("Number of Checkboxes are :", len(check_box))
try :
     
    for i in range(len(check_box)) :
        check_box[i].click()

except Exception as e:
    print(f"Error has encountered as {e}")


drp_down = driver.find_element(By.XPATH, "//select[@id = 'country']")
drp_country = Select(drp_down)
drp_country.select_by_visible_text("India")

colors = driver.find_element(By.XPATH, "//select[@id = 'colors']")
color = Select(colors)
color.select_by_visible_text("Green")

driver.execute_script("window.scrollBy(400, 500)")
scroll3 = driver.execute_script("return window.pageYOffset;")
print(f"The Scroll3 pixel is : {scroll3}")

driver.find_element(By.ID, "datepicker").click()
print("Date clicked")

# date_picking = driver.find_elements(By.XPATH, "//table[@class = 'ui-datepicker-calendar']/tbody/tr/td/a[@class = 'ui-state-default']")
# for i in date_picking :
#     if i.text == "15" :
#         i.click()
#         break
# time.sleep(4)    

day = "9"
month = "March"
Year = "2022"
driver.find_element(By.ID, "datepicker").click()

while True :
    months = driver.find_element(By.XPATH, "//div/span[@class = 'ui-datepicker-month']").text

    years = driver.find_element(By.XPATH, "//div/span[@class = 'ui-datepicker-year']").text

    if months == month and years == Year :
        break
    else:
        driver.find_element(By.XPATH, "//div/a[1]/span[text() = 'Prev']").click()

dates = driver.find_elements(By.XPATH, "//table[@class = 'ui-datepicker-calendar']/tbody/tr/td/a")
for date in dates :
    if date.text == day :
        date.click()
        break

print("Date, Month and Year is been set in calender.")

link_HRM = driver.find_element(By.XPATH, "//a[text() =  'orange HRM']")
link_HRM.click()
print("Entered in Orange HRM Website.")

name_HRM = driver.find_element(By.NAME, "username")
name_HRM.send_keys("admin")

pass_HRM = driver.find_element(By.NAME, "password")
pass_HRM.send_keys("admin123")

login_btn = driver.find_element(By.XPATH, "//button[@type = 'submit']")
login_btn.click()
print("Log in to Orange HRM is Successfull.....")

admin = driver.find_element(By.XPATH,  "//li[1]//a[1]//span[1]")
admin.click()

try : 
    user_name = driver.find_element(By.XPATH, "//div[@class = 'oxd-grid-4 orangehrm-full-width-grid']/div[1]/div[1]/div[2]/input")
    user_name.send_keys("Admin")
    print("Username has been entered.")

except Exception :
    print("Error took place, kindly correct it.")  

try :
    role = driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/div/div/div[1]")
    role.click()

except Exception as e:
    print(f"Error is encountred{e}")   
     
driver.back()
time.sleep(3)


   
        
    