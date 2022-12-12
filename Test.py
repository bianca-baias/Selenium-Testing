from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By  # Set of locators strategies
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

options = Options() #Firefox is installed in a custom location and in this case you need to pass the absolute path of the Firefox binary
options.binary_location = r"C:\Program Files\Mozilla Firefox\firefox.exe"

driver = webdriver.Firefox(executable_path= r"C:\Users\xcommerce services\Desktop\Folder\Selenium\geckodriver", options=options)  # path to the browser driver
 
driver.implicitly_wait(10) #waits max x seconds for an action to be done. After this it raises an error
 
driver.maximize_window() #make full-screen
 
driver.get("https://www.osplash.eu") # link of the website to test
 
 #driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") #scroll at the bottom of a page

# test_element = driver.find_element(By.LINK_TEXT, "CLEANING EQUIPMENT") # find link in page by text and atribute it to an object
# test_element.click()  # click on the link
 
time.sleep(2)
 
# banner = driver.find_element(By.XPATH, '//a[@href="/module/spareparts/mainPage"]') #find element by anchor
# banner.click()

#############################################################################################################
#newsletter subscription

# newsletter = driver.find_element(By.ID, "email_field")
# newsletter.send_keys("bianca@xcommerce.eu")

# check_box = driver.find_element(By.ID, "psgdpr_consent_checkbox_104")
# check_box.click()

# subscribe = driver.find_element(By.NAME, "submitNewsletter")
# subscribe.click()

# time.sleep(3)

#############################################################################################################
#search a product
search = driver.find_element(By.XPATH, "/html/body/main/header/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/form/input[2]")
search.send_keys("chlorine")
send_search = driver.find_element(By.XPATH, "/html/body/main/header/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/form/button/i")
send_search.click()

time.sleep(2)

#############################################################################################################
#click on a product
desired_product = driver.find_element(By.XPATH, "/html/body/main/section/div/div[3]/section/section/div[3]/div/div[1]/article[1]")
desired_product.click()
time.sleep(2)

#############################################################################################################
#add to cart
add_to_cart = driver.find_element(By.XPATH, "//*[@id='add_to_cart']")
add_to_cart.click()
time.sleep(3)
go_to_cart = driver.find_element(By.XPATH, "/html/body/div[5]/div/div/div[2]/div/div[2]/div/div/a")
go_to_cart.click()

#############################################################################################################
#driver.back()

# login = driver.find_element(By.CLASS_NAME, "user-info")
# login.click()
 
# time.sleep(15)
# driver.find_element(By.ID, 'buttons.icon_button').click()
 
# email=driver.find_element(By.NAME, 'email')  
# email.click()
# email.send_keys("bianca@xcommerce.eu")
 
# password = driver.find_element(By.NAME, 'password')
# #password.click()
# password.send_keys('123456')
 
# sign_in = driver.find_element(By.ID, 'submit-login')
 
# time.sleep(5)
# sign_in.click()
 
 
 
# second_element = driver.find_element(By.ID, "_desktop_logo")
# second_element.click()
 
 
# driver.back()
