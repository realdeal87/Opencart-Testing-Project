"""Тестовые сценарии для проверки основных операций с продуктами в каталоге Opencart"""
from pageobjects import AdminPage, BasePage, DashBoard, MainPage


def test_create_product(driver, url):
    """Успешное добавление продукта с заполнением требуемых полей"""

    p_name = "Alcatel OT-890"
    p_meta_teg_title = "Android 2.1"
    p_model = "Product 2011"

    AdminPage(driver).open(url).login(login="Realdeal87", password="K1x9Z5b8!")
    DashBoard.Navigation(driver).catalog().products()
    DashBoard.Products(driver) \
        .create_product() \
        .fill_required_fields(p_name, p_meta_teg_title, p_model) \
        .save_changes()


def test_edit_product(driver, url):
    """Успешное редактирование продукта по заданному порядковому номеру,
    с добавлением описания продукта"""

    p_description = "Alcatel OT-890 supports GSM frequency. Official announcement date is " \
                    "February 2011. The device is working on an Android OS, v2.1 (Eclair) " \
                    "with a 420 MHz processor. Alcatel OT-890 has 150 MB of built-in memory. " \
                    "This device has a Mediatek MT6516 chipset. The main screen size is 2.8 " \
                    "inches with 320 x 240 pixels resolution. It has a 143 ppi pixel density. " \
                    "The screen covers about 38.1% of the device's body. " \
                    "This is an average result."

    AdminPage(driver).open(url).login(login="Realdeal87", password="K1x9Z5b8!")
    DashBoard.Navigation(driver).catalog().products()
    DashBoard.Products(driver) \
        .edit_product(number=1) \
        .fill_description(p_description) \
        .save_changes()


def test_delete_products(driver, url):
    """Успешное удаление продуктов по заданному порядковому номеру и количеству"""

    AdminPage(driver).open(url).login(login="Realdeal87", password="K1x9Z5b8!")
    DashBoard.Navigation(driver).catalog().products()
    DashBoard.Products(driver) \
        .choose_products(number=3, quantity=3) \
        .delete_products()
