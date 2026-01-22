import pytest
from selenium import webdriver
from pages.CalcPage import CalcPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.title("Тестирование калькулятора")
@allure.description("Тест проверяет корректность работу калькулятора")
@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.CRITICAL)
def test_calculator_addition(driver):
    calc = CalcPage(driver)
    with allure.step("Открытие страницы калькулятора"):
        calc.open()
    with allure.step("Установка задержки"):
        calc.set_delay(45)
    with allure.step("Выполнение вычисления"):
        calc.click_button('7')
        calc.click_button('+')
        calc.click_button('8')
        calc.click_button('=')

    WebDriverWait(driver, 120).until(EC.text_to_be_present_in_element(
        (By.CSS_SELECTOR, "#calculator .screen"),
        "15"
    ))

    with allure.step("Проверка результата"):
        result = calc.get_result()
        assert result == "15", f"Ожидалось 15, получено {result}"
        print("Тест пройден успешно!")
