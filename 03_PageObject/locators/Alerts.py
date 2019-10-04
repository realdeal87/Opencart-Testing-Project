"""Локаторы для алертингов на сайте Opencart"""
from selenium.webdriver.common.by import By


class Alerts:
    """Локаторы алертингов"""
    alert_success = (By.CLASS_NAME, "alert-success")
    alert_danger = (By.CLASS_NAME, "alert-danger")
