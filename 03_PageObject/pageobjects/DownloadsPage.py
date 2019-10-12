"""Модуль описывает действия на странице загрузок панели администратора
сайта opencart"""
import time
from locators import Downloads
from .BasePage import BasePage


class DownloadsPage(BasePage):
    """Методы описывают действия на странице загрузок панели администратора"""

    def upload_file(self, file, name):
        """Загрузка файла в раздел загрузок"""
        script = """
                document.getElementById("button-upload").click();
                var f = document.createElement("form");
                f.id = "form-upload";
                f.style.display = "block";
                f.enctype = "multipart/form-data";
                inp = document.createElement("input");
                inp.type = "file";
                inp.name = "file";
                f.appendChild(inp);
                body = document.getElementsByTagName("body")[0];
                body.insertBefore(f, body.firstChild);
                """
        self._upload_file(script, file)
        time.sleep(2)
        self.alert().accept()
        self._input(Downloads.download_name, name)
        return self
