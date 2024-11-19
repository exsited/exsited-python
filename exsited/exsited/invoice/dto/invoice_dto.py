from dataclasses import dataclass

from exsited.exsited.common.dto.common_dto import CustomFormsDTO, CurrencyDTO, PaginationDTO
from exsited.exsited.order.dto.order_nested_dto import OrderLineDTO
from exsited.sdlize.ab_base_dto import ABBaseDTO


@dataclass(kw_only=True)
class LastPaymentDTO:
    id: str = None
    amount: str = None
    created_at: str = None


@dataclass(kw_only=True)
class TaxDTO(ABBaseDTO):
    uuid: str = None
    code: str = None
    rate: float = None

@dataclass(kw_only=True)
class LineItemValueDTO(ABBaseDTO):
    tax: TaxDTO = None
    accountingCode: str = None
    lineItemName: str = None
    lineItemInvoiceNote: str = None
    lineItemQuantity: str = None
    lineItemPrice: str = None
    lineItemDiscountAmount: str = None


@dataclass(kw_only=True)
class LineItemOperationDTO(ABBaseDTO):
    operation: str = None
    uuid: str = None
    value: LineItemValueDTO = None


@dataclass(kw_only=True)
class LineOperationDTO(ABBaseDTO):
    operation: str = None
    uuid: str = None
    value: OrderLineDTO = None
    itemOrderQuantity: str = None
    itemPrice: str = None
    itemDiscountAmount: str = None



@dataclass(kw_only=True)
class InvoiceDataDTO(ABBaseDTO):
    status: str = None
    id: str = None
    type: str = None
    customerPurchaseOrderId: str = None
    billingStartDate: str = None
    alternateBillingStartDate: str = None
    billingEndDate: str = None
    alternateBillingEndDate: str = None
    issueDate: str = None
    alternateIssueDate: str = None
    dueDate: str = None
    alternateDueDate: str = None
    subtotal: str = None
    tax: str = None
    taxTotal: str = None
    total: str = None
    paid: str = None
    due: str = None
    paymentStatus: str = None
    discountAmount: str = None
    priceTaxInclusive: str = None
    invoiceNote: str = None
    accountId: str = None
    orderId: str = None
    createdBy: str = None
    createdOn: str = None
    lastUpdatedBy: str = None
    lastUpdatedOn: str = None
    uuid: str = None
    version: str = None

    lines: list[OrderLineDTO] = None

    customForms: CustomFormsDTO = None
    currency: CurrencyDTO = None

    lastPayment: LastPaymentDTO = None
    kpis: dict = None

    customAttributes: list = None
    customObjects: list = None
    customForm: CustomFormsDTO = None


@dataclass(kw_only=True)
class InvoiceDetailsDTO(ABBaseDTO):
    invoice: InvoiceDataDTO = None


@dataclass(kw_only=True)
class InvoiceCreateDTO(ABBaseDTO):
    invoice: InvoiceDataDTO


@dataclass(kw_only=True)
class InvoiceListDTO(ABBaseDTO):
    invoices: list[InvoiceDataDTO] = None
    pagination: PaginationDTO = None


@dataclass(kw_only=True)
class InvoiceAccountDTO(ABBaseDTO):
    account: InvoiceListDTO = None



