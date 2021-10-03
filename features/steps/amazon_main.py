from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from behave import given, when, then


CART_ICON_LINK = (By.ID, "nav-cart")
FLYOUT_SIGNIN_BUTTON = (By.XPATH, "//a[@data-nav-ref='nav_custrec_signin']")


@given('Open Amazon main page')
def open_amazon_main(context):
    context.driver.get('https://www.amazon.com/')

@when('Click on cart icon')
def click_cart(context):
    element = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable(CART_ICON_LINK)
    )
    context.driver.find_element(*CART_ICON_LINK).click()

