"""Модуль генерирует файл логов сервера apache или nginx"""
import random

IP_ADDRESSES = ("192.168.12.7", "192.168.12.4", "192.168.0.40", "192.168.4.108",
                "10.24.177.55", "10.24.177.1", "10.24.177.255", "10.24.177.190",
                "95.120.254.0", "::1")

METHODS = ("GET", "POST", "PUT", "PATH", "DELETE", "COPY", "HEAD", "OPTIONS",
           "LINK", "UNLINK", "PURGE", "LOCK", "UNLOCK", "PROPFIND", "VIEW")

CODES = ("200", "201", "301", "302", "400", "401", "403", "404",
         "500", "501", "502", "503")

with open("access_generated.log", "w") as file:
    i = 0
    while i < 10000:
        IP_ADDRESS = random.choice(IP_ADDRESSES)
        METHOD = random.choice(METHODS)
        CODE = random.choice(CODES)
        LENGTH = random.randint(1, 200000)

        REQUEST = IP_ADDRESS + ' - - [04/Nov/2019:22:38:52 +0300] "' + METHOD + \
                  ' /opencart/path HTTP/1.1" ' + CODE + ' ' + str(LENGTH) + \
                  ' "http://localhost/opencart/" "Mozilla/5.0 (X11; Linux x86_64; ' \
                  'rv:60.0) Gecko/20100101 Firefox/60.0"\n'
        file.write(REQUEST)
        i += 1
