from dataclasses import dataclass
from ab_py.exsited.common.dto.common_dto import TaxDTO, PaginationDTO
from ab_py.sdlize.ab_base_dto import ABBaseDTO
from ab_py.exsited.common.dto.common_dto import PaginationDTO

@dataclass(kw_only=True)
class PurchaseOrderCurrencyDTO(ABBaseDTO):
    uuid: str = None
    name: str = None
    link: str = None


@dataclass(kw_only=True)
class PurchaseOrderPricingRuleDTO(ABBaseDTO):
    uuid: str = None
    version: str = None
    priceType: str = None
    price: str = None
    uom: str = None
    warehouse: str = None
    pricingVersion: str = None
    latestUsedPricingVersion: str = None


@dataclass(kw_only=True)
class PurchaseOrderItemPriceSnapshotDTO(ABBaseDTO):
    pricingRule: PurchaseOrderPricingRuleDTO = None


@dataclass(kw_only=True)
class PurchaseOrderTaxCodeDTO(ABBaseDTO):
    uuid: str = None
    code: str = None
    rate: str = None
    link: str = None


@dataclass(kw_only=True)
class PurchaseOrderItemPurchaseTaxConfigurationDTO(ABBaseDTO):
    purchasePriceIsTaxInclusive: str = None
    taxCode: PurchaseOrderTaxCodeDTO = None


@dataclass(kw_only=True)
class KPIDTO(ABBaseDTO):
    totalExpense: float = 0
    estimatedTotal: float = 0
    totalOutstanding: float = 0
    totalOverdue: float = 0
    lastInvoiceIssueDate: str = ""
    lastInvoiceTotal: float = 0
    totalPurchaseInvoice: float = 0
    lastReactivatedOn: str = ""
    lastCalcelledOn: str = ""
    lastChangedOn: str = ""
    lastDeletedOn: str = ""
    issueDate: str = ""

@dataclass(kw_only=True)
class PurchaseOrderItemAccountingCodeDTO(ABBaseDTO):
    costOfGoodsSold: str = None


@dataclass(kw_only=True)
class PurchaseOrderLineDTO(ABBaseDTO):
    subtotal: str = None
    total: str = None
    tax: str = None
    itemUuid: str = None
    itemId: str = None
    itemName: str = None
    itemQuantity: str = None
    itemPriceSnapshot: PurchaseOrderItemPriceSnapshotDTO = None
    itemPurchaseTaxConfiguration: PurchaseOrderItemPurchaseTaxConfigurationDTO = None
    itemPriceTaxExempt: str = None
    itemPriceTax: TaxDTO = None
    purchaseOrderNote: str = None
    itemAccountingCode: PurchaseOrderItemAccountingCodeDTO = None
    uuid: str = None
    version: str = None
    itemSerialOrBatchNumber: str = None



@dataclass(kw_only=True)
class PurchaseOrderDTO(ABBaseDTO):
    status: str = None
    id: str = None
    currency: PurchaseOrderCurrencyDTO = None
    supplierInvoiceId: str = None
    issueDate: str = None
    dueDate: str = None
    expectedCompletionDate: str = None
    subtotal: str = None
    tax: str = None
    total: str = None
    priceTaxInclusive: str = None
    purchaseOrderNote: str = None
    accountId: str = None
    createdBy: str = None
    createdOn: str = None
    lastUpdatedBy: str = None
    lastUpdatedOn: str = None
    uuid: str = None
    version: str = None
    customAttributes: list = None  # Added to match response
    customObjects: list = None  # Added to match response
    lines: list[PurchaseOrderLineDTO] = None
    kpis: KPIDTO = None


@dataclass(kw_only=True)
class PurchaseOrderDataDTO(ABBaseDTO):
    status: str = None
    id: str = None
    currency: str = None
    supplierInvoiceId: str = None
    issueDate: str = None
    dueDate: str = None
    expectedCompletionDate: str = None
    subtotal: str = None
    tax: str = None
    total: str = None
    priceTaxInclusive: str = None
    purchaseOrderNote: str = None
    accountId: str = None
    createdBy: str = None
    createdOn: str = None
    uuid: str = None
    version: str = None
    customAttributes: list = None
    customObjects: list = None
    lines: list[PurchaseOrderLineDTO] = None


@dataclass(kw_only=True)
class PurchaseOrderDetailsDTO(ABBaseDTO):
    purchaseOrder: PurchaseOrderDTO = None


@dataclass(kw_only=True)
class PurchaseOrderCreateDTO(ABBaseDTO):
    purchaseOrder: PurchaseOrderDataDTO = None


@dataclass(kw_only=True)
class PurchaseOrderListDTO(ABBaseDTO):
    purchaseOrders: list[PurchaseOrderDTO] = None
    pagination: PaginationDTO = None
