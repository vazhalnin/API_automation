import json
from requests import Response
from _datetime import datetime

class BaseCase:
    # в этом классе будут методы для получения куки и хедеров из ответов сервера по имени
    # суть методов: сначала в них передаём объект ответа, который получаем после запроса и имя, по которому из ответа получаем либо хедер, либо куки. если данных нет - тест упадёт
    def get_cookie(self, response: Response, cookie_name):
        assert cookie_name in response.cookies, f"Cannot find cookie with name {cookie_name} in the last response"
        return response.cookies[cookie_name]

    def get_header (self, response: Response, headers_name):
        assert headers_name in response.headers, f"Cannot find header with the name {headers_name} in the last response"
        return response.headers[headers_name]

    def get_json_value(self, response : Response, name):

        # прежде, чем получить что-то из Json, мы должны убедиться, что респонс от сервера пришёл точно в формате Json
        try:
            response_as_dict = response.json()
            # пытаемся распарсить ответ от сервера, как будто он json
        except json.decoder.JSONDecodeError:
            assert False, f"Response is not in JSON Format. Response text is '{response.text}"
            # если распарсить не получится, assert false сделает тест упавшим

        assert name in response_as_dict, f"Response JSON doesn't have a key '{name}'"
            # если парсинг прошёл успешно, делаем ассерт по имени name есть в ответе. и если всё ок, возвращаем  это значение

        return response_as_dict[name]


    def prepare_registraion_data(self, email=None):
        # всю логику по созданию нового пользователя мы вынесли из класса testuserregister, но сделали email входным параметром с дефолтным значением
        # мы его можем передавать, а можем и не передавать. если не передать - он будет равен None, и будет сгенерирован рандомным образом
        if email is None:
            base_part = "learnqa"
            domain = "example.com"
            random_part = datetime.now().strftime("%m%d%Y%H%M%S")
            email = f"{base_part}{random_part}@{domain}"

        return {
            'password': '123',
            'username': '123',
            'firstName': 'learnqa',
            'lastName': 'learnqa',
            'email': email
        }