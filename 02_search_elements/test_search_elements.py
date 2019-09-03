"""Тестовые сценарии для проверки функционала сайта Opencart"""
import time
from locators import DirPart, LoginPanel, MainPage, ProductCard


def test_search(browser_driver):
    """Поиск продуктов Canon, добавление найденного продукта в отслеживаемые,
    получение успешного алертинга"""
    browser_driver.find_element(*MainPage.Search.search_field).send_keys("Canon")
    browser_driver.find_element_by_xpath(MainPage.Search.search_button).click()
    product_keys = browser_driver.find_elements_by_xpath(MainPage.Promo.button_group)
    product_keys[1].click()
    browser_driver.find_element(*MainPage.alert_success)


def test_catalog(browser_driver):
    """Добавление двух мониторов из каталога для сравнения"""
    browser_driver.find_element_by_link_text(MainPage.Footer.link_site_map).click()
    browser_driver.find_element_by_link_text(MainPage.Footer.link_monitors).click()
    browser_driver.find_element(*DirPart.button_list).click()
    product_keys = browser_driver.find_elements_by_xpath(MainPage.Promo.button_group)
    product_keys[2].click()
    time.sleep(2)
    product_keys[5].click()
    browser_driver.find_element(*DirPart.compare).click()
    assert len(browser_driver.find_elements_by_xpath(DirPart.compare_count)) == 2


def test_card(browser_driver):
    """Переход к карточке iPhone, ввод в поле Qty невалидного значения,
    добавление в корзину, получение алертинга с ошибкой"""
    products = browser_driver.find_elements_by_xpath(MainPage.Promo.image_link)
    products[1].click()
    browser_driver.find_element(*ProductCard.input_qty).clear()
    browser_driver.find_element(*ProductCard.input_qty).send_keys("BreakIt")
    browser_driver.find_element(*ProductCard.button_cart).click()
    browser_driver.find_element(*ProductCard.alert_danger)


def test_pictures(browser_driver):
    """Переход к карточке MacBook, просмотр всех фото, добавление в корзину,
    открытие dropdown-menu"""
    products = browser_driver.find_elements_by_xpath(MainPage.Promo.image_link)
    products[0].click()
    pictures = browser_driver.find_elements(*ProductCard.Thumbnails.tumbnails)
    pictures[0].click()
    for _ in pictures:
        browser_driver.find_element_by_xpath(ProductCard.Thumbnails.arrow_right).click()
    browser_driver.find_element_by_xpath(ProductCard.Thumbnails.button_esc).click()
    browser_driver.find_element(*ProductCard.button_cart).click()
    browser_driver.find_element_by_xpath(MainPage.Header.button_cart).click()
    browser_driver.find_element_by_xpath(ProductCard.dropdown_menu)


def test_admin_panel(browser_driver, url):
    """Вход в панель администратора с невалидными данными, получение алертинга с ошибкой"""
    browser_driver.get(url + "/admin")
    browser_driver.find_element(*LoginPanel.LoginDetails.input_username).send_keys("xxx")
    browser_driver.find_element(*LoginPanel.LoginDetails.input_password).send_keys("xxx")
    browser_driver.find_element_by_xpath(LoginPanel.LoginDetails.login_button).submit()
    browser_driver.find_element(*LoginPanel.LoginDetails.alert_danger)
    # # Проверка с валидными данными:
    # browser_driver.find_element(*LoginPanel.Dashboard.dashboard_nav)
