import pytest
from lib.my_requests import MyRequests
from lib.base_case import BaseCase
from lib.assertions import Assertions

class TestUserAuth(BaseCase):
    exclude_params = [
        ("no_cookie"),
        ("no_token")
    ]
    # список параметров теста

    def setup(self):
        data = {
            "email": "vinkotov@example.com",
            "password": "1234"}

        # функция setup - код внутри неё автоматически вызывается перед запуском каждого теста, где она используется. туда кладём логику, с которой начинаются все тесты в классе

        response1 = MyRequests.post("/user/login", data=data)
        # отправляем POST запрос с боди из переменной data

        self.auth_sid = self.get_cookie(response1, "auth_sid")
        self.token = self.get_header(response1, "x-csrf-token")
        self.user_id_from_auth_method = self.get_json_value(response1, "user_id")
        # получение куки и хэдеров перевели в новые методы

        self.user_id_from_auth_method = response1.json()["user_id"]
        # получаем параметры из результатов POST запроса и сохраняем их в переменные. чтобы переменные использовать в других тестах, добавляем 'self'
        # self - указатель, позволяющий делать переменную полем класса, т.е. передавать её значения из одной функции в другие. внутри функций их тоже надо вызывать через self

    def test_user_auth(self):

        response2 = MyRequests.get(
            "/user/auth",
            headers={"x-csrf-token": self.token},
            cookies={"auth_sid": self.auth_sid}
        )

        Assertions.assert_json_value_by_name(
            response2,
            "user_id",
            self.user_id_from_auth_method,
            "User id from auth method is not equal to user id from check method"
        )


    @pytest.mark.parametrize('condition', exclude_params)
        # внутри теста будет переменная "Condition", которая будет либо "No Cookie", либо "No Token"
    def test_negative_auth_check(self, condition):


        if condition == "no_cookie":
            response2 = MyRequests.get(
                "/user/auth",
                headers={"x-csrf-token": self.token}
            )
        else:
            response2 = MyRequests.get(
                "/user/auth",
                cookies={"auth_sid": self.auth_sid}
                )
        # если переменная "Condition" = "No Cookie", тогда сделаем запрос без куки. Иначе - без токена.

        Assertions.assert_json_value_by_name(
            response2,
            "user_id",
            0,
            f"User if authorized with condition {condition}"
        )