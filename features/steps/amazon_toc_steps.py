from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then

IS_DEBUG_MODE = True

PRODUCT_NAME = (By.CSS_SELECTOR, "li.s-result-item span.a-size-medium.wfm-sales-item-card__product-name.a-text-bold")
REGULAR_PRICE = (By.CSS_SELECTOR, "li.s-result-item span.a-size-small.a-color-tertiary.wfm-sales-item-card__regular-price")
PRIVACY_PAGE_LINK = (By.XPATH, "//a[@href='https://www.amazon.com/privacy']")
PRIVACY_PAGE_TITLE = (By.XPATH, "//h1[text()='Amazon.com Privacy Notice']")
ORIGINAL_PAGE_TITLE = (By.XPATH, "//h1[text()='Conditions of Use']")

@given('Open Amazon T&C page')
def open_amazon_product(context):
    target_url = 'https://www.amazon.com/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088'
    context.driver.get(target_url)


@when('Store original windows')
def store_original_windows(context):
    context.original_window = context.driver.current_window_handle


@when('Click on Amazon Privacy Notice link')
def click_privacy_link(context):
    element = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable(PRIVACY_PAGE_LINK), message='Expected Privacy Notice link is clickable'
    )
    context.driver.find_element(*PRIVACY_PAGE_LINK).click()


@when('Switch to the newly opened window')
def switch_new_window(context):
    all_windows_handles = context.driver.window_handles
    context.driver.switch_to.window(all_windows_handles[1])


@then('Verify Amazon Privacy Notice page is opened')
def verify_privacy_page_opened(context):
    element = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located(PRIVACY_PAGE_TITLE), message='Expected Privacy Notice page is displayed'
    )

@then('User can close new window and switch back to original')
def user_close_window_switch_back(context):
    context.driver.close
    context.driver.switch_to.window(context.original_window)
    element = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located(ORIGINAL_PAGE_TITLE), message='Expected Original Amazon T&C page is displayed'
    )