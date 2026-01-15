from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from pages.login import LoginPage
from pages.main import MainPage
from pages.cart import CartPage
from pages.checkout import CheckoutPage
from selenium.webdriver.firefox.options import Options


def test_full_purchase():
    firefox_options = Options()
    service = Service(executable_path=r'C:\Users\Анастас\Downloads\geckodriver-v0.36.0-win64\geckodriver.exe')
    driver = webdriver.Firefox(service=service, options=firefox_options)
    driver.maximize_window()

    login = LoginPage(driver)
    main = MainPage(driver)
    cart = CartPage(driver)
    checkout = CheckoutPage(driver)

    driver.get("https://www.saucedemo.com/")

    login.enter_username("standard_user")
    login.enter_password("secret_sauce")
    login.click_login()

    main.add_backpack()
    main.add_tshirt()
    main.add_onesie()
    main.go_to_cart()

    cart.click_checkout()

    checkout.enter_first_name("Анастасия")
    checkout.enter_last_name("Жилина")
    checkout.enter_post_code("443500")
    checkout.click_continue()

    total_price = checkout.get_total_price()
    total = total_price.replace("Total: ", "").strip()

    assert total == "$58.29", f"Ожидалось $58.29, получено {total}"

    driver.quit()
