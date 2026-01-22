from pages.base import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import allure


class CheckoutPage(BasePage):
    """
    Класс для работы со страницей оформления заказа
    """
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POST_CODE = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    TOTAL_PRICE = (By.CSS_SELECTOR, ".summary_total_label")

    @allure.step("Ввод имени покупателя")
    def enter_first_name(self, first_name: str) -> None:
        """
        Вводит имя покупателя в поле
        """
        self.find_element(self.FIRST_NAME).send_keys(first_name)

    @allure.step("Ввод фамилии покупателя")
    def enter_last_name(self, last_name: str) -> None:
        """
        Вводит фамилию покупателя в поле

        """
        self.find_element(self.LAST_NAME).send_keys(last_name)

    @allure.step("Ввод почтового индекса")
    def enter_post_code(self, post_code: str) -> None:
        """
        Вводит почтовый индекс в соответствующее поле
        """
        self.find_element(self.POST_CODE).send_keys(post_code)

    @allure.step("Переход к подтверждению заказа")
    def click_continue(self) -> None:
        """
        Нажимает кнопку продолжения оформления заказа
        """
        self.find_element(self.CONTINUE_BUTTON).click()

    @allure.step("Получение итоговой суммы")
    def get_total_price(self) -> str:
        """
        Получает итоговую сумму заказа
        """
        total_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.TOTAL_PRICE)
        )
        return total_element.text
