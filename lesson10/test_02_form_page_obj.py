import pytest
from selenium import webdriver
from pages.FormPage import FormPage
import allure


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(3)
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.title('Тестирование формы обратной связи')
@allure.feature("Форма обратной связи")
@allure.description("Тестирование процесса заполнения и отправки формы")
@allure.severity(allure.severity_level.NORMAL)
def test_form_submission_flow(driver):
    form_page = FormPage(driver)
    with allure.step("Открытие страницы формы"):
        form_page.open()
    with allure.step("Заполнение формы данными"):
        form_page.fill_form()
    with allure.step("Отправка заполненной формы"):
        form_page.submit_form()
    with allure.step("Проверка отправки"):
        form_page.check_form_submission()
