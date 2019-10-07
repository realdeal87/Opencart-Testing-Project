"""Модуль описывает действия на главной странице сайта opencart"""
from locators import DashBoard
from .BasePage import BasePage


class DashBoardPage(BasePage):

    def settings(self):
        self._click(DashBoard.button_setting)
        return self

    def refresh_theme_cache(self):
        self._click(DashBoard.theme_refresh)
        return self

    def refresh_sass_cache(self):
        self._click(DashBoard.sass_refresh)
        return self
