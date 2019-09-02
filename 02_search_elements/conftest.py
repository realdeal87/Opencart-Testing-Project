"""Модуль содержит функцию и фикстуру для выбора браузера для тестирования сайта Opencart"""
import pytest
from selenium import webdriver
from selenium.webdriver import ChromeOptions, FirefoxOptions, IeOptions


def pytest_addoption(parser):
    """Функция принимает параметры строки --browser {"Chrome", "Firefox", "IE"} и --base-url
    (по умолчанию 'localhost')"""
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
        default="localhost",
        help="URL that you're testing, by default: 'localhost'"
    )


@pytest.fixture
def browser(request):
    """Фикстура возвращает имя браузера"""
    param = request.config.getoption("--browser")
    return param


@pytest.fixture
def url(request):
    """Фикстура возвращает URL"""
    param = "http://" + request.config.getoption("--base-url") + "/opencart"
    return param


@pytest.fixture
def browser_driver(request, browser, url):
    """Фикстура для запуска браузеров {Chrome, Firefox, IE} в полноэкранном режиме"""
    web = None
    if browser == "Chrome":
        options = ChromeOptions()
        web = webdriver.Chrome(options=options)
    if browser == "Firefox":
        options = FirefoxOptions()
        web = webdriver.Firefox(options=options)
    if browser == "IE":
        options = IeOptions()
        web = webdriver.Ie(options=options)
    web.maximize_window()
    web.implicitly_wait(20)
    web.get(url)
    request.addfinalizer(web.quit)
    return web
