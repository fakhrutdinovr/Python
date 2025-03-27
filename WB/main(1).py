from data.ApiClient import ApiClient
import json
from dotenv import load_dotenv
import os

load_dotenv()
# Пример использования
if __name__ == "__main__":

    # Создаем экземпляр класса
    client = ApiClient(os.getenv("API_TOKEN"), os.getenv("API_URL"))

    # Выполняем запрос к API
    data = client.getJSON("orders", {"dateFrom": "2024-01-01"})


    if data:
        print("Данные получены:", json.dumps(data, indent=4, ensure_ascii=False))
    else:
        print("Не удалось получить данные.")
