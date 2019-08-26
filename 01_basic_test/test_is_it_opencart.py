"""Базовая проверка с использованием Selenium"""


def test_opencart_homepage(browser_driver):
    """Открыть в браузере основную страницу opencart"""
    assert browser_driver.title == "Your Store"
