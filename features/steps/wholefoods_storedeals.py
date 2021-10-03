from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then

IS_DEBUG_MODE = True

PRODUCT_NAME = (By.CSS_SELECTOR, "li.s-result-item span.a-size-medium.wfm-sales-item-card__product-name.a-text-bold")
REGULAR_PRICE = (By.CSS_SELECTOR, "li.s-result-item span.a-size-small.a-color-tertiary.wfm-sales-item-card__regular-price")

@given('Open Whole Foods Store Deals')
def open_amazon_product(context):
    target_url = 'https://www.amazon.com/wholefoodsdeals'
    context.driver.get(target_url)


@then('Every product has text Regular and Product name')
def verify_products_detail(context):

    element = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located(REGULAR_PRICE), message='A Regular price element not found')

    product_name = context.driver.find_elements(*PRODUCT_NAME)
    regular_text = context.driver.find_elements(*REGULAR_PRICE)

    i = 0
    for product in product_name:
        this_product = product_name[i].text
        this_regular = regular_text[i].text
        if IS_DEBUG_MODE: print(f"Debug > {i}, {this_product}, {this_regular}")
        assert len(this_product) > 0, f"Can"
        assert len(product_name) == len(regular_text), f"Product#{i} name is Empty!"
        assert "Regular" in this_regular, f"Product#{i} not has text Regular"
        i += 1
