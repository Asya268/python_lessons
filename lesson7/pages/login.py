from pages.base import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")

    def enter_username(self, username):
        self.find_element(self.USERNAME).send_keys(username)

    def enter_password(self, password):
        self.find_element(self.PASSWORD).send_keys(password)

    def click_login(self):
        self.find_element(self.LOGIN_BUTTON).click()
