import pytest
from selenium import webdriver
from pages.CalcPage import CalcPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_calculator_addition(driver):
    # Создаем объект страницы
    calc = CalcPage(driver)

    # Открываем страницу
    calc.open()

    # Устанавливаем задержку
    calc.set_delay(45)

    # Выполняем вычисления
    calc.click_button('7')
    calc.click_button('+')
    calc.click_button('8')
    calc.click_button('=')

    WebDriverWait(driver, 120).until(EC.text_to_be_present_in_element(
        (By.CSS_SELECTOR, "#calculator .screen"),
        "15"
    ))
    # Проверяем результат
    result = calc.get_result()
    assert result == "15", f"Ожидалось 15, получено {result}"
    print("Тест пройден успешно!")
