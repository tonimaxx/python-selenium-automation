from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.common.keys import Keys

# init Search
expect_text = 'Cancel Items or Orders'
target_url = 'https://www.amazon.com/gp/help/customer/display.html'

@given('Open Amazon help page')
def open_amazon_help(context):
    context.driver.get(target_url)

@when('Search for {search_keyword}')
def search_for_keyword(context, search_keyword):
    search = context.driver.find_element(By.ID, 'helpsearch')
    search.clear()
    search.send_keys(search_keyword)
    search.send_keys(Keys.RETURN)
    sleep(4)

@then('{search_keyword} is shown')
def verify_found_result_text(context, search_keyword):
    # at target_url
    target_xpath = "//h1[contains(text(), '"+expect_text+"')]"
    search = context.driver.find_elements_by_xpath(target_xpath)

    # verify if we can find a result in list (list is not empty)
    is_found = False if len(search) < 1 else True

    assert is_found, f"Expected text '{expect_text}' not found"
