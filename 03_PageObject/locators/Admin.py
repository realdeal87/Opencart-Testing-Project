"""Локаторы для панели логина сайта Opencart"""


class Admin:
    """Локаторы для панели логина"""

    class LoginDetails:
        """Локаторы для панели ввода логина и пароля"""

        username = {'id': 'input-username'}
        password = {'id': 'input-password'}
        forgot = {'link': 'Forgotten Password'}
        login_button = {'css': '.btn', 'xpath': '//button'}
        home_page = {'link': 'OpenCart'}

    class ForgottenPassword:
        """Локаторы для панели ввода почтового ящика"""

        email = {'id': 'input-email'}
        reset_button = {'css': 'button.btn', 'xpath': '//button'}
        cancel_button = {'css': 'a.btn'}
