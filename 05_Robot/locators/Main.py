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

    class CustomerMenu:
        """Локаторы для меню покупателя"""
        my_account = {'xpath': '//a[@title="My Account"]'}
        login = {'link': 'Login'}

    class Login:
        email = {'id': 'input-email'}
        password = {'id': 'input-password'}
        login_button = {'xpath': '//input[@value="Login"]'}

    class MyAccount:
        my_account = {'link': 'Edit your account information'}

    class MyAccountInformation:
        firstname = {'id': 'input-firstname'}
        lastname = {'id': 'input-lastname'}
        email = {'id': 'input-email'}
        telephone = {'id': 'input-telephone'}


