"""Базовая проверка с использованием Selenium"""
from pageobjects import MainPage


def test_opencart_mainpage(driver, url):
    """Открыть в браузере основную страницу opencart"""
    MainPage(driver).open(url)
    assert MainPage(driver).title == "Your Store"
