"""Дополнительные тестовые сценарии для сайта Opencart"""
import allure
from pageobjects import AdminBar, AdminPage, AlertMSG, ButtonGroup,\
    DashBoardPage, NavigationBar, ProductsPage, ProfilePage


@allure.feature("Редактирование каталога товаров")
@allure.story("Копирование карточки товара")
@allure.title("Копирование карточки товара")
def test_copy_product(driver, url):
    """Копирование выбранных продуктов"""
    with allure.step("Авторизация на странице администратора"):
        AdminPage(driver, url).open().login(login="Realdeal87", password="K1x9Z5b8!")
    with allure.step("Переход в раздел каталога Products"):
        NavigationBar(driver).catalog().products()
    with allure.step("Выбор продуктов"):
        ProductsPage(driver).choose_products(number=2, quantity=2)
    with allure.step("Нажатие кнопки Copy"):
        ButtonGroup(driver).copy()
    with allure.step("Появление сообщения об успешном действии"):
        AlertMSG(driver).check_alert_success()


@allure.feature("Настройки")
@allure.story("Очистка кеша темы")
@allure.title("Очистка кеша темы")
def test_clearing_theme_cache(driver, url):
    """Очистка кеша темы в настройках"""
    with allure.step("Авторизация на странице администратора"):
        AdminPage(driver, url).open().login(login="Realdeal87", password="K1x9Z5b8!")
    with allure.step("Переход в настройки"):
        DashBoardPage(driver).settings()
    with allure.step("Очистка кеша"):
        DashBoardPage(driver).refresh_theme_cache()
    with allure.step("Появление сообщения об успешном действии"):
        AlertMSG(driver).check_alert_success()


@allure.feature("Авторизация")
@allure.story("Выход из панели администратора")
@allure.title("Выход из панели администратора")
def test_logout(driver, url):
    """Выход из панели администратора"""
    with allure.step("Авторизация на странице администратора"):
        AdminPage(driver, url).open().login(login="Realdeal87", password="K1x9Z5b8!")
    with allure.step("Выход из аккаунта администратора"):
        AdminBar(driver).logout()
    with allure.step("Сравнение заголовка страницы"):
        assert AdminPage(driver).title() == "Administration"


@allure.feature("Авторизация")
@allure.story("Отправка почтового ящика")
@allure.title("Отправка почтового ящика")
def test_invalid_email(driver, url):
    """Отправка невалидного значения почтового ящика для восстановления пароля"""
    with allure.step("Переход на страницу восстановления пароля"):
        AdminPage(driver, url).open()
    with allure.step("Отправка невалидного значения почтового ящика"):
        AdminPage(driver, url).forgotten_password("Test")
    with allure.step("Появление сообщения о неуспешном действии"):
        AlertMSG(driver).check_alert_danger()


@allure.feature("Настройки")
@allure.story("Сохранение информации в профайле")
@allure.title("Сохранение информации в профайле")
def test_save_profile(driver, url):
    """Сохранение информации в профайле"""
    with allure.step("Авторизация на странице администратора"):
        AdminPage(driver, url).open().login(login="Realdeal87", password="K1x9Z5b8!")
    with allure.step("Переход в профиль аккаунта"):
        AdminBar(driver).your_profile()
    with allure.step("Сохранение изменений"):
        ProfilePage(driver).save_changes()
    with allure.step("Появление сообщения об успешном действии"):
        AlertMSG(driver).check_alert_success()
