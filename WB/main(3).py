import asyncio
from schemes.Database import Database
from repositories.ProductRepository import ProductRepository
from models.Models import ModelStocks, ModelIncomes, ModelOrders, ModelSales
from data.ApiClient import ApiClient
from schemes.Tables import TableStocks, TableIncomes, TableOrders, TableSales
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
        data_stocks = client.getData("stocks", ModelStocks, {"dateFrom": "2019-01-01"})
        # Вставляем данные в таблицу
        await repo.insert_many_products(data_stocks, TableStocks)


        # Выполняем запрос к API
        data_incomes = client.getData("incomes", ModelIncomes, {"dateFrom": "2024-01-01"})
        # Вставляем данные в таблицу
        await repo.insert_many_products(data_incomes, TableIncomes)


        # Выполняем запрос к API
        data_orders = client.getData("orders", ModelOrders, {"dateFrom": "2025-01-01"})
        # Вставляем данные в таблицу
        await repo.insert_many_products(data_orders, TableOrders)

        # Выполняем запрос к API
        data_sales = client.getData("sales", ModelSales, {"dateFrom": "2025-01-01"})
        # Вставляем данные в таблицу
        await repo.insert_many_products(data_sales, TableSales)

        print("Данные успешно загружены в базу данных.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    asyncio.run(main())
