import requests
from lib.logger import Logger


class MyRequests():
    @staticmethod
    def post (url: str, data: dict = None, headers: dict = None, cookies: dict = None):
        return MyRequests._send(url, data, headers, cookies, 'POST')
    @staticmethod
    def get (url: str, data: dict = None, headers: dict = None, cookies: dict = None):
        return MyRequests._send(url, data, headers, cookies, 'GET')
    @staticmethod
    def put (url: str, data: dict = None, headers: dict = None, cookies: dict = None):
        return MyRequests._send(url, data, headers, cookies, 'PUT')
    @staticmethod
    def delete (url: str, data: dict = None, headers: dict = None, cookies: dict = None):
        return MyRequests._send(url, data, headers, cookies, 'DELETE')

    @staticmethod
    # метод статический, т.к. класс является вспомогательным и создавать объекты этого класса не надо
    def _send(url: str, data: dict, headers: dict, cookies: dict, method: str):
    # в питоне нет приватных классов, поэтому функции, которые будут использоваться только внутри класса, являясь вспомогательными, их называют с _

        url = f"https://playground.learnqa.ru/api{url}"

        if headers is None:
            headers = {}
        if cookies is None:
            cookies = {}
    # если в функцию не было передано значение headers, то мы заменяем его значение None на пустой словарь

        Logger.add_request(url, data, headers, cookies, method)

        if method == 'GET':
            response = requests.get(url, params=data, headers=headers, cookies=cookies)
        elif method == 'POST':
            response = requests.post(url, data=data, headers=headers,cookies=cookies)
        elif method == 'PUT':
            response = requests.put(url, data=data, headers=headers, cookies=cookies)
        elif method == 'DELETE':
            response = requests.delete(url, data=data, headers=headers, cookies=cookies)
        else:
            raise Exception(f"Bad HTTP method '{method}' was received")

        Logger.add_response(response)
        return response
    # в зависимости от того, какой метод мы передали, выполнится тот или иной запрос. если непонятно, какой метод передан, вывалится exception
