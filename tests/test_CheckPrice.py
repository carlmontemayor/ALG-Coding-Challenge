# Include unit testing module
import unittest

# Import module to test
from CheckPrice.CheckPrice import CheckPrice

class TestCheckPrice(unittest.TestCase): 
    def setUp(self):
        """
        Set up the browser, with Options and additional specifications
        """
        
        #Instantiate CheckPrice class
        self

    def test_initializedBrowser(self):
        """
        Basic test 
        """
        # Instantiate CheckPrice() object
        testCheckPrice = CheckPrice()

        # Get correct name of website
        correctUrl = 'https://www.allegiantair.com/'
        self.assertEqual(correctUrl, testCheckPrice.checkBrowser()) 

        




    def test_submitTravelForm(self):
        """
        Test the submitTravelForm() function. 
        """

        #Check if on Allegiant travel page
        
        

if __name__ == "__main__":
    unittest.main()
