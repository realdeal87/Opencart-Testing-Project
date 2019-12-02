"""Модуль описывает действия в меню администратора сайта opencart"""
from locators import Admin
from .BasePage import BasePage


class AdminBar(BasePage):
    """Методы описывают действия в меню администратора"""

    def logout(self):
        """Выход из аккаунта администратора"""
        self._wait_for_visible(Admin.AdminBar.logout)
        self._click(Admin.AdminBar.logout)

    def your_profile(self):
        """Переход в профайл"""
        self._click(Admin.AdminBar.dropdown_toggle)
        self._click(Admin.AdminBar.your_profile)

    def your_store(self):
        """Переход по ссылке на главную страницу"""
        self._click(Admin.AdminBar.dropdown_toggle)
        self._click(Admin.AdminBar.your_store)
