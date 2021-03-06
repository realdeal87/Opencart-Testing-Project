# Opencart-Testing-Project
Testing Opencart with Selenium

Занятие №7
Задание:
1. Описать элементы на страницах:
- Главная (Шапка, разделы меню, промоблок, футер, поисковая строка)
- Карточка товара
- Раздел каталога
- Панель логина /admin/

2. Реализовать 5 тестовых сценариев, в основе которых будут лежать поиск элементов и элементарные действия
(click, submit, input) и задействованы все описанные страницы

Требования:
Тесты проходят в браузерах firefox, chrome (ie, safari - опционально).
Локаторы используются из отдельного пакета с локаторами.
Тесты независимы друг от друга.
В коде отсутсвуют грубые нарушения PEP8.
url можно передать параметром, браузер можно передать параметром (есть значения по умолчанию)

В качестве решения предоставить ссылку на код и скриншот проверок pylint.

Запуск: pytest -vs test_search_elements.py --browser={Chrome, Firefox}


Занятие №8
Задание:
1. Для страницы Products реализовать тесты, которые проверяют функциональность добавления, изменения и удаления продукта

Требования:
Тесты проходят в браузерах firefox, chrome.
Отсутствуют дублирующиеся и захардкоженные локаторы в методах.
Тесты независимы друг от друга.
Код легко поддерживать и изменять.
Код проходит успешно проверки pylint.

В качестве решения предоставить ссылку на коммит и скриншот проверок pylint

Запуск: pytest -vs test_crud_products.py --browser={Chrome, Firefox}


Занятие №10
Задание:
1. Добавить ожидания элементов и обработку исключений для тестов страницы Products

2. Добавить ожидание в настройки браузера перед тестом

3. Добавить опцию выставления ожидания для браузера в опции командной строки

Критерии оценки: Тесты проходят в браузерах firefox, chrome.
Отсутствуют дублирующиеся и захардкоженные локаторы в методах.
Тесты независимы друг от друга.
Код легко поддерживать и изменять.
Код проходит успешно проверки pylint.

В качестве решения предоставить ссылку на коммит и скриншот проверок pylint.

Запуск: pytest -vs test_crud_products.py --browser={Chrome, Firefox} --waiting=0