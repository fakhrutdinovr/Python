from datetime import datetime
from pydantic import BaseModel


# Pydantic модель для валидации данных
class ModelStocks(BaseModel):
    lastChangeDate: datetime
    warehouseName: str
    supplierArticle: str
    nmId: int
    barcode: str
    quantity: int
    inWayToClient: int
    inWayFromClient: int
    quantityFull: int
    category: str
    subject: str
    brand: str
    techSize: str
    Price: float
    Discount: int
    isSupply: bool
    isRealization: bool
    SCCode: str

class ModelIncomes(BaseModel):
    incomeId: int
    number: str
    date: datetime
    lastChangeDate: datetime
    supplierArticle: str
    techSize: str
    barcode: str
    quantity: int
    totalPrice: float
    dateClose: datetime
    warehouseName: str
    nmId: int
    status: str

class ModelOrders(BaseModel):
    date: datetime
    lastChangeDate: datetime
    warehouseName: str
    warehouseType: str
    countryName: str
    oblastOkrugName: str
    regionName: str
    supplierArticle: str
    nmId: int
    barcode: str
    category: str
    subject: str
    brand: str
    incomeID: int
    isSupply: bool
    isRealization: bool
    totalPrice: float
    discountPercent: int
    spp: float
    finishedPrice: float
    priceWithDisc: float
    isCancel: bool
    cancelDate: datetime
    orderType: str
    sticker: str
    gNumber: str
    srid: str



class ModelSales(BaseModel):
    date: datetime
    lastChangeDate: datetime
    warehouseName: str
    warehouseType: str
    countryName: str
    oblastOkrugName: str
    regionName: str
    supplierArticle: str
    nmId: int
    barcode: str
    category: str
    subject: str
    brand: str
    techSize: str
    incomeID: int
    isSupply: bool
    isRealization: bool
    totalPrice: float
    discountPercent: int
    spp: float
    paymentSaleAmount: int
    forPay: float
    finishedPrice: float
    priceWithDisc: float
    saleID: str
    orderType: str
    sticker: str
    gNumber: str
    srid: str