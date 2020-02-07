# Carl Montemayor
# Coding Challenge
# 
# This module is used to check the assertions after making an Allegiant 
# booking. 

# TODO
# - Finish top comments
# - Finish commands/submit a flight


# Import Selenium Webdriver modules
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains


# Allegiant Landing Page
ALLEGIANT_URL = 'https://www.allegiantair.com/'

class CheckPrice():
    def __init__(self):
        # Create and initialize Chrome browser
        self.browser = webdriver.Chrome()
        
        # Track prices of flight/package
        self.price = 0.0

    def priceSayHello(self):
        return("Hello from CheckPrice")
    
  
