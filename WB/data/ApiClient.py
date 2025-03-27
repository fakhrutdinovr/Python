import requests


class ApiClient:
    def __init__(self, token, url):
        """
        Конструктор класса.
        :param token: Токен для авторизации.
        :param url: Базовый URL API.
        """
        self.token = token
        self.url = url
        self.headers = {"Content-type": 'application/json',
                        "Authorization": f'{self.token}'}

    def getData(self, endpoint, model, params=None):
        """
        Метод для выполнения GET-запроса к API.
        :param endpoint: Конечная точка API (например, "/stocks").
        :param model: Модель pydentic
        :param params: Параметры запроса (опционально).
        :return: Ответ от сервера в формате JSON.
        """
        full_url = f"{self.url}{endpoint}"  # Полный URL запроса
        try:
            response = requests.get(full_url, headers=self.headers, params=params)
            response.raise_for_status()  # Проверяем, не вернулась ли ошибка HTTP
            return [model(**item) for item in response.json()]  # Возвращаем ответ в формате pydentic модели
        except requests.exceptions.RequestException as e:
            print(f"Ошибка при выполнении запроса: {e}")
            return None

    def getJSON(self, endpoint, params=None):
        """
        Метод для выполнения GET-запроса к API.

        :param endpoint: Конечная точка API (например, "/stocks").
        :param params: Параметры запроса (опционально).
        :return: Ответ от сервера в формате JSON или словарь с информацией об ошибке.
        """
        full_url = f"{self.url}{endpoint}"  # Полный URL запроса
        try:
            response = requests.get(full_url, headers=self.headers, params=params)
            response.raise_for_status()  # Проверяем, не вернулась ли ошибка HTTP
            return response.json()  # Возвращаем ответ в формате JSON
        except requests.exceptions.RequestException as e:
            print(f"Ошибка при выполнении запроса: {e}")
            return None