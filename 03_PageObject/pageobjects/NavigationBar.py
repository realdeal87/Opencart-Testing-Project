from locators import Navigation
from .BasePage import BasePage


class NavigationBar(BasePage):

    def catalog(self):
        self._click(Navigation.catalog)
        return self

    def products(self):
        self._click(Navigation.products)
        return self
