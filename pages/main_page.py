from .base_page import BasePage
from .locators import MainPageLocators, LoginPageLocators
from .login_page import LoginPage
from selenium.webdriver.common.by import By

class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()

        LoginPage.should_be_login_page(self)
        # login_form = LoginPage.should_be_login_form(self)
        # register_form = LoginPage.should_be_register_form(self)


    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "#Login link is not presented"
