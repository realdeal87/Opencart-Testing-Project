"""Модуль для обработки всплывающего модального окна"""
from selenium.webdriver.common.alert import Alert as AL


class Alert:
    """Методы для работы с всплывающим модальным окном"""

    def __init__(self, driver):
        self.driver = driver

    def alert_accept(self):
        """Метод подтверждает действие"""
        AL(self.driver).accept()

    def alert_dismiss(self):
        """Метод отменяет действие"""
        AL(self.driver).dismiss()
