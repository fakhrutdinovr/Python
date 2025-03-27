from sqlalchemy.orm import DeclarativeBase
from datetime import datetime
from sqlalchemy import DateTime
from sqlalchemy.orm import Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class TableStocks(Base):
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


class TableIncomes(Base):
    __tablename__ = 'TableIncomes'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    incomeId: Mapped[int]
    number: Mapped[str]
    date: Mapped[datetime]
    lastChangeDate: Mapped[datetime]
    supplierArticle: Mapped[str]
    techSize: Mapped[str]
    barcode: Mapped[str]
    quantity: Mapped[int]
    totalPrice: Mapped[float]
    dateClose: Mapped[datetime]
    warehouseName: Mapped[str]
    nmId: Mapped[int]
    status: Mapped[str]


class TableOrders(Base):
    __tablename__ = 'TableOrders'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    date: Mapped[datetime]
    lastChangeDate: Mapped[datetime]
    warehouseName: Mapped[str]
    warehouseType: Mapped[str]
    countryName: Mapped[str]
    oblastOkrugName: Mapped[str]
    regionName: Mapped[str]
    supplierArticle: Mapped[str]
    nmId: Mapped[int]
    barcode: Mapped[str]
    category: Mapped[str]
    subject: Mapped[str]
    brand: Mapped[str]
    incomeID: Mapped[int]
    isSupply: Mapped[bool]
    isRealization: Mapped[bool]
    totalPrice: Mapped[float]
    discountPercent: Mapped[int]
    spp: Mapped[float]
    finishedPrice: Mapped[float]
    priceWithDisc: Mapped[float]
    isCancel: Mapped[bool]
    cancelDate: Mapped[datetime]
    orderType: Mapped[str]
    sticker: Mapped[str]
    gNumber: Mapped[str]
    srid: Mapped[str]



class TableSales(Base):
    __tablename__ = 'TableSales'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    date: Mapped[datetime]
    lastChangeDate: Mapped[datetime]
    warehouseName: Mapped[str]
    warehouseType: Mapped[str]
    countryName: Mapped[str]
    oblastOkrugName: Mapped[str]
    regionName: Mapped[str]
    supplierArticle : Mapped[str]
    nmId: Mapped[int]
    barcode: Mapped[str]
    category: Mapped[str]
    subject: Mapped[str]
    brand: Mapped[str]
    techSize: Mapped[str]
    incomeID: Mapped[int]
    isSupply: Mapped[bool]
    isRealization: Mapped[bool]
    totalPrice: Mapped[float]
    discountPercent: Mapped[int]
    spp: Mapped[float]
    paymentSaleAmount: Mapped[int]
    forPay: Mapped[float]
    finishedPrice: Mapped[float]
    priceWithDisc: Mapped[float]
    saleID: Mapped[str]
    orderType: Mapped[str]
    sticker: Mapped[str]
    gNumber: Mapped[str]
    srid: Mapped[str]