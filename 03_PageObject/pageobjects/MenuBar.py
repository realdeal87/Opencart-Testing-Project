from locators import Menu
from .BasePage import BasePage


class MenuBar(BasePage):

    def components(self):
        self._wait_for_visible(Menu.components)
        self._click(Menu.components)
        return self

    def monitors(self):
        self._click(Menu.monitors)
        return self
