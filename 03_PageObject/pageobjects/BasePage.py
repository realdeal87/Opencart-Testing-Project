from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from .common.Alert import Alert


class BasePage:

    def __init__(self, driver, url=None):
        self.driver = driver
        self.url = url
        self.alert = Alert(self.driver)

    def __element(self, selector: dict, number: int):
        by = None
        if 'css' in selector.keys():
            by = By.CSS_SELECTOR
            selector = selector['css']
        elif 'id' in selector.keys():
            by = By.ID
            selector = selector['id']
        elif 'link' in selector.keys():
            by = By.LINK_TEXT
            selector = selector['link']
        elif 'part_link' in selector.keys():
            by = By.PARTIAL_LINK_TEXT
            selector = selector['part_link']
        elif 'class' in selector.keys():
            by = By.CLASS_NAME
            selector = selector['class']
        elif 'xpath' in selector.keys():
            by = By.XPATH
            selector = selector['xpath']
        elif 'name' in selector.keys():
            by = By.NAME
            selector = selector['name']
        return self.driver.find_elements(by, selector)[number]

    def _open(self, patch=''):
        self.driver.get(self.url + patch)

    def _click(self, selector, number=0):
        self.__element(selector, number).click()
        # ActionChains(self.driver).move_to_element(self.__element(selector, number)).click().perform()

    def _input(self, selector, value, number=0):
        element = self.__element(selector, number)
        element.clear()
        element.send_keys(value)

    def _wait_for_visible(self, selector, number=0, wait=3):
        return WebDriverWait(self.driver, wait).until(EC.visibility_of(self.__element(selector, number)))

    def _get_title(self):
        return self.driver.title
