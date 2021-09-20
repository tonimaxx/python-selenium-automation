from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# init Search
keyword = 'Cancel orders'
expectText = 'Cancel Items or Orders'
targetURL = 'https://www.amazon.com/gp/help/customer/display.html'

# init driver
driver = webdriver.Chrome()
driver.maximize_window()

# open the url
driver.get(targetURL)

search = driver.find_element(By.ID, 'helpsearch')
search.clear()
search.send_keys(keyword)
search.send_keys(Keys.RETURN)

# wait for 4 sec
sleep(4)

# at TargetURL
targetXpath = "//h1[contains(text(), '"+expectText+"')]"
search = driver.find_elements_by_xpath(targetXpath)

# verify if we can find a result in list (list is not empty)
isFound = False if len(search) < 1 else True

print('Test Passed' if isFound else expectText+' not found')

driver.quit()