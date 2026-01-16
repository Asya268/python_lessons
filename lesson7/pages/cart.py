from pages.base import BasePage
from selenium.webdriver.common.by import By


class CartPage(BasePage):
    CHECKOUT_BUTTON = (By.ID, "checkout")

    def click_checkout(self):
        self.find_element(self.CHECKOUT_BUTTON).click()
