"""Локаторы для панели логина сайта Opencart"""


class AdminLocators:
    """Локаторы для панели логина"""

    class LoginDetails:
        """Локаторы для панели ввода логина и пароля"""

        input_username = {'id', 'input-username'}
        input_password = {'id', "input-password"}
        forgot = "Forgotten Password"
        login_button = "//button"
        home_page = "OpenCart"

    class ForgottenPassword:
        """Локаторы для панели ввода почтового ящика"""

        input_email = (By.ID, "input-email")
        reset_button = "//button"
        cancel_button = "//button[@data-original-title='Cancel']"
