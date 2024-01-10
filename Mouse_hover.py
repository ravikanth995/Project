from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
import time

ops = webdriver.ChromeOptions()
ops.add_argument("--disable-notifications")
serv_obj = Service("C:\\Users\\Shashikanth\\Desktop\\Selenium\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service= serv_obj, options= ops)

# driver.get("https://www.testim.io/blog/")
# driver.maximize_window()
# driver.implicitly_wait(10)

# def mouse_hover_1():
#     product = driver.find_element(By.XPATH, "//a[text() = 'Products']")
#     act = ActionChains(driver)
#     try :
#         act.move_to_element(product).click().perform()
#         time.sleep(5)
#         auto = driver.find_element(By.XPATH, "//ul[@class = 'drop-nav']/li/a[@class = 'i-link bg-black']")
#         auto.click()
#     except Exception as e:
#         print(e)    

# mouse_hover_1()

# def multi_hover():
#     driver.get("https://www.amazon.in/")
#     driver.maximize_window()
#     driver.implicitly_wait(10)

#     prime = driver.find_element(By.ID, "nav-link-amazonprime")
#     act = ActionChains(driver)
#     act.move_to_element(prime).click().perform()

# multi_hover()

# def right_click():

#     driver.get("https://www.amazon.in/")
#     driver.maximize_window()
#     driver.implicitly_wait(8)
#     click = driver.find_element(By.XPATH, "//a[text() = ' Electronics ']")
#     act = ActionChains(driver)
#     act.context_click(click)

# right_click()

# def double_click():

#     driver.get("https://testautomationpractice.blogspot.com/")
#     driver.maximize_window()
#     driver.implicitly_wait(8)
    
#     try: 
        
#         driver.execute_script("window.scrollBy(0, 400)")
#         page = driver.execute_script("return window.pageYOffset;")
#         print("Number of Pixels Scrolled :", page)

#         field1 = driver.find_element(By.ID, "field1")
#         field1.clear()
#         field1.send_keys("Lalalalalala")

#         btn_double = driver.find_element(By.XPATH, "//button[normalize-space()='Copy Text']")
#         act = ActionChains(driver)
#         act.double_click(btn_double)
#         time.sleep(20)

#     except Exception as e:
#         print("Error took place :", e)
# double_click()

# def drag_drop():
    # driver.get("https://testautomationpractice.blogspot.com/")
    # driver.maximize_window()
    # driver.implicitly_wait(8)

    # driver.execute_script("window.scrollBy(0, 400)")
    # page = driver.execute_script("return window.pageYOffset;")
    # print(f"Number of Pixels scrolled is :", page)
#     source_ele = driver.find_element(By.ID, "draggable")
#     target_ele = driver.find_element(By.ID, "droppable")
#     act = ActionChains(driver)
#     act.drag_and_drop(source_ele, target_ele).perform()
#     time.sleep(5)

# drag_drop()

# def slider():
#     driver.get("https://testautomationpractice.blogspot.com/")
#     driver.maximize_window()
#     driver.implicitly_wait(8)

#     driver.execute_script("window.scrollBy(0, 700)")
#     page = driver.execute_script("return window.pageYOffset;")
#     print(f"Number of Pixels scrolled is :", page)

#     min_slide = driver.find_element(By.XPATH, "//div[@id = 'slider']/span")
#     max_slide = driver.find_element(By.XPATH, "//body//div//span[1]")

#     print(f"Minimum slide is : {min_slide.location}")
#     print(f"Maximum slide is : {max_slide.location}")

#     act = ActionChains(driver)
#     act.drag_and_drop_by_offset(min_slide, 100, 0).perform()
#     act.drag_and_drop_by_offset(max_slide, -40, 0).perform()
#     time.sleep(10)
    
#     print("Location after sliding...")
#     print(f"After Sliding Minimum Location is : {min_slide.location}")
#     print(f"After Maximum sliding is : {max_slide.location}")

# slider()
 
def flipKart():

    driver.get("https://www.flipkart.com/")
    driver.maximize_window()
    driver.implicitly_wait(10)

    search = driver.find_element(By.NAME, "q")
    search.send_keys("Mobile")

    btn_submit = driver.find_element(By.XPATH, "//button[@type= 'submit']")
    btn_submit.click()
    
    min_slide = driver.find_element(By.XPATH, "//div[@class = '_31Kbhn _28DFQy']/div[@class = '_3FdLqY']")
    max_slide = driver.find_element(By.XPATH, "//div[@class = '_31Kbhn WC_zGJ']/div[@class = '_3FdLqY']")

    print(f"Minimum Slide is : {min_slide.location}")
    print(f"Maximum Slide is {max_slide.location}")

    act = ActionChains(driver)
    act.drag_and_drop_by_offset(min_slide, 50, 0).perform()
    act.drag_and_drop_by_offset(max_slide, -54, 0).perform()

    print(f"After Minimum Sliding is {min_slide.location}")
    print(f"After Maximum Sliding is {max_slide}")
    time.sleep(5)

flipKart()
