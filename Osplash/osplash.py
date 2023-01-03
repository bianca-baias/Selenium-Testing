#describe the methods that we are going to call 

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import Osplash.constants as const
import os
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

class Osplash(webdriver.Firefox):
    def __init__(self, driver_path=r"C:\Users\xcommerce services\Desktop\Folder\Selenium\geckodriver"):
        self.driver_path=driver_path
        super(Osplash,self).__init__() #lenovo
        #DELL
        #self.firefox_binary=FirefoxBinary(r"C:\Program Files\Mozilla Firefox\firefox.exe")
        #super(Osplash, self).__init__(firefox_binary=self.firefox_binary)
        os.environ['PATH'] += self.driver_path

        self.implicitly_wait(10)
        self.maximize_window()
        
    def __exit__(self, exc_type, exc_val, exc_tb): #ends the session after the actions are done
        time.sleep(10)
        self.quit() 
    
    def land_first_page(self):
        self.get(const.BASE_URL)
    
    def click_on_banner(self):
        banner = self.find_element(By.XPATH, '//a[@href="/module/spareparts/mainPage"]')
        banner.click()
    
    def newsletter_subscribe(self):
        newsletter = self.find_element(By.ID, "email_field")
        newsletter.send_keys("bianca@xcommerce.eu")
        
        check_box = self.find_element(By.ID, "psgdpr_consent_checkbox_104")
        check_box.click()

        subscribe = self.find_element(By.NAME, "submitNewsletter")
        subscribe.click()
    
    def search_product(self):
        search = self.find_element(By.CSS_SELECTOR, "input[placeholder]='Search our catalog")
        #search = self.find_element(By.XPATH, "//input[@placeholder='Search our catalog']")
        search.send_keys("chlorine")
        send_search=self.find_element(By.CSS_SELECTOR, ".search")
        send_search.click()

    def click_on_product(self):
        desired_product = self.find_element(By.XPATH, "/html/body/main/section/div/div[3]/section/section/div[3]/div/div[1]/article[1]")
        desired_product.click()
    
    def add_to_cart(self):
        add_to_cart = self.find_element(By.XPATH, "//*[@id='add_to_cart']")
        add_to_cart.click()
        time.sleep(3)

        go_to_cart = self.find_element(By.CSS_SELECTOR, ".cart-content-btn > a:nth-child(2)")
        go_to_cart.click()

        # continue_shopping = self.find_element(By.CSS_SELECTOR,".cart-content-btn > button:nth-child(1)")
        # continue_shopping.click()

    def login(self):
        id_password= [['', ''], ["", "123456"], ["bianca@xcom", ''], ["bianca@xcom.eu", "12300"], ["bianca", "123456"], ["bianca@xcommerce.eu", "123444"], ["bianca@xcommerce.eu", "123456"]]
        login = self.find_element(By.XPATH, "/html/body/main/header/nav/div/div/div[1]/div[2]/div[1]/div/a/span")
        login.click()

        for pair in id_password:
            try:
                email=self.find_element(By.XPATH, '/html/body/main/section/div/div[2]/section/section/section/form/section/div[1]/div/input')  
                password = self.find_element(By.XPATH, '/html/body/main/section/div/div[2]/section/section/section/form/section/div[2]/div/div/input')
                sign_in = self.find_element(By.XPATH, '//*[@id="submit-login"]')
                email.send_keys(Keys.CONTROL + "a")
                email.send_keys(Keys.DELETE)
                email.send_keys(pair[0])
                password.send_keys(pair[1])
                time.sleep(2)
                sign_in.click()
                time.sleep(2)
                if self.current_url == "https://www.osplash.eu/my-account": #if login was successful
                    print(f"Successul sign in with the credentials: email - {pair[0]}, password - {pair[1]}")
                    break
            except:
                print(f"Could not input the following data: {pair}")
