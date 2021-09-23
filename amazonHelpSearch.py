#Homework#2 - Fixed Snake case & AssertionError'

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# init Search
keyword = 'Cancel orders'
expect_text = 'Cancel Items or Orders'
target_url = 'https://www.amazon.com/gp/help/customer/display.html'

# init driver
#driver = webdriver.Chrome(executable_path='/Users/tonimaxx/careerist/python-selenium-automation/chromedriver')
driver = webdriver.Chrome(executable_path='./chromedriver')

driver.maximize_window()

# open the url
driver.get(target_url)

search = driver.find_element(By.ID, 'helpsearch')
search.clear()
search.send_keys(keyword)
search.send_keys(Keys.RETURN)

# wait for 4 sec
sleep(4)

# at target_url
target_xpath = "//h1[contains(text(), '"+expect_text+"')]"
search = driver.find_elements_by_xpath(target_xpath)

# verify if we can find a result in list (list is not empty)
is_found = False if len(search) < 1 else True

assert is_found, f"Expected text '{expect_text}' not found"
print('Test Passed')

driver.quit()