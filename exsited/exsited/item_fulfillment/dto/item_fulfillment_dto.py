from dataclasses import dataclass

from exsited.exsited.item.dto.item_dto import PaginationDTO
from exsited.sdlize.ab_base_dto import ABBaseDTO


@dataclass(kw_only=True)
class FulfillmentDTO(ABBaseDTO):
    itemUuid: str = None
    itemId: str = None
    uom: str = None
    warehouse: str = None
    fulfillmentQuantity: str = None
    fulfillmentLeft: str = None
    uuid: str = None


@dataclass(kw_only=True)
class ItemFulfillmentDataDTO(ABBaseDTO):
    status: str = None
    date: str = None
    id: str = None
    orderId: str = None
    invoiceId: str = None
    trackingNumber: str = None
    note: str = None
    fulfillments: list[FulfillmentDTO] = None
    createdBy: str = None
    createdOn: str = None
    lastUpdatedBy: str = None
    lastUpdatedOn: str = None
    uuid: str = None
    version: str = None


@dataclass(kw_only=True)
class ItemFulfillmentListResponseDTO(ABBaseDTO):
    item_fulfillments: list[ItemFulfillmentDataDTO] = None
    pagination: PaginationDTO = None


@dataclass(kw_only=True)
class ItemFulfillmentCreateDTO(ABBaseDTO):
    item_fulfillments: ItemFulfillmentDataDTO = None


@dataclass(kw_only=True)
class ItemFulfillmentDetailsDTO(ABBaseDTO):
    item_fulfillment: ItemFulfillmentDataDTO = None


@dataclass(kw_only=True)
class ItemFulfillmentInvoiceDTO(ABBaseDTO):
    invoice: ItemFulfillmentDetailsDTO = None


@dataclass(kw_only=True)
class ItemFulfillmentInvoiceListDTO(ABBaseDTO):
    invoice: ItemFulfillmentListResponseDTO = None
