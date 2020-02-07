from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains

#TODO
#   - Finish selecting options on landing page
#   - Submit form
#
#

browser = webdriver.Chrome()

browser.get('https://www.allegiantair.com')

assert 'Allegiant' in browser.title


delEl = 'body > div.ui-dialog.ui-widget.ui-widget-content.ui-corner-all.ui-front.credit-card-overlay-wrapper.dialog-drupal.ui-draggable.ui-resizable > div.ui-dialog-titlebar.ui-widget-header.ui-corner-all.ui-helper-clearfix.ui-draggable-handle > button > span.ui-button-icon-primary.ui-icon.ui-icon-closethick'

delBox = browser.find_element_by_css_selector(delEl).click()

el = '/html/body/div[5]/div/div/div[1]/div[1]/div/div[2]/div[1]/div/div/div[1]/form/div/div[1]/div[1]/div[1]/div/div/div[1]/div/input'

dropDown = browser.find_element_by_xpath(el).click()

actions = ActionChains(browser)
actions.send_keys(Keys.ARROW_DOWN)
actions.send_keys(Keys.ENTER)
actions.perform()

toEl = '/html/body/div[5]/div/div/div[1]/div[1]/div/div[2]/div[1]/div/div/div[1]/form/div/div[1]/div[1]/div[2]/div/div/div[1]/div/input'

dropDown = browser.find_element_by_xpath(toEl).click()

actions = ActionChains(browser)
actions.send_keys(Keys.ARROW_DOWN)
actions.send_keys(Keys.ARROW_DOWN)
actions.send_keys(Keys.ENTER)
actions.perform()



browser.implicitly_wait(100)


browser.close()
browser.quit()
