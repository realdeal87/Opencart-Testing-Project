"""Модуль описывает базовые действия на сайте opencart"""
import os
import allure
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    """Методы описывают базовые действия на сайте"""

    def __init__(self, driver, url=None):
        self.driver = driver
        self.url = url

    def __element(self, selector: dict, number: int):
        """Получение элементов на странице"""
        with allure.step(f"Поиск элемента {selector}, порядковй номер {number + 1}"):
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
        """Открытие страницы"""
        with allure.step(f"Открытие страницы {self.url + patch}"):
            self.driver.get(self.url + patch)

    def _click(self, selector, number=0):
        """Нажатие на элемент"""
        with allure.step(f"Нажатие на элемент {selector}, порядковй номер {number + 1}"):
            self.__element(selector, number).click()
            # Работает не везде:
            # ActionChains(self.driver).move_to_element(self.__element(selector,
            # number)).click().perform()

    def _input(self, selector, value, number=0):
        """Взаимодействие с полем ввода"""
        with allure.step(f"Ввод текста {value} в элемент {selector}, порядковй номер {number + 1}"):
            element = self.__element(selector, number)
            element.clear()
            element.send_keys(value)

    def _wait_for_visible(self, selector, number=0, wait=10):
        """Ожидание элемента"""
        with allure.step(f"Ожидание {wait} секунд элемента {selector},"
                         f"порядковй номер {number + 1}"):
            return WebDriverWait(self.driver,
                                 wait).until(EC.visibility_of(self.__element(selector, number)))

    def _get_title(self):
        """Получение заголовка страницы"""
        with allure.step(f"Получение заголовка страницы {self.driver.title}"):
            return self.driver.title

    def alert(self):
        """Переключение на алертинг"""
        with allure.step(f"Переключение на алертинг"):
            return self.driver.switch_to.alert

    def _upload_file(self, script, file):
        """Загрузка файлов в форму"""
        with allure.step(f"Загрузка файла {file}"):
            dirname = os.path.dirname(__file__)
            filename = os.path.join(dirname, file)
            self.driver.execute_script(script)
            element = self.driver.find_element_by_css_selector("input[type=file]")
            element.send_keys(filename)

    def _get_value(self, selector, number=0):
        """Получение значения поля ввода"""
        return self.__element(selector, number).get_attribute("value")
