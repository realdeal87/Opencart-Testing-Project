"""Модуль предустановок для тестирования сайта Opencart"""
import pytest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
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
def browser(request):
    """Фикстура возвращает имя браузера"""
    param = request.config.getoption("--browser")
    return param


@pytest.fixture
def url(request):
    """Фикстура возвращает URL Opencart"""
    param = "http://" + request.config.getoption("--base-url")
    return param


@pytest.fixture
def browser_driver(request, browser, url):
    """Фикстура для запуска браузеров {Chrome, Firefox, IE} в полноэкранном режиме"""
    web = None
    if browser == "Chrome":
        options = ChromeOptions()
        options.add_argument("--headless")
        web = webdriver.Chrome(options=options)
    if browser == "Firefox":
        options = FirefoxOptions()
        options.add_argument("--headless")
        web = webdriver.Firefox(options=options)
    if browser == "IE":
        options = IeOptions()
        options.add_argument("--headless")
        web = webdriver.Ie(options=options)
    web.maximize_window()
    web.implicitly_wait(20)
    web.get(url)
    request.addfinalizer(web.quit)
    return web


@pytest.fixture
def sign_in(browser_driver, url):
    """Фикстура для авторизации в Opencart и перехода в каталог продуктов"""
    browser_driver.get(url + "/admin")
    browser_driver.find_element(*LoginPanel.LoginDetails.input_username).send_keys("realdeal87")
    browser_driver.find_element(*LoginPanel.LoginDetails.input_password).send_keys("K1x9Z5b8!")
    browser_driver.find_element_by_xpath(LoginPanel.LoginDetails.login_button).submit()

    # Добавлена обработка исключения при поиске элементов "Catalog" и "Products".
    # При запуске тестов с параметром --waiting=0 неявное ожидание равно 0.
    # Если при этом установить оба или одно из явных ожиданий равными 0,
    # может сработать исключение NoSuchElementException.
    try:
        locator = DashBoard.catalog_link
        element = WebDriverWait(browser_driver, 20).until(EC.presence_of_element_located(locator))
        element.click()
        locator = DashBoard.products_link
        element = WebDriverWait(browser_driver, 20).until(EC.presence_of_element_located(locator))
        element.click()
    except NoSuchElementException:
        print("\nError in setup! No such element on page")
    except TimeoutException:
        print("\nError in setup! Timeout exception")
    else:
        print("\nYou get no errors in setup! Begin testing...")

    return browser_driver
