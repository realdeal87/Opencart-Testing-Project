"""Модуль предустановок для тестирования сайта Opencart"""
import datetime
import logging
import urllib.parse
import pytest
from browsermobproxy import Server, Client
from selenium import webdriver
from selenium.webdriver import ChromeOptions, FirefoxOptions
from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener


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
def proxy():
    """Фикстура для конфигурирования прокси-сервера"""
    server = Server("03_PageObject/browsermob-proxy-2.1.4/bin/browsermob-proxy")
    server.start()
    client = Client("localhost:8080")
    print(client.port)
    client.new_har()
    return client


@pytest.fixture
def driver(request, proxy):
    """Фикстура для запуска браузеров {Chrome, Firefox} в полноэкранном режиме"""
    browser = request.config.getoption("--browser")
    waiting = request.config.getoption("--waiting")
    url = urllib.parse.urlparse(proxy.proxy).path

    if browser == "Chrome":
        options = ChromeOptions()
        options.add_argument('--proxy-server=%s' % url)
        # options.add_argument("--headless")
        # web = webdriver.Chrome(options=options)
        web = EventFiringWebDriver(webdriver.Chrome(options=options), MyListener())
    elif browser == "Firefox":
        options = FirefoxOptions()
        options.add_argument('--proxy-server=%s' % url)
        # options.add_argument("--headless")
        # web = webdriver.Firefox(options=options)
        web = EventFiringWebDriver(webdriver.Firefox(options=options), MyListener())
    else:
        raise Exception(f"{browser} is not supported!")

    web.maximize_window()
    web.implicitly_wait(waiting)

    def fin():
        """Файнолайзер: запись логов браузера, прокси сервера, закрытие браузера"""
        if web.name == "chrome":
            browser_logging(web)
        proxy_logging(proxy)
        web.quit()

    request.addfinalizer(fin)
    return web


@pytest.fixture(scope="session")
def logging_test():
    """Фикстура для конфигурирования логирования"""
    # создаём logger
    logger = logging.getLogger("opencart_testing")
    logger.setLevel(logging.DEBUG)
    # создаём консольный handler и задаём уровень
    shr = logging.StreamHandler()
    shr.setLevel(logging.WARNING)
    # создаём файловый handler и задаём уровень
    fhr = logging.FileHandler("03_PageObject/logs/opencart_testing.log")
    fhr.setLevel(logging.INFO)
    # создаём formatter
    formatter = logging.Formatter('%(asctime)s - %(funcName)s - %(levelname)s - %(message)s')
    # добавляем formatter в shr и fhr
    shr.setFormatter(formatter)
    fhr.setFormatter(formatter)
    # добавляем shr и fhr к logger
    logger.addHandler(shr)
    logger.addHandler(fhr)
    return logger


class MyListener(AbstractEventListener):
    """Логирование Webdriver"""
    logging.basicConfig(filename="03_PageObject/logs/opencart_testing_webdriver.log",
                        level=logging.ERROR)

    def before_find(self, by, value, driver):
        """Логирование перед нахождением элемента"""
        logging.info("Opening element " + by + value)

    def after_find(self, by, value, driver):
        """Логирование после нахождения элемента"""
        logging.info("Find element " + by + value)

    def on_exception(self, exception, driver):
        """Логирование в случае ошибки, создание скриншота"""
        now = datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S_")
        message = str(now) + driver.name + "_" + exception.msg
        driver.save_screenshot("03_PageObject/screenshots/" + message[:55] + ".png")
        logging.error(message)


def browser_logging(driver):
    """Запись лога браузера"""
    with open("03_PageObject/logs/opencart_testing_browser.log", "a") as file:
        for line in driver.get_log('browser'):
            message = str(line["timestamp"]) + " - " + str(line["source"]) + " - " +\
                str(line["level"]) + " - " + str(line["message"] + "\n")
            file.write(message)


def proxy_logging(proxy):
    """Запись лога прокси сервера"""
    with open("03_PageObject/logs/opencart_testing_proxy.log", "a") as file:
        params = proxy.har["log"]
        for key in params:
            message = str(key) + "->" + str(params[key]) + "\n"
            file.write(message)
