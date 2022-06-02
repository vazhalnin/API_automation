import pytest
import requests

class TestUserAuth:
    def test_user_auth(self):
        data = {
            "email":"vinkotov@example.com",
            "password":"1234"}
        # создали класс, внутри него - тест, а в переменную data положили данные для авторизации

        response1 = requests.post("https://playground.learnqa.ru/api/user/login", data=data)
        # отправляем POST запрос с боди из переменной data

        assert "auth_sid" in response1.cookies, "NET KUKI"
        assert "x-csrf-token" in response1.headers, "NET CSRF"
        assert "user_id" in response1.json(), "NET USER"
        # проверяем, есть ли нужные параметры в переменной response1. если нет - выводим сообщение об ошибке

        # после того, как мы убедились, что все параметры есть, перекладываем их в отдельные переменные (строки ниже)

        auth_sid = response1.cookies.get("auth_sid")
        token = response1.headers.get("x-csrf-token")
        user_id_from_auth_method = response1.json()["user_id"]
        # получаем параметры из результатов POST запроса и сохраняем их в переменные

    response2 = requests.get(
        "https://playground.learnqa.ru/api/user/auth",
        headers={"x-csrf-token":token},
        cookies={"auth_sid":auth_sid}

    )
    # делаем GET запрос с использованием полученных данных из POST запроса

    assert "user_id" in response2.json(), "NET USER"
    user_id_from_check_method = response2.json()["user_id"]

    # убеждаемся, что во втором респонсе тоже есть user_id и после заносим его в отдельную переменную

    assert user_id_from_auth_method == user_id_from_check_method, "EGOG"
    # сравним две переменных

    exclude_params= [
        ("no_cookie"),
        ("no_token")
    ]

    @pytest.mark.parametrize('condition', exclude_params)
        # внутри теста будет переменная "Condition", которая будет либо "No Cookie", либо "No Token"
    def test_negative_auth_check(self, condition):
        data = {
            "email":"vinkotov@example.com",
            "password":"1234"}
        # создали класс, внутри него - тест, а в переменную data положили данные для авторизации

        response1 = requests.post("https://playground.learnqa.ru/api/user/login", data=data)
        # отправляем POST запрос с боди из переменной data

        assert "auth_sid" in response1.cookies, "NET KUKI"
        assert "x-csrf-token" in response1.headers, "NET CSRF"
        assert "user_id" in response1.json(), "NET USER"
        # проверяем, есть ли нужные параметры в переменной response1. если нет - выводим сообщение об ошибке


        auth_sid = response1.cookies.get("auth_sid")
        token = response1.headers.get("x-csrf-token")
        # получаем параметры из результатов POST запроса и сохраняем их в переменные

        if condition == "no_cookie":
            response2 = requests.get(
                "http://playground.learnqa.ru/api/user/auth",
                headers={"x-csrf-token": token}
            )
        else:
            response2 = requests.get(
                "http://playground.learnqa.ru/api/user/auth",
                cookies={"auth_sid": auth_sid}
                )
        # если переменная "Condition" = "No Cookie", тогда сделаем запрос без куки. Иначе - без токена.

        assert  "user_id" in response1.json(), "There is no user id n the second response"
        # проверка, что user_id в ответе есть

        user_id_from_check_method = response2.json()["user_id"]

        assert  user_id_from_check_method == 0, f"User is authorized with condition {condition}"
        # убеждаемся, что переменная из второго ответа = 0, а если это не так - пишем, что юзер авторизован, несмотря на условия