"""Модуль предустановок для тестирования сайта Opencart"""
import logging
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


@pytest.fixture
def logging_test():
    # создаём logger
    logger = logging.getLogger("opencart-testing")
    logger.setLevel(logging.DEBUG)

    # создаём консольный handler и задаём уровень
    ch = logging.StreamHandler()
    ch.setLevel(logging.WARNING)

    # создаём файловый handler и задаём уровень
    fh = logging.FileHandler("03_PageObject/opencart-testing.log")
    fh.setLevel(logging.INFO)

    # создаём formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # добавляем formatter в ch и fh
    ch.setFormatter(formatter)
    fh.setFormatter(formatter)

    # добавляем ch и fh к logger
    logger.addHandler(ch)
    logger.addHandler(fh)
    return logger
