from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


SEARCH_INPUT = (By.NAME, 'q')
SEARCH_SUBMIT = (By.NAME, 'btnK')



@given('Open Google page')
def open_google(context):
    context.driver.get('https://www.google.com/')


@when('Input {search_word} into search field')
def input_search(context, search_word):
    search = context.driver.find_element(*SEARCH_INPUT)
    search.clear()
    search.send_keys(search_word)
    sleep(4)


@when('Click on search icon')
def click_search_icon(context):
    context.driver.find_element(*SEARCH_SUBMIT).click()
    sleep(1)


@then('Product results for {search_word} are shown')
def verify_found_results_text(context, search_word):
    assert search_word.lower() in context.driver.current_url.lower(), f"Expected query not in {context.driver.current_url.lower()}"

##--------- Homework #4 from this line

ORDERS_LINK = (By.ID, "nav-orders")

@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')

@when('Click on Orders')
def click_orders(context):
    #context.driver.find_elements_by_xpath("//a[@class='nav-a nav-a-2 nav-progressive-attribute']").click()
    context.driver.find_element(*ORDERS_LINK).click()
    sleep(4)

@then('Sign in page opened')
def verify_signin_page_opened(context):
    assert 'signin' in context.driver.current_url.lower(), f"Expected query not in {context.driver.current_url.lower()}"