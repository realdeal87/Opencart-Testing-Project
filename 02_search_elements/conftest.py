"""Модуль предустановок для тестирования сайта Opencart"""
import pytest
from selenium import webdriver
from selenium.webdriver import ChromeOptions, FirefoxOptions, IeOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import DashBoard, LoginPanel


def pytest_addoption(parser):
    """Функция принимает параметры строки --browser {"Chrome", "Firefox", "IE"} и --base-url
    (по умолчанию 'localhost/opencart')"""
    parser.addoption(
        "--browser",
        action="store",
        help="web browser that you're testing",
        choices=["Chrome", "Firefox", "IE"],
        required=True
    )

    parser.addoption(
        "--base-url",
        action="store",
        default="localhost/opencart",
        help="URL that you're testing, by default: 'localhost/opencart'",
        required=False
    )

    parser.addoption(
        "--waiting",
        action="store",
        help="Time which browser will wait elements",
        default=20,
        required=False
    )


@pytest.fixture
def browser_driver(request):
    """Фикстура для запуска браузеров {Chrome, Firefox, IE} в полноэкранном режиме"""
    browser = request.config.getoption("--browser")
    url = "http://" + request.config.getoption("--base-url")
    waiting = request.config.getoption("--waiting")

    if browser == "Chrome":
        options = ChromeOptions()
        # options.add_argument("--headless")
        web = webdriver.Chrome(options=options)
    elif browser == "Firefox":
        options = FirefoxOptions()
        # options.add_argument("--headless")
        web = webdriver.Firefox(options=options)
    else:
        raise Exception(f"{browser} is not supported!")

    web.maximize_window()
    web.implicitly_wait(waiting)
    web.get(url)
    # request.addfinalizer(web.quit)
    return web


@pytest.fixture
def sign_in(request, browser_driver):
    """Фикстура для авторизации в Opencart и перехода в каталог продуктов"""
    browser_driver.get("http://" + request.config.getoption("--base-url") + "/admin")
    browser_driver.find_element(*LoginPanel.LoginDetails.input_username).send_keys("realdeal87")
    browser_driver.find_element(*LoginPanel.LoginDetails.input_password).send_keys("K1x9Z5b8!")
    browser_driver.find_element_by_xpath(LoginPanel.LoginDetails.login_button).submit()
    return browser_driver


@pytest.fixture
def go_to_products(sign_in):
    locator = DashBoard.catalog_link
    element = WebDriverWait(sign_in, 20).until(EC.presence_of_element_located(locator))
    element.click()
    locator = DashBoard.products_link
    element = WebDriverWait(sign_in, 20).until(EC.presence_of_element_located(locator))
    element.click()
    return sign_in
