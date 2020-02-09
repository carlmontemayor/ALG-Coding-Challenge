# Allegiant Coding Challenge 

The solution to the coding challenge given that checks to see if the final price of 
one Allegiant flight (round-trip) is equal to the price of all selected items. 

Included is also small unittests to ensure that the program works correctly.

The CheckPrice class included has functionality that tests and checks 2 conditions:
    (1) The prices of selected items from the "Flights" page is equal to the price 
        shown on the "Travelers" page.
    (2) The prices of selected items shown on the "Travel" page is equal to the 
        final price shown.

The distinction between the 2 above assertions is made as I had extracted the prices
from both the "Flights" page and the "Travelers" page. As I wanted to ensure that 
the prices were complete for both pages.

In the screencap below, I extracted prices that are highlighted red for the prices on 
the "Flights" page and blue for the prices in the "Travelers" page. I checked the 
summation of both of the prices with the final price highlighted green. 
   

## Installation

Install the module by cloning the repository:
```
git@github.com:carlmontemayor/AllegaintCodingChallenge.git
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
cd Allegiant\ Coding\ Challenge/ 
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

## Technology Used
Languages: Python
Frameworks: unittest (from Python) and Selenium
Browser: Google Chrome
