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
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, f"biba'{response.text}"

            assert name in response_as_dict, f"123'{name}"

            @staticmethod
            def assert_code_status(response: Response, expected_status_code)
                assert response.status_code == expected_status_code, f"Unexpected status code! Expected: {expected_status_code}". Actual: {response.status_code}"
