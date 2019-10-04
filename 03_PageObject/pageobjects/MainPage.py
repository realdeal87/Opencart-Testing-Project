from selenium.webdriver.common.by import By


class MainPage:

    def __init__(self, driver):
        self.driver = driver
        self.title = self.driver.title

    def open(self, url):
        self.driver.get(url)
        return self

    def add_to_cart(self, quantity):
        self.driver.find_element(By.ID, "input-quantity").clear()
        self.driver.find_element(By.ID, "input-quantity").send_keys(quantity)
        self.driver.find_element(By.ID, "button-cart").click()
        return self

    def add_to_wishlist(self, number):
        self.driver.find_element(By.CSS_SELECTOR, f"div.product-layout:nth-child({number}) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > button:nth-child(2)").click()
        return self

    def compare_elements(self, number1, number2):
        self.driver.find_element(By.CSS_SELECTOR, f"div.product-layout:nth-child({number1}) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > button:nth-child(3)").click()
        self.driver.find_element(By.CSS_SELECTOR, f"div.product-layout:nth-child({number2}) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > button:nth-child(3)").click()
        self.driver.find_element(By.PARTIAL_LINK_TEXT, "Product Compare").click()
        return self

    def list_images(self):
        pictures = self.driver.find_elements(By.CLASS_NAME, "thumbnail")
        pictures[0].click()
        for _ in pictures:
            self.driver.find_element(By.CSS_SELECTOR, "button.mfp-arrow:nth-child(4)").click()
        self.driver.find_element(By.CSS_SELECTOR, ".mfp-close").click()
        return self

    class Header:

        def __init__(self, driver):
            self.driver = driver

        def search_element(self, product):
            self.driver.find_element(By.NAME, "search").clear()
            self.driver.find_element(By.NAME, "search").send_keys(product)
            self.driver.find_element(By.CSS_SELECTOR, ".btn-default").click()
            return self

    class MenuBar:

        def __init__(self, driver):
            self.driver = driver

        def components(self):
            self.driver.find_element(By.LINK_TEXT, "Components").click()
            return self

        def monitors(self):
            self.driver.find_element(By.PARTIAL_LINK_TEXT, "Monitors").click()
            return self

    class Featured:

        def __init__(self, driver):
            self.driver = driver

        def choose_product(self, product):
            self.driver.find_element(By.LINK_TEXT, product).click()
            return self
