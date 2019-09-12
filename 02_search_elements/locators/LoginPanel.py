from selenium.webdriver.common.by import By
"""Локаторы для панели логина сайта Opencart"""


class LoginPanel:
    """Локаторы для панели логина"""

    class LoginDetails:
        """Локаторы для панели ввода логина и пароля"""

        input_username = (By.ID, "input-username")
        input_password = (By.ID, "input-password")
        forgot = "Forgotten Password"
        login_button = "//button"
        home_page = "OpenCart"

    class ForgottenPassword:
        """Локаторы для панели ввода почтового ящика"""

        input_email = (By.ID, "input-email")
        reset_button = "//button"
        cancel_button = "//button[@data-original-title='Cancel']"
