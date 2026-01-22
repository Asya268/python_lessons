from pages.base import BasePage
from selenium.webdriver.common.by import By
import allure


class CartPage(BasePage):
    """
    Класс для работы с корзиной
    """
    CHECKOUT_BUTTON = (By.ID, "checkout")

    @allure.step("Переход к оформлению заказа")
    def click_checkout(self) -> None:
        """
        Метод для перехода к оформлению заказа

        Выполняет следующие действия:
        - Находит кнопку оформления заказа
        - Выполняет клик по кнопке

        :return: None
        """
        self.find_element(self.CHECKOUT_BUTTON).click()
