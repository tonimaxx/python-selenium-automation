from selenium.webdriver.common.by import By
from pages.base_page import Page

class SigninPage(Page):
    PAGE_TITLE = (By.CSS_SELECTOR, 'h1')

    def verify_page_title(self):
        self.verify_text("Sign-In", *self.PAGE_TITLE)
