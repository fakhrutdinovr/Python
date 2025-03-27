from repositories.ProductRepository import ProductRepository
import json


class DataService:

    async def putDataToDb(self, data: dict, model, table):
        products = [model(**item) for item in data]
        await ProductRepository.insert_many_products(products, table)
