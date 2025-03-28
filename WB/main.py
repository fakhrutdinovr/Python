import asyncio
from models.Models import ModelStocks
from schemes.Database import Database
from repositories.ProductRepository import ProductRepository
from data.ApiClient import ApiClient
from schemes.TableStocks import TableStocks
from dotenv import load_dotenv
import os

load_dotenv()

API_TOKEN = os.getenv("API_TOKEN")
API_URL = os.getenv("API_URL")


async def main():
    try:
        # Инициализация базы данных
        db = Database(os.getenv("DB_URL"))
        await db.delete_tables()
        await db.init_db()

        # Получаем сессию
        session = await db.get_session()

        # Инициализация репозитория
        repo = ProductRepository(session)

        # Создаем экземпляр класса
        client = ApiClient(API_TOKEN, API_URL)

        # Выполняем запрос к API
        data_stocks = client.getData("stocks", {"dateFrom": "2019-01-01"})

        # Вставляем данные в таблицу
        products = [ModelStocks(**item) for item in data_stocks]
        await repo.insert_many_products(products, TableStocks)

        print("Данные успешно загружены в базу данных.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    asyncio.run(main())

