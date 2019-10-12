"""Модуль описывает действия в разделе Products панели администратора сайта opencart"""
import time
from locators import Products
from .BasePage import BasePage


class ProductsPage(BasePage):
    """Методы описывают действия в разделе Products панели администратора"""

    def edit_product(self, number):
        """Редактирование продукта"""
        self._click(Products.edit_buttons, number - 1)
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

    def fill_required_fields(self, name, meta_teg_title, model):
        """Заполнение обязательной информации о продукте"""
        self._wait_for_visible(Products.ProductEdit.general_link)
        self._input(Products.ProductEdit.product_name, name)
        self._input(Products.ProductEdit.meta_teg_title, meta_teg_title)
        self._click(Products.ProductEdit.data_link)
        self._input(Products.ProductEdit.model, model)
        return self

    def upload_new_image(self, file):
        """Загрузка нового изображения продукта"""
        script = """
                document.getElementById("button-upload").click();
                var f = document.createElement("form");
                f.id = "form-upload";
                f.style.display = "block";
                f.enctype = "multipart/form-data";
                inp = document.createElement("input");
                inp.type = "file";
                inp.name = "file[]";
                f.appendChild(inp);
                body = document.getElementsByTagName("body")[0];
                body.insertBefore(f, body.firstChild);"""
        self._click(Products.ProductEdit.image_link)
        self._click(Products.ProductEdit.thumb_image)
        self._click(Products.ProductEdit.button_image)
        time.sleep(2)
        self._upload_file(script, file)
        time.sleep(2)
        self.alert().accept()
        return self

    def choose_image(self, file):
        """Выбор изображения для продукта"""
        image = {'xpath': f'//a/img[@title="{file}"]'}
        self._click(image)
        return self

    def fill_description(self, description):
        """Добавление описания продукта"""
        self._click(Products.ProductEdit.description_area)
        self._input(Products.ProductEdit.description_area, description)
        return self

    def product_filter(self, name='', model='', price='', quantity=''):
        """Поиск продукта по заданным параметрам"""
        self._input(Products.input_model, model)
        self._input(Products.input_price, price)
        self._input(Products.input_name, name)
        self._input(Products.input_name, quantity)
        self._click(Products.button_filter)
