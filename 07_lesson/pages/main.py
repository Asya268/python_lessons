from pages.base import BasePage
from selenium.webdriver.common.by import By


class MainPage(BasePage):
    BACKPACK_BUTTON = (By.ID, "add-to-cart-sauce-labs-backpack")
    TSHIRT_BUTTON = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
    ONESIE_BUTTON = (By.ID, "add-to-cart-sauce-labs-onesie")
    CART_LINK = (By.CSS_SELECTOR, ".shopping_cart_link")

    def add_backpack(self):
        self.find_element(self.BACKPACK_BUTTON).click()

    def add_tshirt(self):
        self.find_element(self.TSHIRT_BUTTON).click()

    def add_onesie(self):
        self.find_element(self.ONESIE_BUTTON).click()

    def go_to_cart(self):
        self.find_element(self.CART_LINK).click()
