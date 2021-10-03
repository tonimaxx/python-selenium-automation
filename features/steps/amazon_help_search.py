from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from behave import given, when, then

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


@then('{search_keyword} is shown')
def verify_found_result_text(context, search_keyword):

    target_xpath = "//h1[contains(text(), '"+expect_text+"')]"
    element = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, target_xpath))
    )
    search = context.driver.find_elements_by_xpath(target_xpath)
    assert len(search) > 0, f"Expected text '{expect_text}' not found"
