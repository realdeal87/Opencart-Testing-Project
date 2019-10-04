from selenium.webdriver.common.by import By
from locators import AdminLocators


class AdminPage:

    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        self.driver.get(url + "/admin")
        return self

    def login(self, login, password):
        self.driver.find_element(By.ID, "input-username").clear()
        self.driver.find_element(By.ID, "input-username").send_keys(login)
        self.driver.find_element(By.ID, "input-password").clear()
        self.driver.find_element(By.ID, "input-password").send_keys(password)
        self.driver.find_element(By.XPATH, "//button").submit()
        return self
