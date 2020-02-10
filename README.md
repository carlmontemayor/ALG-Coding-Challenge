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
327       # Conduct assertion (1)
328       try:
329           assert self.departPrice + self.returnPrice == self.finalPrice, 'Assertion failed, price from Flights does not match'
330           print("Prices Match on the Flights Page!")
331           print(str(self.departPrice) + " + " + str(self.returnPrice) + " = " + str(self.finalPrice))
332       except:
333           raise Exception("final price does not equal return and depart flights")
```

In Module CheckPrice.py 337: 349
```
336       # Conduct assertion (2)
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

In UnitTest test_CheckPrice.py 135: 143
```
135         # Assertion (1)
136         sumOfPrices = self.testCheckPrice.departPrice + self.testCheckPrice.returnPrice
137         print(sumOfPrices)
138         finalCost = self.testCheckPrice.finalPrice
139 
140         res = self.assertEqual(sumOfPrices, finalCost,
141                          "prices not equal: expected value {" +
142                          str(finalCost) + "} actual value {"
143                          + str(sumOfPrices) + "}")
```

In UnitTest test_CheckPrice.py 145: 154
```
145         # Assertion (2)
146         sumOfCosts = sum(self.testCheckPrice.prices)
147 
148         self.assertEqual(sumOfCosts, finalCost, "prices not equal: expected"
149                          + "value {" + str(finalCost) + "} actual value {" +
150                          str(sumOfCosts))
151 
152         # If exception occurs, test if it is correctly raised
153         self.assertRaises(Exception, self.testCheckPrice.checkData(), 
154                           str(finalCost))
```

## Installation

Install the module by cloning the repository:
```
git clone git@github.com:carlmontemayor/ALG-Coding-Challenge.git
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

## Note on running
The program and thee uunittests run as is after cloning the repository, however, there may be some problems that occur
that have to do with how the HTML/CSS elements are rendered. Just to ensure, the program should be ran
at least twice to make sure this isn't the case.

## Technology Used
Languages: Python\
Frameworks: unittest (from Python) and Selenium\
Browser: Google Chrome
