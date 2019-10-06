from selenium.webdriver.common.by import By
"""Локаторы для главной страницы сайта Opencart"""


class Main:
    """Локаторы для главной страницы"""

    class Header:
        """Локаторы для хедера"""
        logo_link = (By.ID, "logo")
        button_cart = "//div[@id='cart']/button"
        cart_count = "//span[@id='cart-total']/text()"

    class MenuBar:
        """Локаторы для меню"""
        menu_element = (By.CLASS_NAME, "dropdown")
        see_all = "Show All"

    class Promo:
        """Локаторы для промоблока"""
        product_thumb = (By.CLASS_NAME, "product-thumb")
        image_link = "//div[@class='image']/a"
        product_link = "//div[@class='caption']/h4/a"
        button_group = "//div[@class='button-group']/button"

    class Footer:
        """Локаторы для футера"""
        link_site_map = "Site Map"
        link_monitors = "Monitors"

    class Search:
        """Локаторы для поисковой строки"""
        search_field = {'name': 'search'}
        search_button = {'css': '.btn-default'}
