from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select

class Header(Page):

    ## Test user credential
    amazon_useremail = "rossumhuggins@gmail.com"
    amazon_userpassword = "tonitester"
    product_to_search = "halloween tech shirt"

    #Locators
    SEARCH_DEPARTMENT = (By.ID, 'searchDropdownBox')
    SEARCH_DEPARTMENT_XPATH = "//select[@id='searchDropdownBox']"
    NEW_ARRIVAL = (By.XPATH, "//span[contains(.,'New Arrivals')]")
    NEW_ARRIVAL_CLASS = (By.CLASS_NAME, "nav-a-content")
    SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
    SEARCH_ICON = (By.ID, 'nav-search-submit-button')
    CART_ICON = (By.ID, "nav-cart")
    ORDER_LINK = (By.ID, "nav-orders")
    CART_ICON_LINK = (By.ID, "nav-cart")
    FLYOUT_SIGNIN_BUTTON = (By.XPATH, "//a[@data-nav-ref='nav_custrec_signin']")
    INPUT_SIGNIN_EMAIL_XPATH_STR = "//input[@type='email']"
    INPUT_SIGNIN_EMAIL_XPATH = (By.XPATH, INPUT_SIGNIN_EMAIL_XPATH_STR)
    INPUT_SIGNIN_PASSWORD_XPATH_STR = "//input[@type='password']"
    INPUT_SIGNIN_PASSWORD_XPATH = (By.XPATH, INPUT_SIGNIN_PASSWORD_XPATH_STR)
    FIRST_PRODUCT = (By.XPATH, "//div[@class='sg-col-inner']//span[@data-component-id='1']//a")
    ADD_TO_CART_BUTTON = (By.XPATH, "//input[@id='add-to-cart-button']")

    def select_department(self, department):
        # identify dropdown with Select class
        sel = Select(self.driver.find_element_by_xpath(self.SEARCH_DEPARTMENT_XPATH))
        # select by select_by_visible_text() method
        sel.select_by_visible_text(department)

    def execute_search(self, keyword):
        search = self.driver.find_element(*self.SEARCH_FIELD)
        search.clear()
        search.send_keys(keyword)
        search.send_keys(Keys.RETURN)


    def input_search(self):
        #Todo -- future use
        pass

    def click_search(self):
        self.click(*self.SEARCH_ICON)

    def click_cart_icon(self):
        self.click(*self.CART_ICON)

    def click_order_link(self):
        self.click(*self.ORDER_LINK)

    def sign_in(self):
        self.driver.find_element(*self.FLYOUT_SIGNIN_BUTTON).click()

        self.wait_for_element_appear(*self.INPUT_SIGNIN_EMAIL_XPATH)

        # Fill User email and Submit
        search = self.driver.find_element(By.XPATH, self.INPUT_SIGNIN_EMAIL_XPATH_STR)
        search.clear()
        search.send_keys(self.amazon_useremail)
        search.send_keys(Keys.RETURN)

        self.wait_for_element_appear(*self.INPUT_SIGNIN_PASSWORD_XPATH)

        # Fill Password and Submit
        search = self.driver.find_element(By.XPATH, self.INPUT_SIGNIN_PASSWORD_XPATH_STR)
        search.clear()
        search.send_keys(self.amazon_userpassword)
        search.send_keys(Keys.RETURN)

    def search_and_add_product(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.title_contains("Amazon.com")
        )

        # Search a product by URL
        self.driver.get("https://www.amazon.com/s?k=" + self.product_to_search)
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.FIRST_PRODUCT)
        )

        # Click the first product from result
        self.driver.find_element(*self.FIRST_PRODUCT).click()
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.ADD_TO_CART_BUTTON)
        )

        # Click Add to cart button
        self.driver.find_element(*self.ADD_TO_CART_BUTTON).click()



