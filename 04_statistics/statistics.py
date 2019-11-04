"""Модуль для парсинга файлов логов сервера apache или nginx"""
import argparse
import json
import os
import re


def log_parser(file, max_lines, prepared):
    """Функция обрабатывает строки файла логов"""

    count = 0
    methods = {"GET": 0, "POST": 0, "PUT": 0, "PATH": 0, "DELETE": 0, "COPY": 0, "HEAD": 0,
               "OPTIONS": 0, "LINK": 0, "UNLINK": 0, "PURGE": 0, "LOCK": 0, "UNLOCK": 0,
               "PROPFIND": 0, "VIEW": 0}
    top_ip = {}
    top_long = {}
    top_400 = {}
    top_500 = {}

    for request in file:
        try:
            line_length = len(request)
            i = 0
            req_params = list()
            # Парсинг по регулярному выражению
            while i < line_length:
                for pattern, token_type in prepared:
                    match = pattern.match(request, i)
                    if match is None:
                        continue
                    i = match.end()
                    if match.group(0) not in (' ', '\n'):
                        req_params.append(match.group(0))

            ip_add = req_params[0]
            method = req_params[4].replace('"', '').split(' ')[0]
            code = req_params[5]
            length = int(req_params[6])
            url = req_params[7].replace('"', '')

            # Добавление записи в словарь ip адресов
            if ip_add not in top_ip:
                top_ip[ip_add] = 1
            else:
                top_ip[ip_add] += 1

            # Добавление записи в словарь методов
            if (method, url, ip_add, length) not in top_long:
                top_long[(method, url, ip_add, length)] = [length, 1]
            else:
                top_long[(method, url, ip_add, length)][1] += 1

            # Добавление записи в словарь ошибок клиента
            if code.startswith("4"):
                if (method, url, code, ip_add) not in top_400:
                    top_400[(method, url, code, ip_add)] = 1
                else:
                    top_400[(method, url, code, ip_add)] += 1

            # Добавление записи в словарь ошибок сервера
            if code.startswith("5"):
                if (method, url, code, ip_add) not in top_500:
                    top_500[(method, url, code, ip_add)] = 1
                else:
                    top_500[(method, url, code, ip_add)] += 1

            methods[method] += 1
            count += 1

            if count == max_lines:
                break

        except (KeyError, ValueError) as err:
            print("Ошибка при обработке файла лога")
            print(err)
            os.abort()

    return count, methods, top_ip, top_long, top_400, top_500


def sorter(dic, param):
    """Функция сортирует полученные записи в порядке убывания и состовляет словарь
    из 10 первых записей"""
    j = 0
    top_10 = {}
    top = list(dic.items())
    top.sort(key=lambda k: k[1])
    top.reverse()
    for _ in top:
        if param == 0:
            top_10[j + 1] = {"Quantity": top[j][1], "IP address": top[j][0]}
        if param == 1:
            top_10[j + 1] = {"Quantity": top[j][1][1], "Method": top[j][0][0],
                             "URL": top[j][0][1], "IP address": top[j][0][2],
                             "Length": top[j][0][3]}
        if param == 2:
            top_10[j + 1] = {"Quantity": top[j][1], "Method": top[j][0][0], "URL": top[j][0][1],
                             "Status code": top[j][0][2], "IP address": top[j][0][3]}
        j += 1
        if j == 10:
            break
    while j < 10:
        top_10[j + 1] = None
        j += 1
    return top_10


def lexer():
    """Функция компилирует регулярное выражение, с помощью которого парсятся
    строки файла логов"""
    wsp, quoted_string, date, raw, no_data = range(5)
    rules = [
        (r'\s+', wsp),
        (r'-|"-"', no_data),
        (r'"([^"]+)"', quoted_string),
        (r'\[([^\]]+)\]', date),
        (r'([^\s]+)', raw),
    ]
    prepared = [(re.compile(regexp), token_type) for regexp, token_type in rules]
    return prepared


def main():
    """Главная функция. Получение аргументов командной строки, открытие файлов
    логов для обработки"""

    parser = argparse.ArgumentParser()

    parser.add_argument("--path", "-p",
                        action="store",
                        help="Абсолютный путь к файлам логов для парсинга. По умолчанию директория,"
                             "из которой запускается скрипт. Использовать: --path=<путь>",
                        default=os.getcwd())

    parser.add_argument("--file", "-f",
                        action="store",
                        help="Файл лога для обработки. По умолчанию, обрабатываются все файлы"
                             "с раширением log в директории. Использовать: --file=<файл>")

    parser.add_argument("--lines", "-l",
                        action="store",
                        type=int,
                        help="Количество обрабатываемых строк в файлах. По умолчанию все строки."
                             "Использовать: --lines=<int>")

    args = parser.parse_args()

    # Добавление одного файла логов или всех файлов логов в каталоге
    if args.file:
        files = list()
        files.append(args.file)
        if not args.file.endswith(".log"):
            raise TypeError("Обрабатываются только файлы с расширением .log")
    else:
        files = [file for file in os.listdir(args.path) if file.endswith(".log")]

    prep = lexer()

    for file in files:
        # Открытие файла логов для обработки
        with open(args.path + "/" + file, "r") as parsing_file:
            stat = log_parser(parsing_file, args.lines, prep)

            top_10_ip = sorter(stat[2], 0)
            top_10_long = sorter(stat[3], 1)
            top_10_400 = sorter(stat[4], 2)
            top_10_500 = sorter(stat[5], 2)

            statistics = {"Total requests": stat[0], "Methods quantity": stat[1],
                          "Top 10 IP addresses": top_10_ip,
                          "Top 10 requests with maximum length": top_10_long,
                          "Top 10 requests with 4xx status code": top_10_400,
                          "Top 10 requests with 5xx status code": top_10_500}

        # Сохранение json файла со статистикой
        file = file[0:-3] + "json"
        with open(args.path + "/" + file, "w") as json_file:
            json.dump(statistics, json_file)


if __name__ == "__main__":
    main()
