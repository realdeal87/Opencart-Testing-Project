"""Модуль содержит функцию и фикстуру для выбора браузера для тестирования opencart"""
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
def base_url(request):
    """Фикстура возвращает базовый URL"""
    param = request.config.getoption("--base-url")
    return param


@pytest.fixture
def browser_driver(request, browser):
    """Фикстура для запуска браузеров {Chrome, Firefox, IE} в полноэкранном режиме
    с опцией headless"""
    web = None
    if browser == "Chrome":
        options = ChromeOptions()
        # options.add_argument("--start-fullscreen")
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
    request.addfinalizer(web.quit)
    return web
