from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import requests
import time

serv_obj = Service("C:\\Users\\Shashikanth\\Desktop\\Selenium\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service= serv_obj)

driver.get("https://demo.automationtesting.in/Alerts.html")
driver.implicitly_wait(8)
driver.maximize_window()

"""First Alert Button"""
alert_ok = driver.find_element(By.PARTIAL_LINK_TEXT, "Alert")
alert_ok.click()

alert_box = driver.find_element(By.XPATH, "//button[@onclick = 'alertbox()']")
alert_box.click()

alert_text = driver.switch_to.alert
alert_text.accept()


"""Second Alert Button"""
alert_ok = driver.find_element(By.XPATH, "//div[@class = 'col-md-12']/div/div/ul/li[2]/a")
alert_ok.click()

alert_confirm_box = driver.find_element(By.XPATH, "//button[@onclick = 'confirmbox()']")
alert_confirm_box.click()

alert_switch = driver.switch_to.alert
print(alert_switch.text)
alert_switch.accept()

"""Third Alert Button"""
alert_text = driver.find_element(By.XPATH, "//div[@class = 'col-md-12']/div/div/ul/li[3]/a")
alert_text.click()

alert_prompt = driver.find_element(By.XPATH, "//button[@onclick = 'promptbox()']")
alert_prompt.click()

alert_switch = driver.switch_to.alert
alert_switch.send_keys("Hi There Man.")
print(alert_switch.text)
alert_switch.accept()

home = driver.find_element(By.XPATH, "//div[@class = 'container']/div[2]/ul[1]/li[2]/a")
home.click()

firstName = driver.find_element(By.XPATH, "//input[@type = 'text' and @placeholder = 'First Name']")
firstName.send_keys("Ravikanth")

lastName = driver.find_element(By.XPATH, "//input[@type = 'text' and @placeholder = 'Last Name']")
lastName.send_keys("Chavan")

address = driver.find_element(By.XPATH, "//div[@class = 'form-group']/div/textarea")
address.send_keys("Station Tanda Chittapur, Kalburagi, Karnataka 585211")

email = driver.find_element(By.XPATH, "//div[@class = 'form-group']/div/input[@type = 'email']")
email.send_keys("ravikanthchavan@gmail.com")

tellephone = driver.find_element(By.XPATH, "//div[@class = 'form-group']/div/input[@type = 'tel']")
tellephone.send_keys("8095063864")

gender = driver.find_element(By.XPATH, "//div[@class = 'form-group']/div/label/input[@type = 'radio' and @value = 'Male']")
gender.click()

hobbies = driver.find_elements(By.XPATH, "//div[@class = 'col-md-4 col-xs-4 col-sm-4']/div/input")
print("Number of CheckBoxes are :", len(hobbies))
# for i in range(len(hobbies)) :
#     hobbies[i].click()
#     time.sleep(1)
for i in range(len(hobbies)):
    hobbies[i].click()

lang = driver.find_element(By.XPATH, "//div[@id = 'msdd']")
lang.click()

driver.execute_script("window.scrollBy(0, 200)")
value = driver.execute_script("return window.pageYOffset;")
print("Number of Pixels Scrolled is :", value)

multi_lang = driver.find_elements(By.XPATH, "//div[@class = 'form-group']/div/multi-select/div[2]/ul/li/a")
print("Number of Languages are :", len(multi_lang))
for langs in multi_lang:
    print(langs.text)
    if langs.text == "Hindi":
        langs.click()

skills = driver.find_elements(By.XPATH, "//div[@class = 'col-md-4 col-xs-4 col-sm-4']/select[@id = 'Skills']/option")
print("Number of Skills there are is :", len(skills))        

for skill in skills :
    print(skill.text)
    
drp_skill = driver.find_element(By.XPATH, "//*[@id='Skills']")
try :
    skills_chosen = Select(drp_skill)
    skills_chosen.select_by_visible_text("Windows")
    time.sleep(5)

except Exception as e:
    print("Error is Occured at {e}")    

country_len = driver.find_elements(By.XPATH, "//select[@id='countries']/option")
print("Number of Countries :", len(country_len))


ctr_drp = driver.find_element(By.XPATH, "//span[@role = 'presentation']")
ctr_drp.click()

drp_down = driver.find_elements(By.XPATH, "//span[@role = 'presentation']/ancestor::span/ancestor::span/ancestor::div[1]/select/option")
print(len(drp_down))

for country in drp_down:
    print(country.text)
    try :
        if country.text == "India" :
            country.click()
            break            
    except Exception as e:
        print("Error is {e}")    

years_drp_down = driver.find_elements(By.XPATH, "//select[@id = 'yearbox']/option")
print("Number of List of Years is :", len(years_drp_down))
for year in  years_drp_down:
    print(year.text)
    if year.text == "2000" :
        year.click()
        break
    else:
        print("Error")

months_drp_down = driver.find_elements(By.XPATH, "//select[@placeholder = 'Month']/option")
print("Number of Months Present in the DropDown is :", len(months_drp_down))
for months in months_drp_down:
    print(months.text)
    if months.text == "March" :
        months.click()
        break 
    else:
        print("Error")  
    
day_drp_down = driver.find_elements(By.XPATH, "//select[@id = 'daybox']/option")
print("Number of Days in a Month :", len(day_drp_down))
for days in day_drp_down:
    print(days.text)
    if days.text == "29":
        days.click()
        break       

driver.execute_script("window.scrollBy(200, 300)")
value_2 = driver.execute_script("return window.pageYOffset;")
print("Page Scrolled by Pixel is :", value_2)
time.sleep(3)

passwd = driver.find_element(By.XPATH, "//input[@id = 'firstpassword']")
passwd.send_keys("ravi12345")

con_pass = driver.find_element(By.XPATH, "//input[@id = 'secondpassword']")
con_pass.send_keys("ravi12345")

button_id = driver.find_element(By.XPATH, "//button[@id = 'submitbtn']")
button_id.click()

driver.back()
time.sleep(3)

all_links = driver.find_elements(By.XPATH, "//div[@class = 'container']/div[2]/ul/li/a")
print("Number of home links are  :", len(all_links))
count = 0
for link in all_links:
    url = link.get_attribute('href')
    try :
        res = requests.head(url)
        if res.status_code>=400:
            print(url, ": is a Broken Link.")
            count += 1
        else:
            print(url, ": Is a Valid Link.")

    except Exception as e:
        print("Error is :{e}")
        count += 1           
try :
    driver.get("https://ravikanth : ravikanth@the-internet.herokuapp.com/basic_auth")
except Exception as e:
    print(e)

driver.back()
time.sleep(5)
