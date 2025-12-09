from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# Инициализация драйвера
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager()
                                                .install()))
driver.maximize_window()

# Переход на тестовую страницу
driver.get("http://uitestingplayground.com/classattr")

# Ожидание загрузки страницы
sleep(5)

# Находим синюю кнопку
blue_button = driver.find_element(
    By.XPATH,
    "//button[contains(concat"
    "(' ', normalize-space(@class), ' '), ' btn-primary ')]")

# Кликаем по кнопке
blue_button.click()

print("Кнопка успешно нажата!")

sleep(5)
