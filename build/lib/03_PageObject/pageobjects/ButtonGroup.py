"""Модуль описывает действия с группой кнопок в панели администратора
сайта opencart"""
from locators import Button
from .BasePage import BasePage


class ButtonGroup(BasePage):
    """Методы описывают действия с группой кнопок"""

    def add_new(self):
        """Добавить"""
        self._click(Button.add_new_button)
        return self

    def copy(self):
        """Копирование"""
        self._click(Button.copy_button)
        return self

    def delete(self):
        """Удаление продуктов"""
        self._click(Button.delete_button)
        return self

    def save(self):
        """Сохранение изменений"""
        self._click(Button.save_button)
        return self

    def cancel(self):
        """Отмена изменений"""
        self._click(Button.cancel_button)
        return self

    def accept(self):
        """Подтверждение удаления"""
        self.alert().accept()
        return self

    def dismiss(self):
        """Отмена удаления"""
        self.alert().dismiss()
        return self
