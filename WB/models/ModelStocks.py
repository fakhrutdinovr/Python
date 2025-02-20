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
