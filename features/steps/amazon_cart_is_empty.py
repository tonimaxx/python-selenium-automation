from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@then('Cart is empty')
def verify_if_cart_is_empty(context):
    # search for the expect text at the target
    expect_text = "Your Amazon Cart is empty"
    target_xpath = "//h2[contains(text(), '"+expect_text+"')]"
    search = context.driver.find_elements_by_xpath(target_xpath)

    # verify if we can find a result in list (list is not empty)
    is_found = False if len(search) < 1 else True

    assert is_found, f"Expected text '{expect_text}' not found"