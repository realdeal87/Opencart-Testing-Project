"""Локаторы для главной страницы сайта Opencart"""


class MainPage:
    """Локаторы для главной страницы"""

    class Header:
        """Локаторы для хедера"""
        logo_link = ("id", "logo")
        button_cart = "//div[@id='cart']/button"
        cart_count = "//span[@id='cart-total']/text()"

    class MenuBar:
        """Локаторы для меню"""
        menu_element = ("class name", "dropdown")
        see_all = "Show All"

    class Promo:
        """Локаторы для промоблока"""
        product_thumb = ("class name", "product-thumb")
        image_link = "//div[@class='image']/a"
        product_link = "//div[@class='caption']/h4/a"
        button_group = "//div[@class='button-group']/button"

    class Footer:
        """Локаторы для футера"""
        link_site_map = "Site Map"
        link_monitors = "Monitors"

    class Search:
        """Локаторы для поисковой строки"""
        search_field = ("name", "search")
        search_button = "//div[@id='search']/span/button"

    alert_success = ("class name", "alert-success")
    alert_danger = ("class name", "alert-danger")
