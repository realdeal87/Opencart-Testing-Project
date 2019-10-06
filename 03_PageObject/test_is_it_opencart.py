"""Базовая проверка с использованием Selenium"""
from pageobjects import MainPage


def test_opencart_mainpage(driver, url):
    """Открыть в браузере основную страницу opencart"""
    assert MainPage(driver, url).open().title() == "Your Store"
