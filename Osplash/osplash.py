#describe the methods that we are going to call 

from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys
import time
import Osplash.constants as const
import os
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.action_chains import ActionChains

#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.firefox.options import Options
#from selenium.webdriver.support import expected_conditions as EC


class Osplash(webdriver.Firefox):
    def __init__(self, driver_path=r"C:\Users\xcommerce services\Desktop\Folder\Selenium\geckodriver"):
        self.driver_path=driver_path
        #LENOVO
        #super(Osplash,self).__init__()

        #DELL
        self.firefox_binary=FirefoxBinary(r"C:\Program Files\Mozilla Firefox\firefox.exe")
        super(Osplash, self).__init__(firefox_binary=self.firefox_binary)
        
        os.environ['PATH'] += self.driver_path

        self.implicitly_wait(3)
        self.maximize_window()
        
    def __exit__(self, exc_type, exc_val, exc_tb): #ends the session after the actions are done
        time.sleep(5)
        self.quit() 
    
    def land_first_page(self):
        self.get(const.BASE_URL)

    def login(self, id=None, psw=None):
        login = self.find_element(By.CSS_SELECTOR, ".user-info > a:nth-child(1) > span:nth-child(2)")
        login.click()
        try:
            email = self.find_element(By.CSS_SELECTOR, "input[type='email']") 
            password = self.find_element(By.CSS_SELECTOR, "input[type='password']" )
            sign_in = self.find_element(By.ID, 'submit-login')
            email.clear()
            email.send_keys(id)
            password.send_keys(psw)
            time.sleep(2)
            sign_in.click()
            time.sleep(2)
            if self.current_url == "https://www.osplash.eu/my-account": #if login was successful
                print(f"Successul sign in with the credentials: email - {id}, password - {psw}")
            else:
                print(f"Failed to login with: email-{id}, password-{psw}")
        except:
            print(f"Unable to input login data.")

    def logout(self):
        my_account = self.find_element(By.CSS_SELECTOR, ".user-info > a:nth-child(1) > span:nth-child(2)") 
        my_account.click()
        if self.current_url == "https://www.osplash.eu/order-history":
            my_account = self.find_element(By.CSS_SELECTOR, ".account > span:nth-child(2)")
            my_account.click()
            sign_out= self.find_element(By.CSS_SELECTOR, "div.text-xs-center:nth-child(1) > a:nth-child(1)")
            sign_out.click()
        elif self.current_url == "https://www.osplash.eu/login?back=my-account":
            print("You are signed out!")

    def forgot_password(self, email=None):
        login = self.find_element(By.CSS_SELECTOR, ".user-info > a:nth-child(1) > span:nth-child(2)")
        login.click()
        forgot_psw= self.find_element(By.CLASS_NAME, "forgot-password")
        forgot_psw.click()
        mail=self.find_element(By.ID, "email")
        mail.clear()
        mail.send_keys(email)
        self.find_element(By.NAME, "submit").click()
        time.sleep(2)
        try:
            self.find_element(By.NAME, "submit")
            print(f"Unsuccessful for email: {email}")
        except:
            print("Success!")

    def sign_up(self, account_type=None, company_name=None, vat=None, social_title=None, first_name=None, last_name=None, language=None, email=None, password=None, newsletter=None):
        login = self.find_element(By.CSS_SELECTOR, ".user-info > a:nth-child(1) > span:nth-child(2)")
        login.click()
        sign_up = self.find_element(By.CLASS_NAME, "no-account")
        sign_up.click()

        business=self.find_element(By.XPATH, "//input[@name='is_company' and @value='1']")
        mr=self.find_element(By.XPATH, "//input[@name='id_gender' and @value='1']")
        mrs=self.find_element(By.XPATH, "//input[@name='id_gender'and @value='2']")
        f_name= self.find_element(By.NAME, "firstname")
        l_name=self.find_element(By.NAME, "lastname")
        mail=self.find_element(By.XPATH, "//input[@type='email']")
        psw=self.find_element(By.XPATH, "//input[@type='password']")
        check_box_terms=self.find_element(By.XPATH, "//input[@name='psgdpr' and @value='1']")
        check_box_newsletter=self.find_element(By.XPATH, "//input[@name='newsletter' and @value='1']")
        save=self.find_element(By.XPATH, "//button[@data-link-action='save-customer']")
        
        if account_type == "business":
            business.click()
            vat_nr= self.find_element(By.XPATH, "//input[@name='siret']")
            vat_nr.send_keys(vat)
            company = self.find_element(By.XPATH, "//input[@name='company']")
            company.send_keys(company_name)
        #else: #it is already selected, but if you need the path to the personal account button, here it is
            #personal=self.find_element(By.XPATH, "//input[@name='is_company' and @value='0']")
            #personal.click()


        if social_title == "mr":
            mr.click()
        else: 
            mrs.click()

        f_name.send_keys(first_name)
        l_name.send_keys(last_name)

        if language == "english":
            choose_language=self.find_element(By.XPATH, "//select[@name='id_communication_lang']/option[@value='1']")
            choose_language.click()
        elif language == "nederlands":
            choose_language=self.find_element(By.XPATH, "//select[@name='id_communication_lang']/option[@value='3']")
            choose_language.click()
        elif language == "francais":
            choose_language=self.find_element(By.XPATH, "//select[@name='id_communication_lang']/option[@value='4']")
            choose_language.click()
        elif language == "espanol":
            choose_language=self.find_element(By.XPATH, "//select[@name='id_communication_lang']/option[@value='5']")
            choose_language.click()
        elif language == "deutch":
            choose_language=self.find_element(By.XPATH, "//select[@name='id_communication_lang']/option[@value='6']")
            choose_language.click()
        elif language == "italiano":
            choose_language=self.find_element(By.XPATH, "//select[@name='id_communication_lang']/option[@value='7']")
            choose_language.click()
        else:
            print(f"Could not select language: {language}.")
        
        mail.send_keys(email)
        psw.send_keys(password)
        
        check_box_terms.click()

        if newsletter == "no":
            check_box_newsletter.click()

        #save.click()

    def search_product(self, name=None):
        search = self.find_element(By.XPATH, "//input[@placeholder='Search our catalog']")
        search.clear()
        search.send_keys(name)
        send_search=self.find_element(By.CSS_SELECTOR, ".search")
        send_search.click()
        time.sleep(2)
        try:
            no_products_found=self.find_element(By.XPATH, "//section[@id='content']/h4")
            if no_products_found.text == "Sorry for the inconvenience.":
                print(f"No products were found with title {name}.")
            return False
        except:
            return True
    
    def sort_products(self, condition=None): #Popularity, Newest, Name A to Z, Name Z to A, Price low to high, Price high to low
        sort_dropdown= self.find_element(By.XPATH, "//button[@data-toggle='dropdown']")
        sort_dropdown.click()
        select_condition=self.find_element(By.PARTIAL_LINK_TEXT, condition)
        select_condition.click()

    def filter_by(self):
        pass

    def navigate_to_page(self, to=None): #next, previous, or page number

        if str(to).lower() == "next":
            try:
                self.find_element(By.XPATH, "//ul[@class='page-list clearfix text-xs-center text-md-right']/li/a[@class='next js-search-link']").click()
            except:
                print("Next page is not available. You are already on the last page.")
        
        elif str(to).lower() == "previous":
            try:
                self.find_element(By.XPATH, "//ul[@class='page-list clearfix text-xs-center text-md-right']/li/a[@class='previous js-search-link']").click()
            except:
                print("Previous page not available. You are already on the first page.")
        
        else:
            try:
                self.find_element(By.XPATH, f".//a[@class='js-search-link' and contains(text(), '{to}')]").click()
            except:
                print(f"Could not navigate to page {to}.")

    def get_products_in_page(self): #creates a file with the titles and prices of all the products in a page
        if os.path.exists("Products.txt"):
            os.remove("Products.txt")
        with open("Products.txt", "a") as f:
            products= self.find_elements(By.XPATH, "//article[@class='col-xs-6 col-sm-6 col-md-6 col-lg-4 col-xxl-3 product-miniature js-product-miniature']")
            for prod in products:
                f.write(prod.find_element(By.CLASS_NAME, "tooltipGeneral").get_attribute("title") + " - ")
                f.write(prod.find_element(By.CLASS_NAME, "price").get_attribute("textContent"))
                f.write("\n")
    
    def click_on_product(self, number=None): #after a search is done, click on the x'th product (number= x; 1-first product)
        try:
            product=self.find_elements(By.XPATH, "//article[@class='col-xs-6 col-sm-6 col-md-6 col-lg-4 col-xxl-3 product-miniature js-product-miniature']")
            product[int(number)-1].click()
        except:
            nr_of_products= self.find_element(By.XPATH, "//div[@id='js-product-list-top']/div[@class='col-md-6 hidden-sm-down total-products']/p").text
            nr_of_products= nr_of_products.split()
            if int(nr_of_products[2]) < number:
                print(f"You searched for product number {number}, but there are only {nr_of_products[2]} products found. Please enter a number between this range.")
            else:
                page_number= int(number/29) + 1
                self.navigate_to_page(page_number)
                time.sleep(3)
                nr= number - ((page_number-1)*28)
                self.click_on_product(nr)

    def add_to_cart(self, quantity=None): #adds a product in cart with given quantity, then presses "Continue shopping" button
        increase_quantity=self.find_element(By.XPATH, "//button[@class='btn btn-touchspin js-touchspin bootstrap-touchspin-up']")
        for _ in range(quantity - 1):
            increase_quantity.click()

        try:
            add_to_cart = self.find_element(By.XPATH, "//button[@id='add_to_cart']")
            add_to_cart.click()
            time.sleep(3)

            continue_shopping = self.find_element(By.XPATH, "//button[@class='btn btn-secondary']")
            continue_shopping.click()
            # go_to_cart = self.find_element(By.XPATH, "//div[@class='cart-content-btn']/a[@class='btn btn-primary']")
            # go_to_cart.click()
        except:
            product_reference=self.find_element(By.XPATH, "//div[@id='product-details']/div[@class='product-reference']/span")
            print(f"Could not add the product with reference {product_reference.text} in cart. Please check if it's in stock.")

    def method():
        pass
##################################################################################################################################################

    def subscribe_to_newsletter(self, email=None):
        newsletter = self.find_element(By.ID, "email_field")
        newsletter.send_keys(email)
        
        check_box = self.find_element(By.ID, "psgdpr_consent_checkbox_104")
        check_box.click()

        subscribe = self.find_element(By.NAME, "submitNewsletter")
        subscribe.click()
    
    
