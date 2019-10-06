from locators import AlertMSGlocators
from .BasePage import BasePage


class AlertMSG(BasePage):

    def check_alert_success(self):
        self._wait_for_visible(AlertMSGlocators.alert_success)

    def check_alert_danger(self):
        self._wait_for_visible(AlertMSGlocators.alert_danger)
