"""Локаторы для панели логина сайта Opencart"""


class LoginPanel:
    """Локаторы для панели логина"""

    class LoginDetails:
        """Локаторы для панели ввода логина и пароля"""

        input_username = ("id", "input-username")
        input_password = ("id", "input-password")
        forgot = "Forgotten Password"
        login_button = "//button"
        alert_danger = ("class name", "alert-danger")
        home_page = "OpenCart"

    class ForgottenPassword:
        """Локаторы для панели ввода почтового ящика"""

        input_email = ("id", "input-email")
        reset_button = "//button"
        cancel_button = "//button[@data-original-title='Cancel']"

    class Dashboard:
        """Локаторы для панели администратора"""

        dashboard_nav = ("id", "navigation")
