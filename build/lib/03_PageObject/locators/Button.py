"""Локаторы для группы кнопок в панели администратора сайта Opencart"""


class Button:
    """Локаторы для группы кнопок"""
    add_new_button = {'xpath': '//a[@data-original-title="Add New"]'}
    copy_button = {'css': 'button.btn:nth-child(3)'}
    delete_button = {'css': 'button.btn:nth-child(4)'}

    save_button = {'css': 'div.pull-right > button:nth-child(1)'}
    cancel_button = {'css': 'a.btn'}
