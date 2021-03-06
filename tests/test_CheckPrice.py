# Include unit testing module
import unittest

# Import Selenium
from selenium.webdriver.chrome.options import Options

# Import module to test
from CheckPrice.CheckPrice import CheckPrice

# Import logging module
import logging

# Import other modules
from time import sleep

# Logging setup/configuration
logging.basicConfig(filename='unittesting.log',
                    format='%(asctime)s %(message)s',
                    filemode='w')

# Instantiate logger
logger = logging.getLogger()

# Set to DEBUG
logger.setLevel(logging.DEBUG)

class TestCheckPrice(unittest.TestCase): 
    def setUp(self):
        """
        Set up the browser, with Options and additional specifications
        """
        # Create browser options 
        self.options = Options()
        self.options.add_argument('--headless')
         
        # Instantiate CheckPrice object
        self.testCheckPrice = CheckPrice(self.options)

        logger.info("CheckPrice instantiated. Automation started")

    def test_initializedBrowser(self):
        """
        Tests the browser to ensure that we are on the correct website
        """
        # Get correct name of website
        correctUrl = 'https://www.allegiantair.com/'

        res = self.testCheckPrice.checkBrowser()

        self.assertEqual(correctUrl, res, 
                         "connection not established: expected value {" 
                         + correctUrl + '} ' + "actual value {" + res + "}") 

        if res:
            logger.info('Connected. Established connection with ' + correctUrl)
        else:
            logger.warning('Error with connection to ' + correctUrl)


    def test_01_submitTravelForm(self):
        """
        Test the submitTravelForm() function. 
        """
        # Call submitTravelForm and extract result
        res = self.testCheckPrice.submitTravelForm()

        # Assert to check if form was submitted
        self.assertTrue(res, "travel form not submitted: expected value {" 
                        + "True" + "} actual value {" + str(res) + "}")

        if res:
            logger.info('Depart/Return flights submitted.')
        else:
            logger.warning('Depart/Return flights not submitted correctly')
  
    def test_02_fillTravelersForm(self):
        """
        Tests the navigation of the fillTravelersForm
        """
        # Had to instantiate and run functions in order for the ordering of tests
        # to make sense when running. 
        self.testCheckPrice = CheckPrice(self.options)
        self.testCheckPrice.submitTravelForm()
        res = self.testCheckPrice.fillTravelersForm()
        self.testCheckPrice.checkData()
        self.testCheckPrice.terminate()
        

        # Assert if result attained is a empty
        self.assertTrue(self.testCheckPrice, "prices are empty: expected\
                        value {" + "True }" + "actual value {" + str(type(res))
                        + "}")

        self.assertIsInstance(self.testCheckPrice.prices, list, "prices are not\
                              a list: expected value {" + "list}" + "actual\
                              value }" + str(type(res)) + "}")

        if res:
            logger.info("finished navigation to travelers")
        else:
            logger.warning("navigation occurred during navigation to travelers page")

    # assert Raises in unittest
    def test_03_checkData(self):
        """
        Asserts that the extracted prices are equal to the final price of 
        the items in both the traveler's page and the flight's page
        For clarification, I assert twice:
            (1) When extract the return and depart prices from the Flights page
                to compare with the final price on the Travelers page 
            (2) When we get to the Travelers page as it shoes the charges and 
                discounts along to check with the final price on the page
        """
        # Had to instantiate and run functions in order for the ordering of tests
        # to make sense when running. 
        self.testCheckPrice = CheckPrice(self.options)
        self.testCheckPrice.submitTravelForm()
        self.testCheckPrice.fillTravelersForm()
        res = self.testCheckPrice.checkData()
        self.testCheckPrice.terminate()

        # Assert that the item's match the final price
         
        # Assert if the functions actually runs/finishes
        self.assertTrue(res, "prices not checked: expected value {"
                        + "True" + "} " + "actual value {" + str(res)
                        + "}")

        # Log the confirmation or error
        if res:
            logger.info("Price checking completed")
        else:
            logger.warning("Price checking not completed")

        # Assertion (1)
        sumOfPrices = self.testCheckPrice.departPrice + self.testCheckPrice.returnPrice
        print(sumOfPrices)
        finalCost = self.testCheckPrice.finalPrice

        res = self.assertEqual(sumOfPrices, finalCost,
                         "prices not equal: expected value {" +  
                         str(finalCost) + "} actual value {"
                         + str(sumOfPrices) + "}")

        # Assertion (2)
        sumOfCosts = sum(self.testCheckPrice.prices)
        
        self.assertEqual(sumOfCosts, finalCost, "prices not equal: expected"
                         + "value {" + str(finalCost) + "} actual value {" +
                         str(sumOfCosts))

        # If exception occurs, test if it is correctly raised
        self.assertRaises(Exception, self.testCheckPrice.checkData(), 
                          str(finalCost))

        

    def test_04_terminate(self):
        """
        Tests the terminate() function
        Will assertTrue() if terminate actually terminates
        the program
        """
        # Terminate program 
        res = self.testCheckPrice.terminate()

        # Assert to check if browser terminates correctly
        self.assertTrue(res, "browser not terminated: expected value {"
                        + "True" + "} " + "actual value {" + str(res) + "}")

        if res:
            logger.info('Browser closed safely')
        else:
            logger.warning('Browser was not closed safely. Check processes and\
                            execution.')

if __name__ == "__main__":
    unittest.main()
