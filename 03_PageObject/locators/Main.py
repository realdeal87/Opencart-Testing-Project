"""Локаторы для главной страницы сайта Opencart"""


class Main:
    """Локаторы для главной страницы"""

    class Header:
        """Локаторы для хедера"""
        logo_link = {'id': 'logo'}
        button_cart = {'xpath': '//div[@id="cart"]/button'}
        cart_count = {'xpath': '//span[@id="cart-total"]/text()'}

    class MenuBar:
        """Локаторы для меню"""
        menu_element = {'class': 'dropdown'}
        see_all = {'link': 'Show All'}

    class Promo:
        """Локаторы для промоблока"""
        product_thumb = {'class': 'product-thumb'}
        image_link = {'xpath': '//div[@class="image"]/a'}
        product_link = {'xpath': '//div[@class="caption"]/h4/a'}
        button_group = {'xpath': '//div[@class="button-group"]/button'}

    class Footer:
        """Локаторы для футера"""
        link_site_map = {'link': 'Site Map'}
        link_monitors = {'link': 'Monitors'}

    class Search:
        """Локаторы для поисковой строки"""
        search_field = {'name': 'search'}
        search_button = {'css': '.btn-default'}
