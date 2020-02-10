# Allegiant Coding Challenge 

The solution to the coding challenge given that checks to see if the final price of 
one Allegiant flight (round-trip) is equal to the price of all selected items. 

Included is also small unittests to ensure that the program works correctly.

The CheckPrice class included has functionality that tests and checks 2 conditions:\
    (1) The prices of selected items from the "Flights" page is equal to the price
        shown on the "Travelers" page.  \
    (2) The prices of selected items shown on the "Travel" page is equal to the 
        final price shown.

The distinction between the 2 above assertions is made as I had extracted the prices
from both the "Flights" page and the "Travelers" page. As I wanted to ensure that 
the prices were complete for both pages.

In the screencap below, I extracted prices that are highlighted yellow for the prices on 
the "Flights" page and red for the prices in the "Travelers" page. I checked the 
summation of both of the prices with the final price highlighted green. Essentially what 
I included is a check to make sure that the sum of the prices in Assertion (1) is equal
to the final price located in the green box on the Travelers Page. With Assertion (2), I included
a check to make sure that the prices on the Travelers page is correct.

The prices with in the yellow boxes AND the prices in the red box both equal to the price shown in 
the green box.

### Flights Page 
![Flights Page](https://github.com/carlmontemayor/AllegaintCodingChallenge/blob/master/screenshots%20(referenced%20in%20README.md)/Flights%20Page.png)

### Travelers Page
![Travelers Page](https://github.com/carlmontemayor/AllegaintCodingChallenge/blob/master/screenshots%20(referenced%20in%20README.md)/Traveler's%20Page.png)

### Assertions
The following lines of code are where I actually make the assertions.


In Module CheckPrice.py 328: 333
```                                                                                                        
328       try:
329           assert self.departPrice + self.returnPrice == self.finalPrice, 'Assertion failed, price from Flights does not match'
330           print("Prices Match on the Flights Page!")
331           print(str(self.departPrice) + " + " + str(self.returnPrice) + " = " + str(self.finalPrice))
332       except:
333           raise Exception("final price does not equal return and depart flights")
```

In Module CheckPrice.py 337: 349
```
337       try:
338           flightTotal = sum(self.prices)
339       
340           stringPrice = [str(price) for price in self.prices]
341           
342           assert flightTotal == self.finalPrice, 'Assertion failed, price from Traveler\'s page does not match'
343 
344           print("\nPrices match on the Travelers Page!")
345 
346           # Unpacking operator in python is not available in version 2.7
347           print(stringPrice[0] + " + " + stringPrice[1] + " + " + stringPrice[2] + " = " + str(self.finalPrice))
348       except:
349           raise Exception("final price does not equal return and depart flights")
```

In UnitTest test_CheckPrice.py 90:96
```
 90         self.assertTrue(self.testCheckPrice, "prices are empty: expected\                                                                 
 91                         value {" + "True }" + "actual value {" + str(type(res))
 92                         + "}")
 93 
 94         self.assertIsInstance(self.testCheckPrice.prices, list, "prices are not\
 95                               a list: expected value {" + "list}" + "actual\
 96                               value }" + str(type(res)) + "}")
```

## Installation

Install the module by cloning the repository:
```
git clone git@github.com:carlmontemayor/AllegaintCodingChallenge.git
```

Before using this module, Selenium must also be installed. It can be installed using pip:
```
pip install selenium
```


In addition, the Google Chrome Selenium Driver must also be installed. It can be found here:
```
https://sites.google.com/a/chromium.org/chromedriver/downloads
```

## Running

Once cloned, the program can be run by doing the following within the terminal:
```
cd ALG-Coding-Challenge/
```

Once inside the Coding Challenge directory, run the program by typing:
```
python CheckPrice
```
The above command will run the program and you can see the automation as the browser 
opens.

In addition, I have also created some unittests for this module. You can run these by
typing:
```
python -m unittest discover
```

Once finished, there is a unittesting.log file that can be opened to check functionality.

## Notes on running
At least two runs of the module and unittests should be conducted to ensure that the program runs just to make sure
there aren't any problems with rendering of the HTML/CSS elements.
Although my program runs and it works from the assertions and actually running the program itself, I cannot control
how fast the the HTML/CSS elements are actually rendered on the page. As a result, multiple runs of the program and 
unittests will help as the speeds in which to wait for the rendering of elements may vary.

From my own testing and running of the unittests and actual application, the functionality is completely present and working.

The possible errors that may occur include the following:\
(1) Some of the elements are not clickable because they have not been 
rendered yet by the DOM\
(2) For a similar reason, the pop-up footer that lets the user accept cookies may also not be rendered in time
because it looks like (looking through the Chrome DevTools) that there is a Javascript snippet that prevents the 
click() function from Selenium from registering. I have tried various methods such as using the wait module from 
Selenium to ensure that the element is clickable, but the most secure way that I have found it to work is through 
finding the XPath of the span of the footer which allows me to use the click()

## Technology Used
Languages: Python
Frameworks: unittest (from Python) and Selenium
Browser: Google Chrome
