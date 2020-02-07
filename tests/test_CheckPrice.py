# Include unit testing module
import unittest

# Import module to test
from CheckPrice.CheckPrice import CheckPrice


class TestCheckPrice(unittest.TestCase): 
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
