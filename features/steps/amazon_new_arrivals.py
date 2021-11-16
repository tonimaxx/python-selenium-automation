from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

NEW_ARRIVALS_FLYOUT = (By.XPATH, "//div[@id='nav-flyout-anchor']/div[16]")

@given('Go to a product page {product_page}')
def open_product(context, product_page):
    # context.app.header.click_order_link()
    context.app.product_page.open_product_page(product_page)


@when('Hovers over New Arrivals')
def hover_new_arrival(context):
    context.app.product_page.hover_new_arrival()


@then('New Arrivals Flyout appears')
def new_arrivals_flyout_appears(context):
    element = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located(NEW_ARRIVALS_FLYOUT), message="Expect New Arrivals is displayed, but not found!"
    )

