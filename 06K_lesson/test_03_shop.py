from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

firefox_options = Options()

service = Service(executable_path=r'C:\Users\Анастас\Downloads\geckodriver-v0.36.0-win64\geckodriver.exe')

driver = webdriver.Firefox(service=service, options=firefox_options)
driver.maximize_window()

driver.get("https://www.saucedemo.com/")

WebDriverWait(driver, 20).until(
    EC.title_is("Swag Labs")
)

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "#user-name"))
)
driver.find_element(By.CSS_SELECTOR, "#user-name").send_keys("standard_user")
driver.find_element(By.CSS_SELECTOR, "#password").send_keys("secret_sauce")
driver.find_element(By.CSS_SELECTOR, "#login-button").click()

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack"))
)
driver.find_element(
    By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()
driver.find_element(
    By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()
driver.find_element(
    By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, ".shopping_cart_link"))
)
driver.find_element(By.CSS_SELECTOR, ".shopping_cart_link").click()


WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "#checkout"))
)
driver.find_element(By.CSS_SELECTOR, "#checkout").click()


WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "#first-name"))
)
driver.find_element(By.CSS_SELECTOR, "#first-name").send_keys("Анасасия")
driver.find_element(By.CSS_SELECTOR, "#last-name").send_keys("Жилина")
driver.find_element(By.CSS_SELECTOR, "#postal-code").send_keys("443500")

driver.find_element(By.CSS_SELECTOR, "#continue").click()

driver.implicitly_wait(10)
total = driver.find_element(By.CSS_SELECTOR, ".summary_total_label").text

print(total)

driver.quit()
