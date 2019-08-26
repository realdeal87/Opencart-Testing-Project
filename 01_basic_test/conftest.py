"""Модуль содержит функцию и фикстуру для выбора браузера для тестирования opencart"""
import pytest
from selenium import webdriver
from selenium.webdriver import ChromeOptions, FirefoxOptions, IeOptions


def pytest_addoption(parser):
    """Функция принимает параметры строки --browser {"Chrome", "Firefox", "IE"} и --base-url
    (по умолчанию 'localhost') """
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
def browser_driver(request):
    """Фикстура выбирает браузер на основе параметра коммандной строки"""

    browser = request.config.getoption("--browser")
    base_url = request.config.getoption("--base-url")
    url = "http://" + base_url + "/opencart"

    web = None
    if browser == "Chrome":
        options = ChromeOptions()
        options.add_argument("--start-fullscreen")
        options.add_argument("--headless")
        web = webdriver.Chrome(options=options)
        web.get(url)
    if browser == "Firefox":
        options = FirefoxOptions()
        options.add_argument("--headless")
        web = webdriver.Firefox(options=options)
        web.get(url)
        web.maximize_window()
    if browser == "IE":
        options = IeOptions()
        options.add_argument("-k")
        options.add_argument("--headless")
        web = webdriver.Ie(options=options)
    print("\nBrowser:", browser, "\nURL:", url)

    request.addfinalizer(web.quit)
    return web
