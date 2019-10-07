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

    class AdminBar:

        dropdown_toggle = {'class': 'dropdown-toggle'}
        your_profile = {'css': '.dropdown > ul:nth-child(2) > li:nth-child(1) > a:nth-child(1)'}
        your_store = {'link': 'Your Store'}
        homepage = {'css': '.dropdown > ul:nth-child(2) > li:nth-child(7) > a:nth-child(1)'}
        documentation = {'css': '.dropdown > ul:nth-child(2) > li:nth-child(8) > a:nth-child(1)'}
        support_forum = {'css': '.dropdown > ul:nth-child(2) > li:nth-child(9) > a:nth-child(1)'}

        logout = {'css': '.nav > li:nth-child(2) > a:nth-child(1)'}