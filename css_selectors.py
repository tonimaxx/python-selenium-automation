from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

# Lesson 3 locator examples:

# ID
driver.find_element(By.CSS_SELECTOR, 'input#twotabsearchtextbox')

# class
driver.find_element(By.CSS_SELECTOR, "span.a-color-state.a-text-bold")

# Full attribute
driver.find_element(By.CSS_SELECTOR, "a[href='/gp/bestsellers/?ref_=nav_cs_bestsellers_8a080d3d7b55497ea1bdd97b7cff8b7b']")

# Partial attribute
driver.find_element(By.CSS_SELECTOR, "a[href*='/gp/bestsellers/?ref_=nav_cs_bestsellers']")

# Travelling through nodes
driver.find_element(By.CSS_SELECTOR, "div#nav-xshop-container div#nav-xshop a")
