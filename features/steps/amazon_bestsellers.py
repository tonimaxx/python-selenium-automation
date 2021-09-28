from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.common.keys import Keys

# Init Variables

target_url = 'https://www.amazon.com/gp/bestsellers/?ref_=nav_em_cs_bestsellers_0_1_1_2'
BEST_SELLERS_LINK_XPATH = "//div[contains(@id,'CardInstance')]//ul//li//a"


@when('Open Amazon best sellers page')
def open_amazon_help(context):
    context.driver.get(target_url)


@then('There are {link_amount} links is founded')
def search_for_keyword(context, link_amount):
    search = context.driver.find_elements_by_xpath(BEST_SELLERS_LINK_XPATH)
    assert len(search)==int(link_amount), f"Number of founded links is {len(search)}, but {int(link_amount)} is what expected!"