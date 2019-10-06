"""Модуль описывает действия в разделе Products панели администратора сайта opencart"""
from locators import Products
from .BasePage import BasePage


class ProductsPage(BasePage):
    """Методы описывают действия в разделе Products панели администратора"""

    def create_product(self):
        """Создание продукта"""
        self._click(Products.add_new_button)
        return self

    def edit_product(self, number):
        """Редактирование продукта"""
        self._click(Products.edit_buttons, number - 1)
        return self

    def save_changes(self):
        """Сохранение изменений"""
        self._click(Products.ProductEdit.save_button)
        return self

    def cancel_changes(self):
        """Отмена изменений"""
        self._click(Products.ProductEdit.cancel_button)
        return self

    def choose_products(self, number, quantity=None):
        """Выбор продуктов"""
        if number == "all":
            self._click(Products.checkbox_all)
        else:
            if quantity:
                i = 0
                while i < quantity:
                    self._click(Products.checkbox, number - 1 + i)
                    i += 1
            else:
                self._click(Products.checkbox, number - 1)
        return self

    def copy_products(self):
        """Копирование продуктов"""
        self._click(Products.copy_button)
        return self

    def delete_products(self):
        """Удаление продуктов"""
        self._click(Products.delete_button)
        return self

    def accept(self):
        """Подтверждение удаления"""
        self.alert.alert_accept()

    def dismiss(self):
        """Отмена удаления"""
        self.alert.alert_dismiss()

    def fill_required_fields(self, name, meta_teg_title, model):
        """Заполнение обязательной информации о продукте"""
        self._wait_for_visible(Products.ProductEdit.general_link)
        self._input(Products.ProductEdit.product_name, name)
        self._input(Products.ProductEdit.meta_teg_title, meta_teg_title)
        self._click(Products.ProductEdit.data_link)
        self._input(Products.ProductEdit.model, model)
        return self

    def fill_description(self, description):
        """Добавление описания продукта"""
        self._click(Products.ProductEdit.description_area)
        self._input(Products.ProductEdit.description_area, description)
        return self
