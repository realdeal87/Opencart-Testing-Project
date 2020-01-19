"""Модуль для работы с browsermob-proxy"""
import psutil
from browsermobproxy import Server, Client


class MyServer(Server):
    """Переопределен класс Server"""

    def __init__(self, path):
        """Создание экземпляра сервера"""
        self.server = super().__init__(path)

    def stop(self):
        """Остановка сервера"""
        super().stop()

        # Поскольку коммандой stop прокси сервер не останавливается
        # приходится убивать процесс
        for process in psutil.process_iter():
            if "-Dapp.name=browsermob-proxy" in process.cmdline():
                process.kill()


class MyClient(Client):
    """Переопределен класс Client"""

    def __init__(self, url):
        """Создание экземпляра клиента"""
        self.client = super().__init__(url)

    def logger(self):
        """Запись лога прокси сервера"""
        with open("proxy.log", "a") as file:
            params = self.har["log"]

            # Здесь необходимо сформировать вывод требуемых параметров
            for key in params:
                message = str(key) + "->" + str(params[key]) + "\n"
                file.write(message)
