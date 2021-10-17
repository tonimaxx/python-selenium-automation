from selenium.webdriver.common.by import By
from pages.base_page import Page

class CartPage(Page):

    PAGE_TITLE = (By.CSS_SELECTOR, 'h2')

    def verify_page_title(self):
        self.verify_text("Your Amazon Cart is empty", *self.PAGE_TITLE)

    def verify_if_cart_is_not_empty(self):
        # This is just to verify if user can add a product to cart and it's expected to be there

        self.verify_title_contains("Amazon.com")
        not_expect_text = "Your Amazon Cart is empty"
        target_xpath = (By.XPATH, f"//h2[contains(text(), '{not_expect_text}')]")

        assert len(self.find_elements(*target_xpath)) == 0, f"Not expected text '{not_expect_text}', but it's shown!"