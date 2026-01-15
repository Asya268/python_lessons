from pages.base import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class CheckoutPage(BasePage):
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POST_CODE = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    TOTAL_PRICE = (By.CSS_SELECTOR, ".summary_total_label")

    def enter_first_name(self, first_name):
        self.find_element(self.FIRST_NAME).send_keys(first_name)

    def enter_last_name(self, last_name):
        self.find_element(self.LAST_NAME).send_keys(last_name)

    def enter_post_code(self, post_code):
        self.find_element(self.POST_CODE).send_keys(post_code)

    def click_continue(self):
        self.find_element(self.CONTINUE_BUTTON).click()

    def get_total_price(self):
        total_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.TOTAL_PRICE)
        )
        return total_element.text
