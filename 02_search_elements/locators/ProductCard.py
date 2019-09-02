"""Локаторы для карточки товара сайта Opencart"""


class ProductCard:
    """Локаторы для карточки товара"""

    like_it_button = "//button[@data-original-title='Add to Wish List']"
    compare_button = "//button[@data-original-title='Compare this Product']"

    brand_link = "//ul[@class='list-unstyled']/li/a"

    input_qty = ("id", "input-quantity")
    button_cart = ("id", "button-cart")

    class Thumbnails:
        """Локаторы для миниатюр"""

        tumbnails = ("class name", "thumbnail")
        button_esc = "//button[@title='Close (Esc)']"
        picture = ("class name", "mfp-img")
        arrow_left = "//button[@title='Previous (Left arrow key)']"
        arrow_right = "//button[@title='Next (Right arrow key)']"
