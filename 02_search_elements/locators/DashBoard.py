"""Локаторы для панели администратора"""
from selenium.webdriver.common.by import By


class DashBoard:
    """Локаторы для панели администратора"""

    dashboard_nav = (By.ID, "navigation")

    catalog_link = "Catalog"
    products_link = "Products"

    class Products:
        """Локаторы для меню"""
        add_new_button = "//a[@data-original-title='Add New']"
        copy_button = "//button[@data-original-title='Copy']"
        delete_button = "//button[@data-original-title='Delete']"
        edit_buttons = "//a[@data-original-title='Edit']"
        trows = "//tbody/tr"

        class ProductEdit:
            """Локаторы для страницы редактирования продукта"""
            general_link = "General"
            product_name = (By.ID, "input-name1")
            description_area = (By.CLASS_NAME, "note-editable")
            meta_teg_title = (By.ID, "input-meta-title1")

            data_link = "Data"
            model = (By.ID, "input-model")

            save_button = "//button[@data-original-title='Save']"
            cancel_button = "//a[@data-original-title='Cancel']"
