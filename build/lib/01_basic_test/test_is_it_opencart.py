"""Базовая проверка с использованием Selenium"""


def test_opencart_homepage(browser_driver, browser, base_url):
    """Открыть в браузере основную страницу opencart"""
    url = "http://" + base_url + "/opencart"
    print("\nBrowser:", browser, "\nURL:", url)
    browser_driver.get(url)
    assert browser_driver.title == "Your Store"
