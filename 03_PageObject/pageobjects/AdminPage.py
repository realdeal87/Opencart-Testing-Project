"""Модуль описывает действия в панели администратора сайта opencart"""
from locators import Admin
from .BasePage import BasePage


class AdminPage(BasePage):
    """Методы описывают действия в панели администратора"""

    def open(self):
        """Открытие панели администратора"""
        self._open("/admin")
        return self

    def login(self, login, password):
        """Авторизация"""
        self._input(Admin.LoginDetails.username, login)
        self._input(Admin.LoginDetails.password, password)
        self._click(Admin.LoginDetails.login_button)
        return self

    def forgotten_password(self, email):
        """Отправка пароля на почту"""
        self._click(Admin.LoginDetails.forgot)
        self._input(Admin.ForgottenPassword.email, email)
        self._click(Admin.ForgottenPassword.reset_button)

    def title(self):
        """Получение заголовка панели администратора"""
        return self._get_title()
