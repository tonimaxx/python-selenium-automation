from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductPage(Page):

    NEW_ARRIVALS_XPATH = "//span[contains(.,'New Arrivals')]"
    NEW_ARRIVALS_FLYOUT_XPATH = "//div[@id='nav-flyout-anchor']/div[16]"
    NEW_ARRIVALS_FLYOUT = (By.XPATH, "//div[@id='nav-flyout-anchor']/div[16]")

    def open_product_page(self, product_page):
        self.driver.get(f"https://www.amazon.com/{product_page}")

    def hover_new_arrival(self):
        element = self.driver.find_element_by_link_text("New Arrivals")
        action = ActionChains(self.driver)
        action.move_to_element(element)
        action.perform()