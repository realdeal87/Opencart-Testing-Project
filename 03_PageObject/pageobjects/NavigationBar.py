"""Модуль описывает действия с боковым меню панели администратора сайта opencart"""
from locators import Navigation
from .BasePage import BasePage


class NavigationBar(BasePage):
    """Методы описывают действия с боковым меню панели администратора"""

    def catalog(self):
        """Переход в раздел Catalog"""
        self._click(Navigation.catalog)
        return self

    def categories(self):
        """Переход в подраздел Categories"""
        self._click(Navigation.categories)
        return self

    def products(self):
        """Переход в подраздел Products"""
        self._click(Navigation.products)
        return self
