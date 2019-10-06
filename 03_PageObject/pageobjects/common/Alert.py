from selenium.webdriver.common.alert import Alert as AL


class Alert:

    def __init__(self, driver):
        self.driver = driver

    def alert_accept(self):
        AL(self.driver).accept()

    def alert_dismiss(self):
        AL(self.driver).dismiss()
