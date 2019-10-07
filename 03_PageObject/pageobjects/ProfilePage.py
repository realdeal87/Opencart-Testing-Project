"""Модуль описывает действия в меню администратора сайта opencart"""
from locators import Profile
from .BasePage import BasePage


class ProfilePage(BasePage):
    """Методы описывают действия в меню администратора"""

    def save_changes(self):
        """Сохранение изменений"""
        self._click(Profile.save_button)
        return self

    def cancel_changes(self):
        """Отмена изменений"""
        self._click(Profile.cancel_button)
        return self
