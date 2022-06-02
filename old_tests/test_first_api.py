import requests
# подключаем библиотеку requests

class TestFirstApi:
    def test_hello_call(self):
        # объявляем класс и функцию теста

        url = "https://playground.learnqa.ru/api/hello"
        name = 'Biba'
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