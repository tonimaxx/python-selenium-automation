from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@when('Select department {department}')
def select_test_department(context, department):
    context.app.header.select_department(department)


@when('Search product {keyword}')
def search_product(context, keyword):
    context.app.header.execute_search(keyword)


@then("Verify search result page is displayed")
def verify_result_page_displayed(context):
    element = WebDriverWait(context.driver, 10).until(
        EC.url_contains("s?k="), message="Expect search result page, but not found!"
    )