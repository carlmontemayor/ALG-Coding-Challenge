# Carl Montemayor
# Coding Challenge
# 
# This module is used to check the assertions after making an Allegiant 
# flight booking. The functions located in the class CheckPrice are ran
# in the __main__.py file.
# 
# The CheckPrice object/class runs a script that navigates to the 
# Allegiant Air travel page after making a flight with departing
# and returning dates at a random location and after filling out 
# the forms and continuing, it tests using an assertion 
# whether or not the prices displayed are correct with the final 
# price on the Travelers page.

# Import Selenium Webdriver modules
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Import additional modules
from time import sleep

# Allegiant Landing Page
ALLEGIANT_URL = 'https://www.allegiantair.com/'

class CheckPrice():
    """
    Initialize class variables such as the browser and prices
    """
    def __init__(self, ops = None):
        # Create and initialize Chrome browser
        self.browser = webdriver.Chrome(chrome_options = ops)

        # Head to Allegiant Air web page
        self.browser.get(ALLEGIANT_URL)
        
        # Track prices of flight/package
        self.prices = []

        # Price of departing flight
        self.departPrice = 0.0

        # Price of returning flight
        self.returnPrice = 0.0

        # Keep Allegiant web page
        self.url = self.browser.current_url

        # Final price
        self.finalPrice = 0.0

    """
    Check and ensure that we are on the correct page
    """
    def checkBrowser(self):
        # Return the browsers URL
        return(self.url)
        
    """
    Once at the landing page, fill in the form items to submit a potential
    flight
    """
    def submitTravelForm(self):
        """
        Navigate through any random city, city pairing 
        and get to the Traveler's page.
        """  
        
        # Let animations/page load
        sleep(1)

        # Print notification submitting form
        print("Submitting form...")

        # Let animations/page load
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

        # Click the dropdown menu for the start date city
        fromDropDownOption = self.browser.find_element_by_xpath(fromDropDown).click()

        # Start Actions to select using keyboard
        actions = ActionChains(self.browser)
        actions.send_keys(Keys.ARROW_DOWN)
        actions.send_keys(Keys.ENTER)
        actions.perform()

        # Let animations/page load
        sleep(1)

        # Click the dropdown menu for the return city 
        toDropDown = ('/html/body/div[5]/div/div/div[1]/div[1]/div/div[2]/div'
                      '[1]/div/div/div[1]/form/div/div[1]/div[1]/div[2]/div/d'
                      'iv/div[1]/div/input')

        # Select return city
        toDropDownOption = self.browser.find_element_by_xpath(toDropDown).click()

        # Set actions to set a random flight for return
        actions = ActionChains(self.browser)
        actions.send_keys(Keys.ARROW_DOWN)
        actions.send_keys(Keys.ARROW_DOWN)
        actions.send_keys(Keys.ENTER)
        actions.perform()

        # Let animations/page load
        sleep(1)
        
        # Click button to select depart
        departButtonIdClass = 'datepicker-toggle'
        departButton = self.browser.find_element_by_class_name(departButtonIdClass)
        departButton.click()

        # Let animations/page load
        sleep(1)
 
        monthClickerPath = ('/html/body/div[5]/div/div/div[1]/div[1]/div/div[2]/div[1] \
                             /div/div/div[1]/form/div/div[1]/div[2]/div[1]/div/div/div/ \
                             div[2]/div[1]/a[2]/span')

        monthClicker = self.browser.find_element_by_xpath(monthClickerPath).click()
        monthClicker = self.browser.find_element_by_xpath(monthClickerPath).click()
        monthClicker = self.browser.find_element_by_xpath(monthClickerPath).click()

        sleep(2)

        # Moved month forward to ensure depart/return dates are valid 
        monthChooserXPath = ('/html/body/div[5]/div/div/div[1]/div[1]/div/div[2]/ \
                              div[1]/div/div/div[1]/form/div/div[1]/div[2]/div[1] \
                              /div/div/div/div[2]/div[1]/a[2]/span')

        chooseMonth = self.browser.find_element_by_xpath(monthChooserXPath).click()
        sleep(1)
        chooseMonth = self.browser.find_element_by_xpath(monthChooserXPath).click()
        sleep(1)
        chooseMonth = self.browser.find_element_by_xpath(monthChooserXPath).click()
        sleep(1)

        sleep(1)

        # Locate xpath for date to depart
        departDateXPath = ('/html/body/div[5]/div/div/div[1]/div[1]/div/div[2]'
                           '/div[1]/div/div/div[1]/form/div/div[1]/div[2]/div[1'
                           ']/div/div/div/div[2]/table/tbody/tr[5]/td[2]/a')

        # Select date to depart
        setDateDepart = self.browser.find_element_by_xpath(departDateXPath).click()

        # Let animations/page load
        sleep(1)

        # Find xpath for return button
        returnButtonXPath = ('/html/body/div[5]/div/div/div[1]/div[1]/div/div'
                             '[2]/div[1]/div/div/div[1]/form/div/div[1]/div[2]'
                             '/div[2]/div/div/div/button')

        # Click on return button
        returnButton = self.browser.find_element_by_xpath(returnButtonXPath).click()

        # Let animations/page load
        sleep(1)

        # Select date to return 
        returnDateXPath = ('/html/body/div[5]/div/div/div[1]/div[1]/div/div[2'
                           ']/div[1]/div/div/div[1]/form/div/div[1]/div[2]/di'
                           'v[2]/div/div/div/div[2]/table/tbody/tr[5]/td[6]/a')

        # Click on return date
        setDateReturn = self.browser.find_element_by_xpath(returnDateXPath).click()

        # Let animations/page load
        sleep(1)

        # Filling form, submitting
        submitButtonXPath = ('/html/body/div[5]/div/div/div[1]/div[1]/div/div'
                             '[2]/div[1]/div/div/div[1]/form/div/div[1]/div[4]'
                             '/div/button')
        
        # Submit the travel form
        button = self.browser.find_element_by_xpath(submitButtonXPath).click()

        # If form does submits correctly, return True
        if not button:
            print("Form Submitted!\n")
            return(True)
        else:
            return(False)

    
    """
    After selecting a flight, continue navigating to the traveler's form
    Perform assertion once at the traveler's form
    """
    def fillTravelersForm(self):
        """
        After filling in destination/return forms, complete
        navigate to the Travelers form and check the price.
        """
        # Print navigation notification
        print("Navigating to Travelers...")

        # Let animations/page load
        sleep(5)

        # Delete cookies pop-up
        privacyXPath = '//*[@id="privacy-policy-footer-close"]'
        WebDriverWait(self.browser, 20).until(EC.element_to_be_clickable((By.XPATH, privacyXPath))).click()

        # Let animations/page load
        sleep(5)

        # Locate departing flight price XPath
        departPricesPath = ('/html/body/div[5]/div/div/div/div/div/div/div/div'
                        '/div[1]/div/div[2]/div/div[4]/div/div[5]/div/div/'
                        'div/form/fieldset/div/div/ul/li/label/span[2]/spa'
                        'n/span[3]')

        # Get the departing price
        departPrices = self.browser.find_element_by_xpath(departPricesPath) 

        
        # Filter price
        departPrices = str(departPrices.text).replace('$', '').split() 
        departPrices = departPrices[1]
        departPrices = float(departPrices)

        # Set departing price
        self.departPrice = departPrices 

        # Locate returning flight price
        returnPricesPath = ('/html/body/div[5]/div/div/div/div/div/div/div/di'
                            'v/div[1]/div/div[2]/div/div[5]/div/div[5]/div/di'
                            'v/div/form/fieldset/div/div/ul/li/label/span[2]/'
                            'span/span[3]')

        # Get the departing price
        returnPrices = self.browser.find_element_by_xpath(returnPricesPath) 

        # Filter price
        returnPrices = str(returnPrices.text).replace('$', '').split()[1] 
        returnPrices = float(returnPrices) 

        # Set departing price
        self.returnPrice = returnPrices

        # Click continue
        continueButtonXPath = ('/html/body/div[5]/div/div/div/div/div/div/div'
                               '/div/div[1]/div/div[2]/div/div[6]/div[3]/'
                               'button')

        # Click Continue *Clicking continue until while as the paths are different 
        # and the animations load at different times
        continueButton = self.browser.find_element_by_xpath(continueButtonXPath).click()

        # Let animations/page load
        sleep(6)
        
        # Click continue
        continueButtonClass = 'continue'
        continueButton = self.browser.find_element_by_class_name(continueButtonClass)

        # Let animations/page load
        sleep(5)
  
        # A string to check if we are on the traveler's portion of the form 
        travelerPageCheck = 'allegiant_traveller_form' 

        # Continue to click through the form until we hit the traveler's form
        # This is allowed as the challenge specifications allow for ANY 
        # packages
        while not self.browser.find_elements_by_class_name(travelerPageCheck):
            # Let animations/page load
            sleep(4)    

            # Select button 
            # Refresh as the CSS selector may not be valid. This also doubles as a check
            # to ensure that the script is clicking on the correct button
            continueButton = self.browser.find_element_by_class_name(continueButtonClass)
            
            # Let animations/page load
            sleep(1)
            continueButton.click()

            # Let animations/page load
            sleep(1)
       
        # Extract the prices from the traveler's page

        # Let animations/page load
        sleep(5)

        # Get the XPath to the table
        pricesXPath = '//*[@id="pricing"]/div/table/tbody[1]/tr' 

        # Find the elements in the table and store by the 'td' selector
        pricesAndDiscounts = self.browser.find_elements_by_css_selector('td') 
        
        # Filter subsequent list. First turns the elements inside the list 
        # into a string then takes out any dollar sign($) characters 
        # Lastly, deletes the last element as it is empty
        pricesAndDiscounts = [str(price.text).replace('$', '') for price in pricesAndDiscounts]
        pricesAndDiscounts.pop() 

        # Turn all values in the charges into float values
        charges = [float(prices) for prices in pricesAndDiscounts]
        
        # Sets the final price and prices from the filtered list
        self.finalPrice = charges.pop()
        self.prices = charges

        # Navigating printing done
        print("Navigation done!\n")

        # Return the charges after the function call
        return(charges)

    """
    Conducts two assertions:
      (1) Check if extracted price values from 'Select Flights' page aligns with 
          final price (the check that is shown on the Coding Challenge page)
      (2) Check if extracted price values from the 'Travelers' page is aligns
          with the final price on the 'Travelers' page
    """
    def checkData(self):
      """
      Takes the browser instance as a parameter and returns a True if the 
      assertions are correct
      """
      # Conduct assertion (1)
      try:
          assert self.departPrice + self.returnPrice == self.finalPrice, 'Assertion failed, price from Flights does not match'
          print("Prices Match on the Flights Page!")
          print(str(self.departPrice) + " + " + str(self.returnPrice) + " = " + str(self.finalPrice))
      except:
          raise Exception("final price does not equal return and depart flights")


      # Conduct assertion (2)
      try:
          flightTotal = sum(self.prices)
      
          stringPrice = [str(price) for price in self.prices]
          
          assert flightTotal == self.finalPrice, 'Assertion failed, price from Traveler\'s page does not match'

          print("\nPrices match on the Travelers Page!")

          # Unpacking operator in python is not available in version 2.7
          print(stringPrice[0] + " + " + stringPrice[1] + " + " + stringPrice[2] + " = " + str(self.finalPrice))
      except:
          raise Exception("final price does not equal return and depart flights")

      

      return True

    """
    After the assertions, close the browser and kill the browser process
    """
    def terminate(self):
        """
        Closes the browser after successful completion and quits the browser.
        """
        # Termination message
        print("\nTerminating browser...")

        # Terminates the browsers after test
        self.browser.close()
        self.browser.quit()

        # Terminated message
        print("Browser terminated.")

        return True

