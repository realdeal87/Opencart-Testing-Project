"""Локаторы для раздела каталога сайта Opencart"""


class DirPart:
    """Локаторы для раздела каталога"""

    breadcrumbs = {'class': 'breadcrumb'}

    sidebar_items = {'class': 'list-group'}

    refine_search = {'xpath': '//div[@class="col-sm-3"]/ul/li'}

    button_list = {'id': 'list-view'}
    button_grid = {'id': 'grid-view'}

    compare = {'id': 'compare-total'}

    compare_count = {'xpath': '//td/input[@value="Add to Cart"]'}
