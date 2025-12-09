
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager()
                                                  .install()))
driver.maximize_window()

# Переход на тестовую страницу
driver.get("http://the-internet.herokuapp.com/inputs")

sleep(5)

input_field = driver.find_element(By.TAG_NAME, "input")

input_field.send_keys("Sky")
print("Введено значение 'Sky'")

input_field.clear()
print("Поле очищено")

input_field.send_keys("Pro")
print("Введено значение 'Pro'")

# Закрываем браузер
driver.quit()
