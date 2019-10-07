"""Модуль описывает действия на главной странице панели администратора
сайта opencart"""
from locators import DashBoard
from .BasePage import BasePage


class DashBoardPage(BasePage):
    """Методы описывают действия на главной странице панели администратора"""

    def settings(self):
        """Переход в настройки"""
        self._click(DashBoard.button_setting)
        return self

    def refresh_theme_cache(self):
        """Очистка кеша темы"""
        self._click(DashBoard.theme_refresh)
        return self

    def refresh_sass_cache(self):
        """Очистка sass кеша"""
        self._click(DashBoard.sass_refresh)
        return self
