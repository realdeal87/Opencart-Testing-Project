class Products:
    """Локаторы для страницы продуктов"""
    add_new_button = {'css': 'a.btn:nth-child(2)'}
    copy_button = {'css': 'button.btn:nth-child(3)'}
    delete_button = {'css': 'button.btn:nth-child(4)'}

    checkbox_all = {'css': '.table > thead:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > input:nth-child(1)'}
    checkbox = {'name': 'selected[]'}
    edit_buttons = {'xpath': '//a[@data-original-title="Edit"]'}

    # checkbox = {'f-css': '.table > tbody:nth-child(2) > tr:nth-child({}) > td:nth-child(1) > input:nth-child(1)'}
    # edit_buttons = {'f-css': '.table > tbody:nth-child(2) > tr:nth-child({}) > td:nth-child(8) > a:nth-child(1)'}

    trows = {'xpath': '//tbody/tr'}

    class ProductEdit:
        """Локаторы для страницы редактирования продукта"""
        general_link = {'link': 'General'}
        product_name = {'id': 'input-name1'}
        meta_teg_title = {'id': 'input-meta-title1'}
        description_area = {'class': 'note-editable'}
        description_area_edited = {'css': '.note-editable > p:nth-child(1)'}

        data_link = {'link': 'Data'}
        model = {'id': 'input-model'}

        save_button = {'css': 'div.pull-right > button:nth-child(1)'}
        cancel_button = {'css': 'a.btn'}
