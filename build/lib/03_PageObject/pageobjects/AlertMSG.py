"""Модуль описывает ожидание получения сообщений о результатах действий"""
from locators import Alert
from .BasePage import BasePage


class AlertMSG(BasePage):
    """Методы описывают ожидание получения сообщений о результатах действий"""

    def check_alert_success(self):
        """Получение сообщения об успехе действия"""
        self._wait_for_visible(Alert.alert_success)

    def check_alert_danger(self):
        """Получение сообщения о провале действия"""
        self._wait_for_visible(Alert.alert_danger)
