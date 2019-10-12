"""Локаторы для раздела Products панели администратора сайта Opencart"""


class Products:
    """Локаторы для раздела каталога Products"""

    checkbox_all = {'css': '.table > thead:nth-child(1) > tr:nth-child(1)'
                           ' > td:nth-child(1) > input:nth-child(1)'}

    checkbox = {'name': 'selected[]'}
    edit_buttons = {'xpath': '//a[@data-original-title="Edit"]'}

    trows = {'xpath': '//tbody/tr'}

    input_name = {'id': 'input-name'}
    input_model = {'id': 'input-model'}
    input_price = {'id': 'input-price'}
    input_quantity = {'id': 'input-quantity'}
    button_filter = {'id': 'button-filter'}

    class ProductEdit:
        """Локаторы для страницы редактирования продукта"""
        general_link = {'link': 'General'}
        product_name = {'id': 'input-name1'}
        meta_teg_title = {'id': 'input-meta-title1'}
        description_area = {'class': 'note-editable'}
        description_area_edited = {'css': '.note-editable > p:nth-child(1)'}

        data_link = {'link': 'Data'}
        model = {'id': 'input-model'}

        image_link = {'link': 'Image'}
        thumb_image = {'id': 'thumb-image'}
        button_image = {'id': 'button-image'}
        button_clear = {'id': 'button-clear'}

        filemanager = {'id': 'filemanager'}
        button_upload = {'id': 'button-upload'}

