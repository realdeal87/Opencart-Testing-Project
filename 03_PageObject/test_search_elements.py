"""Тестовые сценарии для проверки функционала сайта Opencart"""
from pageobjects import AdminPage, BasePage, DashBoard, MainPage


def test_search(driver, url):
    """Поиск продуктов Canon, добавление найденного продукта в отслеживаемые,
    получение успешного алертинга"""
    MainPage(driver).open(url) \
        .Header(driver).search_element("Canon")
    MainPage(driver).add_to_wishlist(number=1)


def test_catalog(driver, url):
    """Добавление двух мониторов из каталога для сравнения"""
    MainPage(driver).open(url) \
        .MenuBar(driver).components().monitors()
    MainPage(driver).compare_elements(number1=1, number2=2)


def test_card(driver, url):
    """Переход к карточке iPhone, ввод в поле Qty невалидного значения,
    добавление в корзину, получение алертинга с ошибкой"""
    MainPage(driver).open(url) \
        .Featured(driver).choose_product("iPhone")
    MainPage(driver).add_to_cart(quantity=5)


def test_pictures(driver, url):
    """Переход к карточке MacBook, просмотр всех фото, добавление в корзину,
    открытие dropdown-menu"""
    MainPage(driver).open(url) \
        .Featured(driver).choose_product("MacBook")
    MainPage(driver).list_images() \
        .add_to_cart(quantity=3)


def test_admin_page(driver, url):
    """Вход в панель администратора с невалидными данными, получение алертинга с ошибкой"""
    AdminPage(driver).open(url).login(login="xxx", password="xxx")
