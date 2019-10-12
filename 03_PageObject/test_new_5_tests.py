"""Дополнительные тестовые сценарии для сайта Opencart"""
from pageobjects import AdminBar, AdminPage, AlertMSG, ButtonGroup,\
    DashBoardPage, NavigationBar, ProductsPage, ProfilePage


def test_copy_product(driver, url):
    """Копирование выбранных продуктов"""
    AdminPage(driver, url).open().login(login="Realdeal87", password="K1x9Z5b8!")
    NavigationBar(driver).catalog().products()
    ProductsPage(driver) \
        .choose_products(number=2, quantity=2)
    ButtonGroup(driver).copy()
    AlertMSG(driver).check_alert_success()


def test_clearing_theme_cache(driver, url):
    """Очистка кеша темы в настройках"""
    AdminPage(driver, url).open().login(login="Realdeal87", password="K1x9Z5b8!")
    DashBoardPage(driver) \
        .settings() \
        .refresh_theme_cache()
    AlertMSG(driver).check_alert_success()


def test_logout(driver, url):
    """Выход из панели администратора"""
    AdminPage(driver, url).open().login(login="Realdeal87", password="K1x9Z5b8!")
    AdminBar(driver).logout()
    assert AdminPage(driver).title() == "Administration"


def test_invalid_email(driver, url):
    """Отправка невалидного значения почтового ящика для восстановления пароля"""
    AdminPage(driver, url).open() \
        .forgotten_password("Test")
    AlertMSG(driver).check_alert_danger()


def test_save_profile(driver, url):
    """Сохранение информации в профайле"""
    AdminPage(driver, url).open().login(login="Realdeal87", password="K1x9Z5b8!")
    AdminBar(driver).your_profile()
    ProfilePage(driver).save_changes()
    AlertMSG(driver).check_alert_success()
