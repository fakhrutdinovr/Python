from Anvarov_ip.WB.data.ApiClient import ApiClient
import json
from config import token, url

# Пример использования
if __name__ == "__main__":

    # Создаем экземпляр класса
    client = ApiClient(token, url)

    # Выполняем запрос к API
    data = client.getData("stocks", {"dateFrom": "2019-01-01"})


    if data:
        print("Данные получены:", json.dumps(data, indent=4, ensure_ascii=False))
    else:
        print("Не удалось получить данные.")
