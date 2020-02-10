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
The actual assertion statement that is made is within the checkData() function. The unittests
are there for me to test and make sure that the functions within the CheckPrice class are actually
ran successfully.

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
