"""Тестовые сценарии для проверки загрузки файлов в формах сайта Opencart"""
import allure
from pageobjects import AdminPage, AlertMSG, ButtonGroup, DownloadsPage, NavigationBar, ProductsPage


@allure.feature("Настройки")
@allure.story("Загрузка файла")
@allure.title("Загрузка файла")
def test_upload_file(driver, url):
    """Добавление файла в форму загрузки"""

    file = "Alcatel_OT_890_EN.pdf"
    download_name = "Alcatel OT-890 Manual"

    with allure.step("Авторизация на странице администратора"):
        AdminPage(driver, url).open().login(login="Realdeal87", password="K1x9Z5b8!")
    with allure.step("Переход в раздел каталога Downloads"):
        NavigationBar(driver).catalog().downloads()
    with allure.step("Нажатие кнопки Add New"):
        ButtonGroup(driver).add_new()
    with allure.step("Загрузка файла"):
        DownloadsPage(driver).upload_file(file, download_name)
    with allure.step("Нажатие кнопки Save"):
        ButtonGroup(driver).save()
    with allure.step("Появление сообщения об успешном действии"):
        AlertMSG(driver).check_alert_success()


@allure.feature("Редактирование каталога товаров")
@allure.story("Загрузка изображения")
@allure.title("Загрузка изображения")
def test_create_product_plus(driver, url):
    """Успешное добавление продукта с заполнением требуемых полей и фотографии товара"""

    p_name = "Alcatel OT-890"
    p_meta_teg_title = "Android 2.1"
    p_model = "Product 2011"
    p_photo = "OT890.jpg"

    with allure.step("Авторизация на странице администратора"):
        AdminPage(driver, url).open().login(login="Realdeal87", password="K1x9Z5b8!")
    with allure.step("Переход в раздел каталога Products"):
        NavigationBar(driver).catalog().products()
    with allure.step("Нажатие кнопки Add New"):
        ButtonGroup(driver).add_new()
    with allure.step("Заполнение обязательных полей формы"):
        ProductsPage(driver) \
            .fill_required_fields(p_name, p_meta_teg_title, p_model)
    with allure.step("Добавление изображения"):
        ProductsPage(driver).upload_new_image(p_photo)
    with allure.step("Установка изображения"):
        ProductsPage(driver).choose_image(p_photo)
    with allure.step("Нажатие кнопки Save"):
        ButtonGroup(driver).save()
    with allure.step("Появление сообщения об успешном действии"):
        AlertMSG(driver).check_alert_success()
