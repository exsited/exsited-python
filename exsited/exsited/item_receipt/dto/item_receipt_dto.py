from dataclasses import dataclass
from exsited.sdlize.ab_base_dto import ABBaseDTO


@dataclass(kw_only=True)
class ItemReceiptLineDTO(ABBaseDTO):
    lineUuid: str = None
    itemId: str = None
    uom: str = None
    warehouse: str = None
    receiptQuantity: str = None
    receiptLeft: str = None


@dataclass(kw_only=True)
class ItemReceiptDTO(ABBaseDTO):
    receiptStatus: str = None
    date: str = None
    id: str = None
    purchaseOrderId: str = None
    trackingNumber: str = None
    note: str = None
    receipts: list[ItemReceiptLineDTO] = None
    createdBy: str = None
    createdOn: str = None
    lastUpdatedBy: str = None
    lastUpdatedOn: str = None
    uuid: str = None
    version: str = None


@dataclass(kw_only=True)
class PaginationDTO(ABBaseDTO):
    records: int = None
    limit: int = None
    offset: int = None
    previousPage: str = None
    nextPage: str = None


@dataclass(kw_only=True)
class ItemReceiptListDTO(ABBaseDTO):
    itemReceipts: list[ItemReceiptDTO] = None
    pagination: PaginationDTO = None


@dataclass(kw_only=True)
class ItemReceiptDetailsDTO(ABBaseDTO):
    itemReceipts: ItemReceiptDTO = None


@dataclass(kw_only=True)
class ItemReceiptDetailsDTO(ABBaseDTO):
    purchaseOrder: ItemReceiptListDTO = None
