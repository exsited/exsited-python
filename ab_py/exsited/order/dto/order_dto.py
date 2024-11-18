from dataclasses import dataclass

from ab_py.exsited.account.dto.account_nested_dto import CommunicationPreferenceDTO
from ab_py.exsited.common.dto.common_dto import CustomFormsDTO, CurrencyDTO, TimeZoneDTO, TaxDTO, PaginationDTO
from ab_py.exsited.order.dto.order_nested_dto import OrderLineDTO, OrderItemPriceSnapshotDTO, OrderPropertiesDTO, \
    ContractPropertiesDTO, UpgradeDowngradePreviewDTO, KpisDTO
from ab_py.sdlize.ab_base_dto import ABBaseDTO


@dataclass(kw_only=True)
class KPIStatsDTO(ABBaseDTO):
    startDate: str = None
    estimatedTotal: float = None
    totalRevenue: float = None
    monthlyRecurringRevenue: float = None
    totalCollected: float = None
    totalOutstanding: float = None
    totalDue: float = None
    lastInvoiceIssueDate: str = None
    lastInvoiceTotal: float = None
    totalInvoice: int = None
    nextInvoiceIssueDate: str = None
    lastReactivatedOn: str = None
    lastCancelledOn: str = None
    lastChangedOn: str = None
    lastDeletedOn: str = None


@dataclass(kw_only=True)
class CustomAttributesDataDTO(ABBaseDTO):
    name: str = None
    value: str = None


@dataclass(kw_only=True)
class OrderDataDTO(ABBaseDTO):
    accountId: str = None
    status: str = None
    id: str = None
    uuid: str = None
    version: str = None
    preOrder: str = None
    quoteOrder: str = None
    name: str = None
    displayName: str = None
    description: str = None
    manager: str = None
    referralAccount: str = None
    shippingCost: str = None
    origin: str = None
    invoiceNote: str = None
    billingStartDate: str = None
    orderStartDate: str = None
    nextBillingFromDate: str = None
    priceTaxInclusive: str = None
    createdBy: str = None
    createdOn: str = None
    lastUpdatedBy: str = None
    lastUpdatedOn: str = None
    allowContract: str = None

    lines: list[OrderLineDTO] = None
    customForms: CustomFormsDTO = None
    currency: CurrencyDTO = None
    timeZone: TimeZoneDTO = None
    properties: OrderPropertiesDTO = None

    contractProperties: ContractPropertiesDTO = None
    billingAddress: dict = None
    shippingAddress: dict = None
    shippingProfile: dict = None
    defaultWarehouse: str = None
    customObjects: list = None
    isTaxExemptWhenSold: str = None
    kpis: KpisDTO = None
    lineItems: list = None
    effectiveDate: str = None
    charge: OrderLineDTO = None
    communicationPreference: list[CommunicationPreferenceDTO] = None
    line: OrderLineDTO = None
    customAttributes: list[CustomAttributesDataDTO] = None
    customerPurchaseOrderId: str = None
    discountProfile: str = None

    def add_line(self, item_id: str, quantity: str, price: str = None):
        line = OrderLineDTO(itemId=item_id, itemOrderQuantity=quantity)
        if price:
            line.itemPriceSnapshot = OrderItemPriceSnapshotDTO().add_rule(price=price)
        if not self.lines:
            self.lines = []
        self.lines.append(line)
        return self


@dataclass(kw_only=True)
class OrderCreateDTO(ABBaseDTO):
    order: OrderDataDTO


@dataclass(kw_only=True)
class OrderDowngradeDetailsDTO(ABBaseDTO):
    order: OrderDataDTO = None
    eventUuid: str = None


@dataclass(kw_only=True)
class OrderDetailsDTO(ABBaseDTO):
    order: OrderDataDTO = None


@dataclass(kw_only=True)
class OrderListDTO(ABBaseDTO):
    orders: list[OrderDataDTO] = None
    pagination: PaginationDTO = None


@dataclass(kw_only=True)
class OrderCancelResponseDTO(ABBaseDTO):
    order: OrderDataDTO = None


@dataclass(kw_only=True)
class AccountOrdersResponseDTO(ABBaseDTO):
    account: OrderListDTO = None


@dataclass(kw_only=True)
class OrderUpgradeDowngradeDTO(ABBaseDTO):
    preview: UpgradeDowngradePreviewDTO = None
