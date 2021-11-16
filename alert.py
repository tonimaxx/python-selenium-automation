from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from time import sleep

# init driver
driver = webdriver.Chrome()
driver.implicitly_wait(4)

# open the url
driver.get('https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_alert')

# Switch to iframe
driver.switch_to.frame('iframeResult')

# Click Try it btn
driver.find_element(By.XPATH, "//button[text()='Try it']").click()
sleep(2)

# Alert => click OK
Alert(driver).accept()
sleep(2)

driver.quit()
