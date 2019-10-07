"""Модуль описывает действия в меню администратора сайта opencart"""
from locators import Admin
from .BasePage import BasePage


class AdminBar(BasePage):

    def logout(self):
        self._wait_for_visible(Admin.AdminBar.logout)
        self._click(Admin.AdminBar.logout)

    def your_profile(self):
        self._click(Admin.AdminBar.dropdown_toggle)
        self._click(Admin.AdminBar.your_profile)

    def your_store(self):
        self._click(Admin.AdminBar.dropdown_toggle)
        self._click(Admin.AdminBar.your_store)
