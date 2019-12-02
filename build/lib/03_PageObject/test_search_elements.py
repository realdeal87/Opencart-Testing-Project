"""Тестовые сценарии для проверки функционала сайта Opencart"""
import allure
from pageobjects import AdminPage, AlertMSG, MainPage, MenuBar


@allure.feature("Действия с товарами")
@allure.story("Поиск товара")
@allure.title("Поиск товара")
def test_search(driver, url):
    """Поиск продуктов Canon, добавление найденного продукта в отслеживаемые,
    получение успешного алертинга"""
    with allure.step("Переход на главную страницу"):
        MainPage(driver, url).open()
    with allure.step("Поиск продукта"):
        MainPage(driver).search_element("Canon")
    with allure.step("Добавление в список желаемых"):
        MainPage(driver).add_to_wishlist(number=1)
    with allure.step("Появление сообщения об успешном действии"):
        AlertMSG(driver).check_alert_success()


@allure.feature("Действия с товарами")
@allure.story("Добавление для сравнения")
@allure.title("Добавление для сравнения")
def test_catalog(driver, url):
    """Добавление двух мониторов в каталога для сравнения, получение алертингов"""
    with allure.step("Переход на главную страницу"):
        MainPage(driver, url).open()
    with allure.step("Переход на страницу каталога Мониторы"):
        MenuBar(driver).components().monitors()
    with allure.step("Добавить товар 1 для сравнения"):
        MainPage(driver).add_to_compare(number=1)
    with allure.step("Появление сообщения об успешном действии"):
        AlertMSG(driver).check_alert_success()
    with allure.step("Добавить товар 2 для сравнения"):
        MainPage(driver).add_to_compare(number=2)
    with allure.step("Появление сообщения об успешном действии"):
        AlertMSG(driver).check_alert_success()


@allure.feature("Действия с товарами")
@allure.story("Добавление в корзину")
@allure.title("Добавление в корзину")
def test_cart(driver, url):
    """Переход к карточке iPhone, ввод в поле Qty валидного значения,
    добавление в корзину, получение алертинга"""
    with allure.step("Переход на главную страницу"):
        MainPage(driver, url).open()
    with allure.step("Выбор продукта"):
        MainPage(driver).choose_product("iPhone")
    with allure.step("Добавление продуктов в корзину"):
        MainPage(driver).add_to_cart(quantity=5)
    with allure.step("Появление сообщения об успешном действии"):
        AlertMSG(driver).check_alert_success()


@allure.feature("Действия с товарами")
@allure.story("Просмотр изображений")
@allure.title("Просмотр изображений")
def test_pictures(driver, url):
    """Переход к карточке MacBook, просмотр всех фото, добавление в корзину,
    открытие dropdown-menu"""
    with allure.step("Переход на главную страницу"):
        MainPage(driver, url).open()
    with allure.step("Выбор продукта"):
        MainPage(driver).choose_product("MacBook")
    with allure.step("Просмотр изображение продукта"):
        MainPage(driver).list_images(quantity=3)
    with allure.step("Добавление продуктов в корзину"):
        MainPage(driver).add_to_cart(quantity=3)
    with allure.step("Появление сообщения об успешном действии"):
        AlertMSG(driver).check_alert_success()


@allure.feature("Авторизация")
@allure.story("Вход с невалидными данными")
@allure.title("Вход с невалидными данными")
def test_admin_page(driver, url):
    """Вход в панель администратора с невалидными данными, получение алертинга с ошибкой"""
    with allure.step("Авторизация на странице администратора"):
        AdminPage(driver, url).open().login(login="xxx", password="xxx")
    with allure.step("Появление сообщения об успешном действии"):
        AlertMSG(driver).check_alert_danger()
