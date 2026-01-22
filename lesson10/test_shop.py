import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from pages.login import LoginPage
from pages.main import MainPage
from pages.cart import CartPage
from pages.checkout import CheckoutPage
import allure


@pytest.fixture
def driver():
    """
    Фикстура для создания и настройки драйвера Firefox
    """
    service = Service(GeckoDriverManager().install())
    options = webdriver.FirefoxOptions()
    options.add_argument('--disable-notifications')
    options.add_argument('--disable-popup-blocking')

    driver = webdriver.Firefox(service=service, options=options)
    driver.maximize_window()

    yield driver
    driver.quit()


@allure.title("Тестирование полного процесса покупки")
@allure.description("Проверка всего процесса покупки")
@allure.feature("Процесс покупки")
@allure.severity(allure.severity_level.BLOCKER)
def test_full_purchase(driver):
    login = LoginPage(driver)
    main = MainPage(driver)
    cart = CartPage(driver)
    checkout = CheckoutPage(driver)

    with allure.step(" Авторизация в системе"):
        driver.get("https://www.saucedemo.com/")
        login.enter_username("standard_user")
        login.enter_password("secret_sauce")
        login.click_login()

    with allure.step("Добавление товаров в корзину"):
        main.add_backpack()
        main.add_tshirt()
        main.add_onesie()
        main.go_to_cart()

    with allure.step("Переход к оформлению заказа"):
        cart.click_checkout()

    with allure.step("Шаг 4: Заполнение данных для доставки"):
        checkout.enter_first_name("Анастасия")
        checkout.enter_last_name("Жилина")
        checkout.enter_post_code("443500")
        checkout.click_continue()

    with allure.step("Шаг 5: Проверка итоговой суммы"):
        total_price = checkout.get_total_price()
        total = total_price.replace("Total: ", "").strip()
        assert total == "$58.29", f"Ожидалось $58.29, получено {total}"
