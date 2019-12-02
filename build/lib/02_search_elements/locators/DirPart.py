from selenium.webdriver.common.by import By
"""Локаторы для раздела каталога сайта Opencart"""


class DirPart:
    """Локаторы для раздела каталога"""

    breadcrumbs = (By.CLASS_NAME, "breadcrumb")

    sidebar_items = (By.CLASS_NAME, "list-group")

    refine_search = "//div[@class='col-sm-3']/ul/li"

    button_list = (By.ID, "list-view")
    button_grid = (By.ID, "grid-view")

    compare = (By.ID, "compare-total")

    compare_count = "//td/input[@value='Add to Cart']"
