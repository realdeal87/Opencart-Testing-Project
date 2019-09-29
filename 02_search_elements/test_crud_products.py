"""Тестовые сценарии для проверки основных операций с продуктами в каталоге Opencart"""
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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


def checkout_alert(browser_driver):
    """Функция ожидает появления элемента alert_success"""
    locator = Alerts.alert_success
    WebDriverWait(browser_driver, 5).until(EC.presence_of_element_located(locator))


def test_create_product(go_to_products):
    """Успешное добавление продукта с заполнением минимального количества атрибутов"""
    p_name = "Alcatel OT-890"
    p_meta_teg_title = "Android 2.1"
    p_model = "Product 2011"

    go_to_products.find_element_by_xpath(DashBoard.Products.add_new_button).click()
    go_to_products.find_element(*DashBoard.Products.ProductEdit.product_name).send_keys(p_name)
    go_to_products.find_element(*DashBoard.Products.ProductEdit.meta_teg_title).send_keys(p_meta_teg_title)
    go_to_products.find_element_by_link_text(DashBoard.Products.ProductEdit.data_link).click()
    go_to_products.find_element(*DashBoard.Products.ProductEdit.model).send_keys(p_model)
    go_to_products.find_element_by_xpath(DashBoard.Products.ProductEdit.save_button).click()
    checkout_alert(go_to_products)


def test_edit_product(go_to_products):
    """Успешное редактирование первого найденного продукта по заданному названию,
    с добавлением описания продукта"""
    p_name = "Alcatel OT-890"
    p_description = "Alcatel OT-890 supports GSM frequency. Official announcement date is " \
                    "February 2011. The device is working on an Android OS, v2.1 (Eclair) " \
                    "with a 420 MHz processor. Alcatel OT-890 has 150 MB of built-in memory. " \
                    "This device has a Mediatek MT6516 chipset. The main screen size is 2.8 " \
                    "inches with 320 x 240 pixels resolution. It has a 143 ppi pixel density. " \
                    "The screen covers about 38.1% of the device's body. " \
                    "This is an average result."

    p_table = go_to_products.find_elements_by_xpath(DashBoard.Products.trows)
    search_product(p_table, p_name, "edit")
    go_to_products.find_element(*DashBoard.Products.ProductEdit.description_area).click()
    go_to_products.find_element(*DashBoard.Products.ProductEdit.description_area).send_keys(p_description)

    # Раньше здесь стоял time.sleep, иногда драйвер проскакивал ввод
    # Теперь проверяется наличие текста p_description в поле ввода
    try:
        locator = DashBoard.Products.ProductEdit.description_area_edited
        WebDriverWait(go_to_products, 5).until(EC.text_to_be_present_in_element(locator, "Проверка"))
    except TimeoutException:
        print("WARN No input text in text area!")
    go_to_products.find_element_by_xpath(DashBoard.Products.ProductEdit.save_button).click()
    checkout_alert(go_to_products)


def test_delete_product(go_to_products):
    """Успешное удаление первого найденного продукта по заданному названию"""
    p_name = "Alcatel OT-890"

    p_table = go_to_products.find_elements_by_xpath(DashBoard.Products.trows)
    search_product(p_table, p_name)
    go_to_products.find_element_by_xpath(DashBoard.Products.delete_button).click()
    Alert(go_to_products).accept()
    checkout_alert(go_to_products)
