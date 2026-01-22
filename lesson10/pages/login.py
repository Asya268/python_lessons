from pages.base import BasePage
from selenium.webdriver.common.by import By
import allure


class LoginPage(BasePage):
    """
    Класс для работы со страницей авторизации
    """

    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")

    @allure.step("Ввод имени пользователя")
    def enter_username(self, username: str) -> None:
        """
        Вводит имя пользователя в поле авторизации
        """
        self.find_element(self.USERNAME).send_keys(username)

    @allure.step("Ввод пароля")
    def enter_password(self, password: str) -> None:
        """
        Вводит пароль в поле авторизации
        """
        self.find_element(self.PASSWORD).send_keys(password)

    @allure.step("Выполнение входа в систему")
    def click_login(self) -> None:
        """
        Нажимает кнопку входа в систему
        """
        self.find_element(self.LOGIN_BUTTON).click()
