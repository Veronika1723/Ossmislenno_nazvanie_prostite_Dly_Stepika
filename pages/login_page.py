from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):        
        assert "login" in self.url, "link is not login"  
        assert True

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.Vhod), "have not vhod"
        assert True

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.Reg), "have not reg"
        assert True