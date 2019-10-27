"""Базовая проверка с использованием Selenium"""
import allure
from pageobjects import MainPage


@allure.feature("Баовые операции")
@allure.story("Отркрытие главной страницы")
@allure.title("Отркрытие главной страницы")
def test_opencart_mainpage(driver, url, logging_test):
    """Открыть в браузере основную страницу opencart"""
    with allure.step("Переход на главную страницу"):
        MainPage(driver, url).open()
    with allure.step("Сравнение заголовка страницы"):
        # assert MainPage(driver).title() == "Your Store"
        assert MainPage(driver).title() == "OLOLO"
