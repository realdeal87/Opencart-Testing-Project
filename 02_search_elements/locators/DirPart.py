"""Локаторы для раздела каталога сайта Opencart"""


class DirPart:
    """Локаторы для раздела каталога"""

    breadcrumbs = ("class name", "breadcrumb")

    sidebar_items = ("class name", "list-group")

    refine_search = "//div[@class='col-sm-3']/ul/li"

    button_list = ("id", "list-view")
    button_grid = ("id", "grid-view")

    compare = ("id", "compare-total")

    compare_count = "//td/input[@value='Add to Cart']"
