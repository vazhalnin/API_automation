import requests
from lib.base_case import BaseCase
from lib.assertions import Assertions
from datetime import datetime


class TestUserRegister(BaseCase):
    def setup(self):
        base_part = "learnqa"
        # определяем базовую часть, с которой будут начинаться все имэйл
        domain = "example.com"
        # определяем доменную часть
        random_part = datetime.now().strftime("%m%d%Y%H%M%S")
        # определяем случайную часть, которая генерируется по времени
        self.email = f"{base_part}{random_part}@{domain}"

    def test_create_user_successfully(self):
        data = {
            'password': '123',
            'username': '123',
            'firstName': 'learnqa',
            'lastName': 'learnqa',
            'email': self.email

        }
        # вместо захардкоженной почты мы вызываем функцию сетап

    response = requests.post("https://playground.learnqa.ru/api/user/", data=data)
       assert response.status_code == 200, f"Unexpected status code {response.status_code}"
       Assertions.assert_json_has_key(response, "id")


def test_create_user_with_existing_email(self):
    email = 'vinkotov@example.com'
    data = {
        'password': '123',
        'username': '123',
        'firstName': 'learnqa',
        'lastName': 'learnqa',
        'email': email
    }

    response = requests.post("https://playground.learnqa.ru/api/user/", data=data)

    assert response.status_code == 400, f"Unexpected status code {response.status_code}"
    assert response.content.decode("utf=8") == f"Users with email '{email}' already exists"