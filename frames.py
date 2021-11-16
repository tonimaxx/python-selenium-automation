
from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome()
driver.implicitly_wait(4)

# open the url
driver.get('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_iframe')

# Switch to frame 1
driver.switch_to.frame('iframeResult')

# Switch to frame 2
frame2 = driver.find_element(By.CSS_SELECTOR, "iframe[src='https://www.w3schools.com']")
driver.switch_to.frame(frame2)

logo = driver.find_element(By.CSS_SELECTOR, 'a.w3-bar-item')
print(logo.get_attribute('href'))

assert logo.get_attribute('href') == 'https://www.w3schools.com/', f'Error..'

driver.quit()
