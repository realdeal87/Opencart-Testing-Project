"""Тестовые сценарии для проверки основных операций с продуктами в каталоге Opencart"""
import time
from selenium.webdriver.common.alert import Alert
from locators import Alerts, DashBoard


def search_product(table, name, edit=None):
    """Функция для первого найденного продукта по заданному в тесте названию осуществляет
    переход к редактированию или отмечает чекбокс в зависимости от теста"""
    for p_trow in table:
        if p_trow.find_elements_by_tag_name("td")[2].text == name:
            if edit:
                p_trow.find_element_by_tag_name("a").click()
            else:
                p_trow.find_element_by_tag_name("input").click()
            break


def test_create_product(sign_in):
    """Функция добавляет продукт с заполнением минимального количества атрибутов"""
    p_name = "Alcatel OT-890"
    p_meta_teg_title = "Android 2.1"
    p_model = "Product 2011"

    sign_in.find_element_by_xpath(DashBoard.Products.add_new_button).click()
    sign_in.find_element(*DashBoard.Products.ProductEdit.product_name).send_keys(p_name)
    sign_in.find_element(*DashBoard.Products.ProductEdit.meta_teg_title).send_keys(p_meta_teg_title)
    sign_in.find_element_by_link_text(DashBoard.Products.ProductEdit.data_link).click()
    sign_in.find_element(*DashBoard.Products.ProductEdit.model).send_keys(p_model)
    sign_in.find_element_by_xpath(DashBoard.Products.ProductEdit.save_button).click()
    sign_in.find_element(*Alerts.alert_success)


def test_edit_product(sign_in):
    """Функция редактирует первый найденный продукт по заданному названию,
    добавляя описание продукта"""
    p_name = "Alcatel OT-890"
    p_description = "Alcatel OT-890 supports GSM frequency. Official announcement date is " \
                       "February 2011. The device is working on an Android OS, v2.1 (Eclair) " \
                       "with a 420 MHz processor. Alcatel OT-890 has 150 MB of built-in memory. " \
                       "This device has a Mediatek MT6516 chipset. The main screen size is 2.8 " \
                       "inches with 320 x 240 pixels resolution. It has a 143 ppi pixel density. " \
                       "The screen covers about 38.1% of the device's body. " \
                       "This is an average result.\n"

    p_table = sign_in.find_elements_by_xpath(DashBoard.Products.trows)
    search_product(p_table, p_name, "edit")
    sign_in.find_element(*DashBoard.Products.ProductEdit.description_area).click()
    sign_in.find_element(*DashBoard.Products.ProductEdit.description_area).send_keys(p_description)
    time.sleep(1)
    sign_in.find_element_by_xpath(DashBoard.Products.ProductEdit.save_button).click()
    sign_in.find_element(*Alerts.alert_success)


def test_delete_product(sign_in):
    """Функция удаляет первый найденный продукт по заданному названию"""
    p_name = "Alcatel OT-890"

    p_table = sign_in.find_elements_by_xpath(DashBoard.Products.trows)
    search_product(p_table, p_name)
    sign_in.find_element_by_xpath(DashBoard.Products.delete_button).click()
    Alert(sign_in).accept()
    sign_in.find_element(*Alerts.alert_success)
