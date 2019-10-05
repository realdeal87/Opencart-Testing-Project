from locators import Admin
from .BasePage import BasePage


class AdminPage(BasePage):

    def open(self):
        self._open("/admin")
        return self

    def login(self, login, password):
        self._input(Admin.LoginDetails.username, login)
        self._input(Admin.LoginDetails.password, password)
        self._click(Admin.LoginDetails.login_button)
        return self
