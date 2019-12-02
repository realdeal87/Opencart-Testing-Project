from selenium.webdriver.common.by import By
"""Локаторы для карточки товара сайта Opencart"""


class ProductCard:
    """Локаторы для карточки товара"""

    like_it_button = "//button[@data-original-title='Add to Wish List']"
    compare_button = "//button[@data-original-title='Compare this Product']"

    brand_link = "//ul[@class='list-unstyled']/li/a"

    input_qty = (By.ID, "input-quantity")
    button_cart = (By.ID, "button-cart")
    dropdown_menu = "//ul[@class='dropdown-menu']/li"

    alert_danger = (By.CLASS_NAME, "alert-danger")

    class Thumbnails:
        """Локаторы для миниатюр"""

        tumbnails = (By.CLASS_NAME, "thumbnail")
        button_esc = "//button[@title='Close (Esc)']"
        picture = (By.CLASS_NAME, "mfp-img")
        arrow_left = "//button[@title='Previous (Left arrow key)']"
        arrow_right = "//button[@title='Next (Right arrow key)']"
