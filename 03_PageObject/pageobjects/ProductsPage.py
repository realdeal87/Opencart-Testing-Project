from locators import Products
from .BasePage import BasePage


class ProductsPage(BasePage):

    def create_product(self):
        self._click(Products.add_new_button)
        return self

    def edit_product(self, number):
        self._click(Products.edit_buttons, number)
        return self

    def save_changes(self):
        self._click(Products.ProductEdit.save_button)
        return self

    def cancel_changes(self):
        self._click(Products.ProductEdit.cancel_button)
        return self

    def choose_products(self, number, quantity=None):
        if number == "all":
            self._click(Products.checkbox_all)
        else:
            if quantity:
                i = 0
                while i < quantity:
                    self._click(Products.checkbox, number + i)
                    i += 1
            else:
                self._click(Products.checkbox, number)
        return self

    def copy_products(self):
        self._click(Products.copy_button)
        return self

    def delete_products(self):
        self._click(Products.delete_button)
        return self

    def accept(self):
        self._alert_accept()

    def dismiss(self):
        self._alert_dismiss()

    def fill_required_fields(self, name, meta_teg_title, model):
        self._wait_for_visible(Products.ProductEdit.general_link)
        self._input(Products.ProductEdit.product_name, name)
        self._input(Products.ProductEdit.meta_teg_title, meta_teg_title)
        self._click(Products.ProductEdit.data_link)
        self._input(Products.ProductEdit.model, model)
        return self

    def fill_description(self, description):
        self._click(Products.ProductEdit.description_area)
        self._input(Products.ProductEdit.description_area, description)
        return self
