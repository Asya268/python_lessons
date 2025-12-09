from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from time import sleep

# Инициализация драйвера Firefox
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager()
                                                  .install()))
driver.maximize_window()

# Переход на страницу логина
driver.get("http://the-internet.herokuapp.com/login")

sleep(2)

# Находим поля ввода
username_field = driver.find_element(By.ID, "username")
password_field = driver.find_element(By.ID, "password")

# Вводим данные
username_field.send_keys("tomsmith")
password_field.send_keys("SuperSecretPassword!")

# нажимаем кнопку входа
login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
login_button.click()

sleep(2)

# Получаем текст с зеленой плашки
success_message = driver.find_element(By.CSS_SELECTOR, ".flash.success")
message_text = success_message.text

# Выводим текст в консоль
print(f"Сообщение об успехе: {message_text}")

# Закрываем браузер
driver.quit()
