from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = ChromeService(ChromeDriverManager().install())
browser = webdriver.Chrome(service=service)

browser.get
('https://bonigarcia.dev/selenium-webdriver-java/loading-images.html')


WebDriverWait(browser, 50).until(
    EC.presence_of_element_located((By.CLASS_NAME, 'col-12'))
)


img_element = WebDriverWait(browser, 50).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "#award"))
)

src_value = img_element.get_attribute("src")
print(src_value)

browser.quit()
