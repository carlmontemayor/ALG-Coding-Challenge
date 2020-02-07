# Include unit testing module
import unittest

# Import module to test
from CheckPrice.CheckPrice import CheckPrice


class TestCheckPrice(unittest.TestCase): 
    def setup(self):
        """
        Set up the browser, with Options and additional specifications
        """
        
        #Instantiate CheckPrice class


                

        
    def test_hello(self):
       """
       Test the priceSayHello() function
       """ 
       # Correct hello statement
       correctHello = "Hello from CheckPrice"

       # Instantiate CheckPrice object and ascertain result
       testCheckPrice = CheckPrice()
       result = testCheckPrice.priceSayHello()

       # Test equality
       self.assertEqual(result, correctHello)

if __name__ == "__main__":
    unittest.main()
