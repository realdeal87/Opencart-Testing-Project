"""Модуль для проверки действий с базой данных OpenCart"""
import pytest
import pymysql
from pageobjects import MainPage


@pytest.fixture
def mysql_connector(request):
    """Фикстура для создания карточки покупателя и удаления ее после тестов"""
    # Значения хэш параметров password и salt соответствуют паролю "test"

    sql_insert = """INSERT INTO oc_customer (
                    customer_group_id, store_id, language_id, firstname, lastname, email,
                    telephone, fax, password, salt,
                    newsletter, address_id, custom_field, ip, status, safe, token, code, date_added)
                    VALUES (
                    1, 0, 1, "Tester", "Testerov", "test@test.com",
                    "777-77-77", "", "1ffb35ced82fed5e31001d854b637d587ff33043", "9ZUXV0GX8",
                    0, 0, "", "::1", 1, 0, "", "", "1000-01-01 00:00:01");"""

    sql_delete = """DELETE FROM oc_customer WHERE firstname = "Tester" AND lastname = "Testerov";"""

    conn = pymysql.connect(host="localhost", user="opencart_user",
                           password="opencartpassopencart", db="opencart")
    cursor = conn.cursor()
    cursor.execute(sql_insert)

    def fin():
        """Файнолайзер: удаление карточки покупателя, закрытие соединения"""
        cursor.execute(sql_delete)
        cursor.close()

    request.addfinalizer(fin)
    return cursor


def test_check_customer(driver, url, logging_test, mysql_connector):
    """Соответствие значения полей Имя и Фамилия из информации об аккаунте клиента на странице,
    значению параметров из базы данных"""
    MainPage(driver, url).open() \
        .login(email="test@test.com", password="test")
    parameters = MainPage(driver).checkout_information()
    assert parameters == ("Tester", "Testerov", "test@test.com", "777-77-77")

