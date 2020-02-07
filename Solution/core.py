from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()

browser.get('https://www.allegiantair.com')

assert 'Allegiant' in browser.title



browser.quit()
