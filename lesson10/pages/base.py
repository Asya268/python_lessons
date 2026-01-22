from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class BasePage:
    """
    Базовый класс для работы с веб-страницами
    """
    def __init__(self, driver):
        """
        Инициализация базовой страницы
        :param driver: экземпляр веб-драйвера
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step('Поиск веб-элемента')
    def find_element(self, locator):
        """
        Метод для поиска веб-элемента на странице

        """
        return self.wait.until(EC.presence_of_element_located(locator))

    @allure.step('Поиск нескольких веб-элементов')
    def find_elements(self, locator) -> list:
        """
        Метод для поиска нескольких веб-элементов на странице
        """
        return self.wait.until(EC.presence_of_all_elements_located(locator))
