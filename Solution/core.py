from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()

browser.get('https://www.allegiantair.com')

assert 'Allegiant' in browser.title

delBox = browser.find_element_by_css_selector("body > div.ui-dialog.ui-widget.ui-widget-content.ui-corner-all.ui-front.credit-card-overlay-wrapper.dialog-drupal.ui-draggable.ui-resizable > div.ui-dialog-titlebar.ui-widget-header.ui-corner-all.ui-helper-clearfix.ui-draggable-handle > button").click()
browser.wait_implicitly(1000)

browser.quit()
