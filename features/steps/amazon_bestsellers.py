from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep

# Init Variables

target_url = 'https://www.amazon.com/gp/bestsellers/?ref_=nav_em_cs_bestsellers_0_1_1_2'
BEST_SELLERS_LINK_XPATH = "//div[contains(@id,'CardInstance')]//ul//li//a"
BEST_SELLERS_PAGE_TITLE = (By.XPATH, "//span[@id='zg_banner_text']")

check_link_text = ''

@given('Open Amazon best sellers page')
def open_amazon_best_sellers(context):
    context.driver.get(target_url)
    context.driver.refresh()
    context.original_window = context.driver.current_window_handle
    element = WebDriverWait(context.driver, 10).until(
        EC.url_contains('https://www.amazon.com/gp/bestsellers'), message='Expected Best Sellers page to be displayed'
    )


@then('There are {link_amount} links is founded')
def search_for_keyword(context, link_amount):
    search = context.driver.find_elements_by_xpath(BEST_SELLERS_LINK_XPATH)
    assert len(search) == int(link_amount), f"Number of founded links is {len(search)}, but {int(link_amount)} is what expected!"


@then('All Best Sellers links open correct target pages')
def all_links_work(context):
    global check_link_text
    n = len(context.driver.find_elements_by_xpath(BEST_SELLERS_LINK_XPATH))
    print(f"Found {n} links")

    i = 0
    while i <= n-1:
        best_seller_links = context.driver.find_elements_by_xpath(BEST_SELLERS_LINK_XPATH)
        check_link_text = best_seller_links[i].text
        print(f"Testing link {i + 1}, check if text '{check_link_text}' is presented in the title. ", end='')
        best_seller_links[i].click()
        target_xpath = "//span[contains(text(), '" + check_link_text + "')]"
        element = WebDriverWait(context.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, target_xpath)), message=f"Expected Title '{check_link_text}' not found"
        )
        print(f"✓ Expected '{check_link_text}' found!")
        context.driver.back()
        i += 1