from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from schemes.TableBase import TableBase


class Database:
    def __init__(self, db_url: str):
        self.engine = create_async_engine(db_url, echo=True)
        self.async_session = sessionmaker(
            self.engine, class_=AsyncSession, expire_on_commit=False
        )

    async def init_db(self):
        """Создает таблицы в базе данных."""
        async with self.engine.begin() as conn:
            await conn.run_sync(TableBase.metadata.create_all)

    async def delete_tables(self):
        """Очищает таблицы в базе данных."""
        async with self.engine.begin() as conn:
            await conn.run_sync(TableBase.metadata.drop_all)

    async def get_session(self) -> AsyncSession:
        """Возвращает асинхронную сессию."""
        return self.async_session()
