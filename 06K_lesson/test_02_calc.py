from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get(
    "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
    )


WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "#calculator"))
)


delay_input = driver.find_element(By.CSS_SELECTOR, "#delay")
delay_input.clear()
delay_input.send_keys("45")


def click_button(button_text):
    buttons = driver.find_elements(
        By.CSS_SELECTOR, "#calculator .keys span.btn"
        )
    for button in buttons:
        if button.text == button_text:
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(button)
            )
            button.click()
            break


click_button('7')
click_button('+')
click_button('8')
click_button('=')

WebDriverWait(driver, 120).until(
    EC.text_to_be_present_in_element(
        (By.CSS_SELECTOR, "#calculator .screen"),
        "15"
    )
)

result = driver.find_element(By.CSS_SELECTOR, "#calculator .screen").text


assert result == "15", f"Ожидалось 15, получено {result}"
print("Тест пройден успешно!")

driver.quit()
