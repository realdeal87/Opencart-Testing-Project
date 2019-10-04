from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By


class DashBoard:

    class Navigation:

        def __init__(self, driver):
            self.driver = driver

        def catalog(self):
            self.driver.find_element(By.LINK_TEXT, "Catalog").click()
            return self

        def products(self):
            self.driver.find_element(By.LINK_TEXT, "Products").click()
            return self

    class Products:

        def __init__(self, driver):
            self.driver = driver
            self.alert = Alert(self.driver)

        def create_product(self):
            self.driver.find_element(By.CSS_SELECTOR, "a.btn:nth-child(2)").click()
            return self

        def edit_product(self, number):
            self.driver.find_element(By.CSS_SELECTOR, f".table > tbody:nth-child(2) > tr:nth-child({number}) > td:nth-child(8) > a:nth-child(1)").click()
            return self

        def save_changes(self):
            self.driver.find_element(By.CSS_SELECTOR, "div.pull-right > button:nth-child(1)").click()
            return self

        def cancel_changes(self):
            self.driver.find_element(By.CSS_SELECTOR, "a.btn")
            return self

        def choose_products(self, number, quantity=None):
            if number == "all":
                self.driver.find_element(By.CSS_SELECTOR, ".table > thead:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > input:nth-child(1)").click()
            else:
                if quantity:
                    i = 0
                    while i < quantity:
                        self.driver.find_element(By.CSS_SELECTOR, f".table > tbody:nth-child(2) > tr:nth-child({number + i}) > td:nth-child(1) > input:nth-child(1)").click()
                        i += 1
                else:
                    self.driver.find_element(By.CSS_SELECTOR, f".table > tbody:nth-child(2) > tr:nth-child({number}) > td:nth-child(1) > input:nth-child(1)").click()
            return self

        def copy_products(self):
            self.driver.find_element(By.CSS_SELECTOR, "button.btn:nth-child(3)").click()
            return self

        def delete_products(self):
            self.driver.find_element(By.CSS_SELECTOR, "button.btn:nth-child(4)").click()
            self.alert.accept()
            return self

        def fill_required_fields(self, name, meta_teg_title, model):
            self.driver.find_element(By.ID, "input-name1").clear()
            self.driver.find_element(By.ID, "input-name1").send_keys(name)
            self.driver.find_element(By.ID, "input-meta-title1").clear()
            self.driver.find_element(By.ID, "input-meta-title1").send_keys(meta_teg_title)
            self.driver.find_element(By.LINK_TEXT, "Data").click()
            self.driver.find_element(By.ID, "input-model").clear()
            self.driver.find_element(By.ID, "input-model").send_keys(model)
            return self

        def fill_description(self, description):
            self.driver.find_element(By.CLASS_NAME, "note-editable").click()
            self.driver.find_element(By.CLASS_NAME, "note-editable").send_keys(description)
            return self








