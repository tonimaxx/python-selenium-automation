from selenium.webdriver.common.by import By
from pages.base_page import Page

class MainPage(Page):

    def open_main_page(self):
        self.open_page('')
