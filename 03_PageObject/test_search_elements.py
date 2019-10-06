"""Тестовые сценарии для проверки функционала сайта Opencart"""
from pageobjects import AdminPage, AlertMSG, BasePage, MainPage, MenuBar


def test_search(driver, url):
    """Поиск продуктов Canon, добавление найденного продукта в отслеживаемые,
    получение успешного алертинга"""
    MainPage(driver, url).open() \
        .search_element("Canon") \
        .add_to_wishlist(number=1)
    AlertMSG(driver).check_alert_success()


def test_catalog(driver, url):
    """Добавление двух мониторов в каталога для сравнения, получение алертингов"""
    MainPage(driver, url).open()
    MenuBar(driver).components().monitors()
    MainPage(driver).add_to_compare(number=1)
    AlertMSG(driver).check_alert_success()
    MainPage(driver).add_to_compare(number=2)
    AlertMSG(driver).check_alert_success()


def test_cart(driver, url):
    """Переход к карточке iPhone, ввод в поле Qty валидного значения,
    добавление в корзину, получение алертинга"""
    MainPage(driver, url).open() \
        .choose_product("iPhone") \
        .add_to_cart(quantity=5)
    AlertMSG(driver).check_alert_success()


def test_pictures(driver, url):
    """Переход к карточке MacBook, просмотр всех фото, добавление в корзину,
    открытие dropdown-menu"""
    MainPage(driver, url).open() \
        .choose_product("MacBook") \
        .list_images(quantity=3) \
        .add_to_cart(quantity=3)
    AlertMSG(driver).check_alert_success()


def test_admin_page(driver, url):
    """Вход в панель администратора с невалидными данными, получение алертинга с ошибкой"""
    AdminPage(driver, url).open().login(login="xxx", password="xxx")
    AlertMSG(driver).check_alert_danger()
