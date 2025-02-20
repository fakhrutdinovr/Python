from datetime import datetime
from sqlalchemy import DateTime
from sqlalchemy.orm import Mapped, mapped_column
from schemes.TableBase import TableBase


class TableStocks(TableBase):
    __tablename__ = 'TableStocks'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    lastChangeDate: Mapped[datetime] = mapped_column(DateTime)
    warehouseName: Mapped[str]
    supplierArticle: Mapped[str]
    nmId: Mapped[int]
    barcode: Mapped[str]
    quantity: Mapped[int]
    inWayToClient: Mapped[int]
    inWayFromClient: Mapped[int]
    quantityFull: Mapped[int]
    category: Mapped[str]
    subject: Mapped[str]
    brand: Mapped[str]
    techSize: Mapped[str]
    Price: Mapped[float]
    Discount: Mapped[int]
    isSupply: Mapped[bool]
    isRealization: Mapped[bool]
    SCCode: Mapped[str]
