import requests
from lib.base_case import BaseCase
from lib.assertions import Assertions


class TestUserRegisterRandomEmail(BaseCase):
    def test_create_user_successfully(self):
        data = self.prepare_registraion_data()

        response = requests.post("https://playground.learnqa.ru/api/user", data=data)
        # отправляем запрос

        assert response.status_code == 200, f"Unexpected status code {response.status_code}"
        # убеждаемся, что код ответа - 200

        Assertions.assert_json_has_key(response, "id")


    def test_create_user_with_existing_email(self):
        email = 'vinkotov@example.com'
        data = self.prepare_registraion_data(email)
        # если мы передаём email, то функция его не будет генерировать, а сразу запишет в data

        response = requests.post("https://playground.learnqa.ru/api/user/", data=data)

        # assert response.status_code == 400, f"Unexpected biba {response.status_code}" - было до появления отдельной проверки статуса в классе ассертов
        Assertions.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == f"Users with email '{email}' already exists", f"Unexpected response content {response.content}"
        # декодируем ответ в utf-8, потому что без него тест не работает

