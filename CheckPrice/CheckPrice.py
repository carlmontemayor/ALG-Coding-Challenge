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

# Import additional modules
from time import sleep


# Allegiant Landing Page
ALLEGIANT_URL = 'https://www.allegiantair.com/'

class CheckPrice():
    def __init__(self):
        # Create and initialize Chrome browser
        self.browser = webdriver.Chrome()

        # Head to Allegiant Air web page
        self.browser.get(ALLEGIANT_URL)
        
        # Track prices of flight/package
        self.price = 0.0

    def priceSayHello(self):
        return("Hello from CheckPrice")
    
    def navigateToTravelers(self):
        """
        Navigate through any random city, city pairing 
        and get to the Traveler's page.
        """  
        # Add assert Allegiant in browser.title to test 

        # Let animations load
        sleep(1)

        # Close initial pop-up
        popUp = ('body > div.ui-dialog.ui-widget.ui-widget-content.ui-corner'
                 '-all.ui-front.credit-card-overlay-wrapper.dialog-drupal.ui'
                 '-draggable.ui-resizable > div.ui-dialog-titlebar.ui-widget'
                 '-header.ui-corner-all.ui-helper-clearfix.ui-draggable-hand'
                 'le > button > span.ui-button-icon-primary.ui-icon.ui-icon-'
                 'closethick')
        
        # Select pop-up and close using 'x'
        self.browser.find_element_by_css_selector(popUp).click()

        # Let pop-up go away
        sleep(1)

        # Start filling out inital destination form
        fromDropDown = ('/html/body/div[5]/div/div/div[1]/div[1]/div/div[2]/d'
                        'iv[1]/div/div/div[1]/form/div/div[1]/div[1]/div[1]/di'
                        'v/div/div[1]/div/input')

        fromDropDownOption = self.browser.find_element_by_xpath(fromDropDown).click()

        # Start Actions to select using keyboard
        actions = ActionChains(self.browser)
        actions.send_keys(Keys.ARROW_DOWN)
        actions.send_keys(Keys.ENTER)
        actions.perform()

        sleep(1)

        toDropDown = ('/html/body/div[5]/div/div/div[1]/div[1]/div/div[2]/div'
                      '[1]/div/div/div[1]/form/div/div[1]/div[1]/div[2]/div/d'
                      'iv/div[1]/div/input')

         
        toDropDownOption = self.browser.find_element_by_xpath(toDropDown).click()

        actions = ActionChains(self.browser)
        actions.send_keys(Keys.ARROW_DOWN)
        actions.send_keys(Keys.ARROW_DOWN)
        actions.send_keys(Keys.ENTER)
        actions.perform()

        sleep(1)
        
        

    def terminate(self):
        self.browser.close()
        self.browser.quit()




