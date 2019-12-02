"""Тестовые сценарии для проверки основных операций с продуктами в каталоге Opencart"""
import allure
from pageobjects import AdminPage, AlertMSG, ButtonGroup, NavigationBar, ProductsPage


@allure.feature("Редактирование каталога товаров")
@allure.story("Создание карточки товара")
@allure.title("Создание карточки товара")
def test_create_product(driver, url, logging_test):
    """Успешное добавление продукта с заполнением требуемых полей"""

    p_name = "Alcatel OT-890"
    p_meta_teg_title = "Android 2.1"
    p_model = "Product 2011"

    with allure.step("Авторизация на странице администратора"):
        AdminPage(driver, url).open().login(login="Realdeal87", password="K1x9Z5b8!")
    with allure.step("Переход в раздел каталога Products"):
        NavigationBar(driver).catalog().products()
    with allure.step("Нажатие кнопки Add New"):
        ButtonGroup(driver).add_new()
    with allure.step("Заполнение обязательных полей формы"):
        ProductsPage(driver) \
            .fill_required_fields(p_name, p_meta_teg_title, p_model)
    with allure.step("Нажатие кнопки Save"):
        ButtonGroup(driver).save()
    with allure.step("Появление сообщения об успешном действии"):
        AlertMSG(driver).check_alert_success()


@allure.feature("Редактирование каталога товаров")
@allure.story("Редактирование карточки товара")
@allure.title("Редактирование карточки товара")
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

    with allure.step("Авторизация на странице администратора"):
        AdminPage(driver, url).open().login(login="Realdeal87", password="K1x9Z5b8!")
    with allure.step("Переход в раздел каталога Products"):
        NavigationBar(driver).catalog().products()
    with allure.step("Нажатие кнопки Edit напротив продукта"):
        ProductsPage(driver).edit_product(number=2)
    with allure.step("Добавление описания продукта"):
        ProductsPage(driver).fill_description(p_description)
    with allure.step("Нажатие кнопки Save"):
        ButtonGroup(driver).save()
    with allure.step("Появление сообщения об успешном действии"):
        AlertMSG(driver).check_alert_success()


@allure.feature("Редактирование каталога товаров")
@allure.story("Удаление карточки товара")
@allure.title("Удаление карточки товара")
def test_delete_products(driver, url):
    """Успешное удаление продуктов по заданному порядковому номеру и количеству"""

    with allure.step("Авторизация на странице администратора"):
        AdminPage(driver, url).open().login(login="Realdeal87", password="K1x9Z5b8!")
    with allure.step("Переход в раздел каталога Products"):
        NavigationBar(driver).catalog().products()
    with allure.step("Выбор продуктов"):
        ProductsPage(driver).choose_products(number=1, quantity=1)
    with allure.step("Нажатие кнопки Delete"):
        ButtonGroup(driver).delete().accept()
    with allure.step("Появление сообщения об успешном действии"):
        AlertMSG(driver).check_alert_success()
