"""Тестовые сценарии для проверки загрузки файлов в формах сайта Opencart"""
from pageobjects import AdminPage, AlertMSG, ButtonGroup, DownloadsPage, NavigationBar, ProductsPage


def test_upload_file(driver, url):
    """Добавление файла в форму загрузки"""

    file = "Alcatel_OT_890_EN.pdf"
    download_name = "Alcatel OT-890 Manual"

    AdminPage(driver, url).open().login(login="Realdeal87", password="K1x9Z5b8!")
    NavigationBar(driver).catalog().downloads()
    ButtonGroup(driver).add_new()
    DownloadsPage(driver).upload_file(file, download_name)
    ButtonGroup(driver).save()
    AlertMSG(driver).check_alert_success()


def test_create_product_plus(driver, url):
    """Успешное добавление продукта с заполнением требуемых полей и фотографии товара"""

    p_name = "Alcatel OT-890"
    p_meta_teg_title = "Android 2.1"
    p_model = "Product 2011"
    p_photo = "OT890.jpg"

    AdminPage(driver, url).open().login(login="Realdeal87", password="K1x9Z5b8!")
    NavigationBar(driver).catalog().products()
    ButtonGroup(driver).add_new()
    ProductsPage(driver) \
        .fill_required_fields(p_name, p_meta_teg_title, p_model) \
        .upload_new_image(p_photo) \
        .choose_image(p_photo)
    ButtonGroup(driver).save()
    AlertMSG(driver).check_alert_success()
