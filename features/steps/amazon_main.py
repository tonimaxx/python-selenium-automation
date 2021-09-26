from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

CART_ICON_LINK = (By.ID, "nav-cart")
FLYOUT_SIGNIN_BUTTON = (By.XPATH, "//a[@data-nav-ref='nav_custrec_signin']")


@given('Open Amazon main page')
def open_amazon_main(context):
    context.driver.get('https://www.amazon.com/')

@when('Click on cart icon')
def click_cart(context):
    context.driver.find_element(*CART_ICON_LINK).click()
    sleep(4)

