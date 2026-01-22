from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class FormPage:
    """
    Класс для работы с формой
    """
    def __init__(self, driver):
        """
        Инициализация __init__
        :param driver: экземпляр веб-драйвера
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)
        self.fields = {
            'first-name': "Иван",
            'last-name': "Петров",
            'address': "Ленина, 55-3",
            'zip-code': "",
            'city': "Москва",
            'country': "Россия",
            'e-mail': "test@skypro.com",
            'phone': "+7985899998787",
            'job-position': "QA",
            'company': "SkyPro"
        }

    @allure.step("Открытие формы")
    def open(self):
        """
        Открывает страницу с формой
        """
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
            )

    @allure.step("Заполнение формы")
    def fill_form(self):
        """
        Заполняет форму данными
        """
        for field, value in self.fields.items():
            self.wait.until(
                EC.presence_of_element_located((
                    By.NAME, field))).send_keys(value)

    @allure.step("Отправка формы")
    def submit_form(self) -> None:
        """
        Отправляет заполненную форму
        """
        self.wait.until(
            EC.element_to_be_clickable((
                By.CSS_SELECTOR, '[type="submit"]'))).click()

    @allure.step("Получение класса поля")
    def get_field_class(self, field_id: str) -> str:
        """
        Получает класс указанного поля
        :param field_id: ID поля формы
        :return: класс элемента
        """
        element = self.wait.until(
            EC.presence_of_element_located((By.ID, field_id))
        ).get_attribute("class")
        return element

    @allure.step("Проверка ошибки зипкода")
    def check_zip_code_error(self) -> bool:
        """
        Проверяет наличие ошибки в поле зипкода
        :return: Если поле не заполнено возвращает ошибку
        """
        return "alert-danger" in self.get_field_class("zip-code")

    @allure.step("Проверка заполнения формы")
    def check_fields_success(self) -> bool:
        """
        Проверяет успешное заполнение всех полей
        :return: True если все поля заполнены успешно, False если не заполнены
        """
        fields = ['first-name', 'last-name', 'address', 'e-mail', 'phone',
                  'city', 'country', 'job-position', 'company']
        for field in fields:
            if "success" not in self.get_field_class(field):
                return False
        return True

    @allure.step("Проверка отправки формы")
    def check_form_submission(self):
        """
        Выполняет проверку результатов отправки формы
        """
        assert self.check_zip_code_error()
        assert self.check_fields_success()
