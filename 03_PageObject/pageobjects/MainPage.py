"""Модуль описывает действия на главной странице сайта opencart"""
from locators import Main, ProductCard
from .BasePage import BasePage


class MainPage(BasePage):
    """Методы описывают действия на главной странице"""

    def open(self):
        """Открытие главной страницы"""
        self._open()
        return self

    def title(self):
        """Получение заголовка главной страницы"""
        return self._get_title()

    def add_to_cart(self, quantity):
        """Добавление товара в корзину"""
        self._input(ProductCard.input_qty, quantity)
        self._click(ProductCard.button_cart)
        return self

    def add_to_wishlist(self, number):
        """Добавление товара в список желаемых"""
        self._click(ProductCard.like_it_button, number - 1)
        return self

    def add_to_compare(self, number):
        """Добавление товара в каталог для сравнения"""
        self._click(ProductCard.compare_button, number - 1)
        return self

    def list_images(self, quantity):
        """Пролистывание миниатюр"""
        self._click(ProductCard.Thumbnails.thumbnails)
        i = 0
        while i < quantity:
            self._click(ProductCard.Thumbnails.arrow_right)
            i += 1
        self._click(ProductCard.Thumbnails.button_esc)
        return self

    def search_element(self, product):
        """Поиск продукта"""
        self._input(Main.Search.search_field, product)
        self._click(Main.Search.search_button)
        return self

    def choose_product(self, product):
        """Выбор продукта по названию на главной странице"""
        product = {'link': product}
        self._click(product)
        return self
