from requests import Response
import json

class Assertions:
    @staticmethod
    def assert_json_value_by_name(response: Response, name, expected_value, error_message):
        # убеждаемся, что значение внутри JSON доступно по определённому имени и равно тому, что мы ожидаем
        # на вход функция должна получать объект с ответом сервера, чтоб получить из него текст; имя, по которому искать значение в json; ожидаемое значение; текст ошибки если значение не найти
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, f"Response is not in JSON format. JSON text is '{response.text}'"

        assert name in response_as_dict, f"Response JSON doesn't have key '{name}'"
        assert response_as_dict[name] == expected_value, error_message

    # вместо того, чтобы возвращать значение, она с помощью assert сравнивает его с ожидаемым
    # метод делае ассерт по значению поля, которое мы заранее не знаем

    @staticmethod
    def assert_json_has_key(response: Response, name):
        # проверка, что в JSON есть поле ID
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, f"Response is not in JSON format. Response text is '{response.text}'"

        assert name in response_as_dict, f"Response JSON doesn't have a key '{name}"

    @staticmethod
    def assert_json_has_keys(response: Response, names: list):
        # вместо того, чтоб принимать только одно значение и проверять одно значение, он принимает список значений и с помощью цикла идёт по этому списку
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, f"Response is not in JSON format. Response text is '{response.text}'"
        for name in names:
            assert name in response_as_dict, f"Response JSON doesn't have a key '{name}"



    @staticmethod
    def assert_json_has_not_key(response: Response, name):
        # проверка, что в JSON есть поле ID
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, f"Response is not in JSON format. Response text is '{response.text}'"

        assert name not in response_as_dict, f"Response JSON shouldn't have a key '{name}. But it present"


    @staticmethod
    def assert_code_status(response: Response, expected_status_code):
        # проверка, что код ответа равняется ожидаемому, и пишет ошибку, когда это не так. И не нужно будет каждый раз писать ожидаемый текст ошибки
        assert response.status_code == expected_status_code, \
            f"Unexpected status code! Expected: {expected_status_code}. Actual: {response.status_code}"
