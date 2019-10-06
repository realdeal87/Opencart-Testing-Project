"""Модуль описывает действия с главным меню сайта opencart"""
from locators import Menu
from .BasePage import BasePage


class MenuBar(BasePage):
    """Методы описывают действия с главным меню"""

    def components(self):
        """Переход в раздел Components"""
        self._wait_for_visible(Menu.components)
        self._click(Menu.components)
        return self

    def monitors(self):
        """Переход в подраздел Monitors"""
        self._click(Menu.monitors)
        return self
