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
driver.get("http://uitestingplayground.com/dynamicid")

sleep(2)

# Находим синюю кнопку
blue_button = driver.find_element(By.CSS_SELECTOR, "button.btn-primary")

# Кликаем по кнопке
blue_button.click()

print("Кнопка успешно нажата!")

sleep(2)
