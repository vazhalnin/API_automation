import pytest
import requests
import pytest
# подключаем библиотеку requests

class ParametrizedTest:

    # внутри класса, но за пределами функции, создаём переменную, которая хранит в себе список/лист; внутри этого списка находится последовательность кортежей
    names = [
        ("Name1"),
        ("Name2"),
        ("")
    ]
    # появилась переменная "список", которая хранит внутри себя кортежи. кортежи состоят из параметров для запуска тестов (имена)

    @pytest.mark.parametrize('name', names)
    # указываем имя переменной, в которую pytest будет передавать данные. через запятую - переменная, в которой эти данные хранятся
    def test_hello_call(self, name):
        # объявляем класс и функцию теста, добавляем ту самую переменную, в которой и будут данные

        url = "https://playground.learnqa.ru/api/hello"
        data = {'name':name}
        # в отдельные переменные выносим url и данные для запроса

        response = requests.get(url, params=data)
        # делаем запрос и помещаем ответ в переменную response

        assert response.status_code == 200, "Wrong response code"
        # проверяем, что код ответа = 200; если условие не выполнится, то будет текст выше

        response_dict = response.json()
        # поскольку ответ - в формате json, мы парсим его в перменную dict (после того, как json распарсен, он является словарём
        assert "answer" in response_dict, "There is no field 'answer' in the response"
        # проверяем, что в словаре есть поле "answer"

        expected_response_test = f"Hello, {name}"
        actual_response_text = response_dict["answer"]
        assert actual_response_text == expected_response_test, "Actual text in the response is not correct"
        # проверяем, что значение поля == ожидаемому тексту; если сравнение не прошло, то выведется ошибка