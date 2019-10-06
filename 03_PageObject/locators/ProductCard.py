from selenium.webdriver.common.by import By
"""Локаторы для карточки товара сайта Opencart"""


class ProductCard:
    """Локаторы для карточки товара"""

    like_it_button = {'xpath': '//button[@data-original-title="Add to Wish List"]'}
    compare_button = {'xpath': '//button[@data-original-title="Compare this Product"]'}

    brand_link = "//ul[@class='list-unstyled']/li/a"

    dropdown_menu = "//ul[@class='dropdown-menu']/li"

    input_qty = {'id': 'input-quantity'}
    button_cart = {'id': 'button-cart'}

    product = {'link': None}

    class Thumbnails:
        """Локаторы для миниатюр"""
        thumbnails = {'class': 'thumbnail'}
        button_esc = {'css': '.mfp-close', 'xpath': '//button[@title="Close (Esc)"]'}
        picture = {'class': 'mfp-img'}
        arrow_left = {'xpath': '//button[@title="Previous (Left arrow key)"]'}
        arrow_right = {'xpath': '//button[@title="Next (Right arrow key)"]'}
