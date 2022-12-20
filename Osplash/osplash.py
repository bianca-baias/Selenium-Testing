#describe the methods that we are going to call 

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By  # Set of locators strategies
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import Osplash.constants as const
import os

class Osplash(webdriver.Firefox):
    def __init__(self, driver_path=r"C:\Users\xcommerce services\Desktop\Folder\Selenium\geckodriver"):
        self.driver_path=driver_path
        super(Osplash, self).__init__()
        os.environ['PATH'] += self.driver_path

    def land_first_page(self):
        self.get(const.BASE_URL)

time.sleep(3)
