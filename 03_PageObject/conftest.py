"""Модуль предустановок для тестирования сайта Opencart"""
import pytest
from selenium import webdriver
from selenium.webdriver import ChromeOptions, FirefoxOptions


def pytest_addoption(parser):
    """Функция принимает параметры строки --browser {"Chrome", "Firefox", "IE"}, --base-url
    (по умолчанию 'localhost/opencart') и --waiting (по умолчанию 20)"""
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
def url(request):
    """Фикстура для передачи базовой ссылки на тестируемый ресурс"""
    return "http://" + request.config.getoption("--base-url")


@pytest.fixture
def driver(request):
    """Фикстура для запуска браузеров {Chrome, Firefox} в полноэкранном режиме"""
    browser = request.config.getoption("--browser")
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
    # request.addfinalizer(web.quit)
    return web
