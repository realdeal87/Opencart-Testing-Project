"""Базовая проверка с использованием Selenium"""
from pageobjects import MainPage


def test_opencart_mainpage(driver, url, logging_test):
    """Открыть в браузере основную страницу opencart"""

    driver.find_element_by_id("lolka")

    logging_test.debug('debug message')
    logging_test.info('info message')
    logging_test.warning('warn message')
    logging_test.error('error message')
    logging_test.critical('critical message')

    assert MainPage(driver, url).open().title() == "Your Store"
