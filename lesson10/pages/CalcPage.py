
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class CalcPage:
    """
    Класс для работы со страницей калькулятора
    """
    def __init__(self, driver):
        """
        Инициализация страницы калькулятора
        :param driver: экземпляр веб-драйвера
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 60)

        # Локаторы
        self.delay = (By.CSS_SELECTOR, '#delay')
        self.calculator = (By.CSS_SELECTOR, '#calculator')
        self.screen = (By.CSS_SELECTOR, '#calculator .screen')
        self.btn_selector = (By.CSS_SELECTOR, '#calculator .keys span.btn')

    @allure.step("Открытие страницы калькулятора")
    def open(self):
        """
        Открывает страницу калькулятора
        """
        self.driver.get(
         "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        self.wait.until(EC.presence_of_element_located(self.calculator))

    @allure.step("Установка задержки вычислений")
    def set_delay(self, delay: int) -> None:
        """
        Устанавливает задержку вычислений
        """
        field = self.wait.until(EC.presence_of_element_located(self.delay))
        field.clear()
        field.send_keys(str(delay))

    @allure.step("Нажатие кнопки на калькуляторе")
    def click_button(self, text: str) -> None:
        """
        Находит и нажимает кнопку с указанным текстом
        """
        buttons = self.wait.until(
            EC.presence_of_all_elements_located(self.btn_selector)
            )
        button = next((btn for btn in buttons if btn.text == text), None)
        if button:
            self.wait.until(EC.element_to_be_clickable(button)).click()

    @allure.step("Получение результата вычисления")
    def get_result(self) -> str:
        """
        Получает текущий результат с экрана калькулятора
        :return: Взвращает результат вычисления
        """
        return self.wait.until(
            EC.presence_of_element_located(self.screen)).text
