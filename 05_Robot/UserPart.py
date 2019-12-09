"""Библиотека кейвордов для пользовательской части Opencart"""
from selenium import webdriver
from selenium.webdriver import ChromeOptions, FirefoxOptions
from robot.api.deco import keyword

from pageobjects import AlertMSG, MainPage, MenuBar


class UserPart:
    """Класс для работы с кейвордами"""
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    def __init__(self, browser, url):
        self.browser = browser
        self.url = url
        self.web = None

    @keyword("Open Web Browser")
    def open_browser(self):
        """Кейворд для отрытия браузера и страницы Opencart"""
        if self.browser == "Chrome":
            options = ChromeOptions()
            options.add_argument("--headless")
            options.add_argument("--no-sandbox")
            self.web = webdriver.Chrome(options=options)
        elif self.browser == "Firefox":
            options = FirefoxOptions()
            options.add_argument("--headless")
            self.web = webdriver.Firefox(options=options)
        else:
            raise Exception(f"{self.browser} is not supported!")
        self.web.maximize_window()
        self.web.implicitly_wait(10)
        self.web.get(self.url)

    @keyword("Close Web Browser")
    def close_browser(self):
        """Кейворд для закрытия браузера"""
        self.web.quit()

    @keyword("Search Product")
    def search_product(self, product):
        """Поиск продукта по названию"""
        MainPage(self.web).search_element(product)

    @keyword("Choose Product")
    def choose_product(self, product):
        """Выбор карточки продукта"""
        MainPage(self.web).choose_product(product)

    @keyword("Add to wishlist Product number")
    def add_product_to_wishlist(self, number):
        """Добавление продукта в список желаемых по порядковому номеру"""
        MainPage(self.web).add_to_wishlist(number=int(number))

    @keyword("Add to compare Product number")
    def add_product_to_compare(self, number):
        """Добавление продукта в список для сравнения по порядковому номеру"""
        MainPage(self.web).add_to_compare(number=int(number))

    @keyword("Add product to cart quantity")
    def add_product_to_cart(self, quantity):
        """Добавление заданного количества продукта в корзину"""
        MainPage(self.web).add_to_cart(quantity=int(quantity))

    @keyword("List images quantity")
    def list_images(self, quantity):
        """Просмотр заданного количества изображений продукта"""
        MainPage(self.web).list_images(quantity=int(quantity))

    @keyword("Check Alert Success")
    def check_alert_success(self):
        """Подтверждение успешного действия"""
        AlertMSG(self.web).check_alert_success()

    @keyword("Go to Monitors")
    def go_to_monitors(self):
        """Переход в каталог Мониторы"""
        MenuBar(self.web).components().monitors()
