from pages.base import BasePage
from selenium.webdriver.common.by import By
import allure


class MainPage(BasePage):
    """
    Класс для работы с главной страницей магазина
    """

    BACKPACK_BUTTON = (By.ID, "add-to-cart-sauce-labs-backpack")
    TSHIRT_BUTTON = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
    ONESIE_BUTTON = (By.ID, "add-to-cart-sauce-labs-onesie")
    CART_LINK = (By.CSS_SELECTOR, ".shopping_cart_link")

    @allure.step("Добавление рюкзака в корзину")
    def add_backpack(self) -> None:
        """
        Добавляет рюкзак в корзину
        """
        self.find_element(self.BACKPACK_BUTTON).click()

    @allure.step("Добавление футболки в корзину")
    def add_tshirt(self) -> None:
        """
        Добавляет футболку в корзину
        """
        self.find_element(self.TSHIRT_BUTTON).click()

    @allure.step("Добавление комбинезона в корзину")
    def add_onesie(self) -> None:
        """
        Добавляет комбинезон в корзину
        """
        self.find_element(self.ONESIE_BUTTON).click()

    @allure.step("Переход в корзину")
    def go_to_cart(self) -> None:
        """
        Переходит в корзину покупок
        """
        self.find_element(self.CART_LINK).click()
