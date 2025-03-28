from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import List
from schemes.Tables import TableStocks  # Импортируем SQLAlchemy модель
from models.Models import ModelStocks  # Импортируем Pydantic модель


class ProductRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def insert_product(self, product_data, db_table):
        """
        Добавляет один продукт в базу данных.
        """
        product = db_table(**product_data.dict())  # Преобразуем Pydantic модель в SQLAlchemy модель
        self.session.add(product)
        await self.session.commit()
        await self.session.refresh(product)
        return product

    async def insert_many_products(self, products_data: List, db_table):
        """
        Добавляет несколько продуктов в базу данных.
        :param db_table: Таблица куда добавляем
        """
        products = [db_table(**item.dict()) for item in
                    products_data]  # Преобразуем список Pydantic моделей в SQLAlchemy модели
        self.session.add_all(products)
        await self.session.commit()
        return products

    async def get_all_products(self):
        """
        Возвращает все продукты из базы данных.
        """
        result = await self.session.execute(select(TableStocks))
        return result.scalars().all()

    async def get_product_by_id(self, product_id: int):
        """
        Возвращает продукт по его ID.
        """
        result = await self.session.execute(select(TableStocks).where(TableStocks.id == product_id))
        return result.scalars().first()
