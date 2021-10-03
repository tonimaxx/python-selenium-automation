from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then

OPTION_BUTTONS = (By.XPATH, "//button[@class='a-button-text']")
COLOR_OPTIONS = (By.XPATH, "//div[@id='variation_color_name']//li")
COLOR_SELECTION = (By.XPATH, "//span[@class='selection']")

@given('Open Amazon product page {product_page}')
def open_amazon_product(context, product_page):
    target_url = 'https://www.amazon.com/'+product_page
    context.driver.get(target_url)


@then('Expected color options are displayed {options_seperated_by_comma}')
def click_cart(context, options_seperated_by_comma) :
    element = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable(OPTION_BUTTONS), message='Option buttons not found'
    )

    options = options_seperated_by_comma.split(",")
    i = 0
    for n in options:
        options[i] = n.strip()
        i += 1

    colors = context.driver.find_elements(*COLOR_OPTIONS)

    i = 0
    for color in colors:
        color.click()
        this_selection = context.driver.find_elements(*COLOR_SELECTION)
        print(this_selection[0].text)
        assert this_selection[0].text == options[i], f"{options[i]} not found"
        i += 1

    print("All color options found, and clickable.")