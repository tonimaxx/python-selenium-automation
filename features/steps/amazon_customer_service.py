from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.common.keys import Keys

# Init Variables
target_url = 'https://www.amazon.com/gp/help/customer/display.html'
UI_ELEMENTS = {
    "title text": "//div[contains(@class,'a-section')]//h1",
    "main container": "//div[@class='a-section a-spacing-large ss-landing-container-wide']",
    "search input": "//input[@id='helpsearch']",
    "help text": "//div[@class='help-content csg']//h1",
    "support container": "//div[@id='csg-support-topics']",
    "promo image": "//img[@class='csg-hb-promo']"
}


@when('Open Amazon customer service page')
def open_amazon_help(context):
    context.driver.get(target_url)


@then('UI Element {ui_element} is founded')
def search_for_ui(context, ui_element):
    search = context.driver.find_elements_by_xpath(UI_ELEMENTS[ui_element.lower()])
    assert len(search)>0, f"{ui_element} not founded!"