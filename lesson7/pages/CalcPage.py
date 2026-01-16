
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalcPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 60)

        # Локаторы
        self.delay = (By.CSS_SELECTOR, '#delay')
        self.calculator = (By.CSS_SELECTOR, '#calculator')
        self.screen = (By.CSS_SELECTOR, '#calculator .screen')
        self.btn_selector = (By.CSS_SELECTOR, '#calculator .keys span.btn')

    def open(self):
        self.driver.get(
         "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        self.wait.until(EC.presence_of_element_located(self.calculator))

    def set_delay(self, delay):
        field = self.wait.until(EC.presence_of_element_located(self.delay))
        field.clear()
        field.send_keys(str(delay))

    def click_button(self, text):
        buttons = self.wait.until(
            EC.presence_of_all_elements_located(self.btn_selector)
            )
        button = next((btn for btn in buttons if btn.text == text), None)
        if button:
            self.wait.until(EC.element_to_be_clickable(button)).click()

    def get_result(self):
        return self.wait.until(
            EC.presence_of_element_located(self.screen)).text
