"""Модуль для проверки действий с удаленным сервером OpenCart"""
import paramiko

PARAMS = ("192.168.1.3", "realdeal87", "realdeal87")


class SSHConnector:
    """Класс для создания соединения по SSH и отправки команд"""

    def __init__(self, host, user, secret, port=22):
        self.secret = secret
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.client.connect(hostname=host, username=user, password=secret, port=port)
        self.channel = self.client.get_transport().open_session()
        self.channel.set_combine_stderr(True)
        self.channel.get_pty()

    def command(self, command):
        """Метод для выполнения команды от имени суперпользователя"""
        self.channel.exec_command(command)
        stdin = self.channel.makefile('wb', -1)
        stdout = self.channel.makefile('rb', -1)
        if command.startswith("sudo"):
            stdin.write(self.secret + "\n")
            stdin.flush()
        result = stdout.read().decode("utf-8")
        self.channel.close()
        self.client.close()
        return result


def test_opencart_works_after_restart():
    """Доступность OpenCart после перезагрузки сервера"""
    SSHConnector(*PARAMS).command("sudo systemctl restart apache2")
    status_code = SSHConnector(*PARAMS).command("curl -o /dev/null -s -w"
                                                "'%{http_code}\n' http://localhost/opencart/")
    assert int(status_code) == 200


def test_restart_apache2():
    """Доступность apache2 после перезагрузки"""
    SSHConnector(*PARAMS).command("sudo systemctl restart apache2")
    status = SSHConnector(*PARAMS).command("systemctl | grep apache2")
    assert "running" in status


def test_restart_mariadb():
    """Доступность mariadb после перезагрузки"""
    SSHConnector(*PARAMS).command("sudo systemctl restart mariadb")
    status = SSHConnector(*PARAMS).command("systemctl | grep mariadb")
    assert "running" in status
