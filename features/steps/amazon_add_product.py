from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.common.keys import Keys

'''
------------
Note:-
Next version
Python Selenium - Wait until next page has loaded after form submit
https://stackoverflow.com/questions/42069503/python-selenium-wait-until-next-page-has-loaded-after-form-submit
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
------------
'''

## Test user credential
amazon_useremail = "rossumhuggins@gmail.com"
amazon_userpassword = "tonitester"
product_to_search = "software tester tshirt"
#product_to_search = str.replace("+", " ")

CART_ICON_LINK = (By.ID, "nav-cart")
FLYOUT_SIGNIN_BUTTON = (By.XPATH, "//a[@data-nav-ref='nav_custrec_signin']")
INPUT_SIGNIN_EMAIL = (By.XPATH,"//input[@type='email']")
FIRST_PRODUCT = (By.XPATH, "//div[@class='sg-col-inner']//span[@data-component-id='1']//a")
ADD_TO_CART_BUTTON = (By.XPATH, "//input[@id='add-to-cart-button']")


@when('Click flyout Signin button on main page')
def click_flyout_signin_button(context):
    ##//a[@data-nav-ref='nav_custrec_signin']
    context.driver.find_element(*FLYOUT_SIGNIN_BUTTON).click()
    sleep(4)

@when('Enter Email and Click continue')
def enter_email_and_click_continue(context):

    #Fill Useremail and Submit
    search = context.driver.find_element(By.XPATH, "//input[@type='email']")
    search.clear()
    search.send_keys(amazon_useremail)
    search.send_keys(Keys.RETURN)
    sleep(4)

    #Fill Password and Submit
    search = context.driver.find_element(By.XPATH, "//input[@type='password']")
    search.clear()
    search.send_keys(amazon_userpassword)
    search.send_keys(Keys.RETURN)
    sleep(4)

@when('Search and add a product')
def search_and_add_product(context):

    # Search a product by URL
    context.driver.get("https://www.amazon.com/s?k="+product_to_search)
    sleep(4)

    '''
    #Search a product by find_element
    search = context.driver.find_element(By.XPATH, "//input[@id='twotabsearchtextbox']")
    search.clear()
    search.send_keys("Halloween Candy")
    search.send_keys(Keys.RETURN)
    '''

    #Click the first product from result
    context.driver.find_element(*FIRST_PRODUCT).click()
    sleep(4)

    """
    # Todo - Save product title to be expected in the cart for verification
    # Get product title
    # product_title = context.driver.find_elements_by_xpath("//h1/span[@id='productTitle']").getText()
    # print("this product is "+product_title)
    """

    # Click Add to cart button
    context.driver.find_element(*ADD_TO_CART_BUTTON).click()
    sleep(4)

@then('Cart is not empty')
def verify_if_cart_is_not_empty(context):

    # This is just to verify if user can add a product to cart and it's expected to be there

    not_expect_text = "Your Amazon Cart is empty"
    target_xpath = "//h2[contains(text(), '"+not_expect_text+"')]"
    search = context.driver.find_elements_by_xpath(target_xpath)
    is_cart_not_empty = False if len(search) > 0 else True
    assert is_cart_not_empty, "No product added to cart, the cart is empty!"

    # Todo - Verify the item title in cart is the item that was added