from dataclasses import dataclass
from exsited.exsited.common.dto.common_dto import TaxDTO
from exsited.sdlize.ab_base_dto import ABBaseDTO


@dataclass(kw_only=True)
class OrderItemAccountingCodeDTO(ABBaseDTO):
    salesRevenue: str = None


@dataclass(kw_only=True)
class OrderItemPricingRuleDTO(ABBaseDTO):
    price: str
    uuid: str = None
    price: str = None
    version: str = None
    priceType: str = None
    uom: str = None
    pricePeriod: str = None
    pricingSchedule: str = None
    pricingLevel: str = None
    pricingMethod: str = None
    warehouse: str = None


@dataclass(kw_only=True)
class OrderItemPropertiesDTO(ABBaseDTO):
    billingMode: str = None
    chargingPeriod: str = None
    chargingStartDate: str = None
    chargingAndBillingAlignment: bool = None
    proRataPartialChargingPeriod: bool = None
    proRataPartialPricingPeriod: bool = None


@dataclass(kw_only=True)
class OrderItemSaleTaxConfigurationDTO(ABBaseDTO):
    salePriceIsBasedOn: str = None
    taxCode: TaxDTO = None


@dataclass(kw_only=True)
class OrderItemPriceSnapshotDTO(ABBaseDTO):
    pricingRule: OrderItemPricingRuleDTO = None

    def add_rule(self, price: str):
        self.pricingRule = OrderItemPricingRuleDTO(price=price)
        return self


@dataclass(kw_only=True)
class POInformationDTO(ABBaseDTO):
    id: str = None
    name: str = None
    accountId: str = None
    currency: str = None
    itemQuantity: str = None
    itemPriceSnapshot: OrderItemPriceSnapshotDTO = None


@dataclass(kw_only=True)
class OrderPurchaseDTO(ABBaseDTO):
    createPo: str = None
    poInformation: POInformationDTO = None


@dataclass(kw_only=True)
class OrderLineDTO(ABBaseDTO):
    itemId: str = None
    itemOrderQuantity: str = None
    itemUuid: str = None
    itemName: str = None
    shippingCost: str = None
    itemInvoiceNote: str = None
    itemDescription: str = None
    itemType: str = None
    itemChargeType: str = None
    chargeItemUuid: str = None
    version: str = None
    itemPriceTax: TaxDTO = None
    isTaxExemptWhenSold: str = None

    itemPriceSnapshot: OrderItemPriceSnapshotDTO = None
    itemSaleTaxConfiguration: OrderItemSaleTaxConfigurationDTO = None
    purchaseOrder: OrderPurchaseDTO = None
    packageName: str = None
    itemSerialOrBatchNumber: str = None
    itemCustomAttributes: list = None
    op: str = None
    uuid: str = None
    itemProperties: OrderItemPropertiesDTO = None

    subtotal: str = None
    total: str = None
    tax: TaxDTO = None

    itemUom: str = None
    itemWarehouse: str = None
    pricingSnapshotUuid: str = None
    chargingStartDate: str = None
    alternateChargingStartDate: str = None
    chargingEndDate: str = None
    alternateChargingEndDate: str = None
    uuid: str = None

    itemPrice: str = None
    itemDiscountAmount: str = None
    taxAmount: str = None
    operation: str = None

    itemCustomAttributes: list[dict] = None
    itemProperties: dict = None
    itemSerialOrBatchNumber: str = None
    discount: str = None
    uom: str = None
    warehouse: str = None
    quantity: str = None
    try:
        accountingCode: dict = None
    except:
        accountingCode: str = None

    itemAccountingCode: dict = None



@dataclass(kw_only=True)
class OrderPropertiesDTO(ABBaseDTO):
    communicationProfile: str = None
    invoiceMode: str = None
    invoiceTerm: str = None
    billingPeriod: str = None
    paymentProcessor: str = None
    paymentMode: str = None
    paymentTerm: str = None
    paymentTermAlignment: str = None
    fulfillmentMode: str = None
    fulfillmentTerm: str = None


@dataclass(kw_only=True)
class ContractPropertiesDTO(ABBaseDTO):
    requireCustomerAcceptance: str = None
    requiresPaymentMethod: str = None
    initialContractTerm: str = None
    renewAutomatically: str = None
    autoRenewalEndsOn: str = None
    autoRenewalRequireCustomerAcceptance: str = None
    autoRenewalTerm: str = None
    allowEarlyTermination: str = None
    earlyTerminationMinimumPeriod: str = None
    applyEarlyTerminationCharge: str = None
    earlyTerminationChargeType: str = None
    terminationPercentageCharge: str = None
    terminationAccountingCode: str = None
    allowPostponement: str = None
    maximumDurationPerPostponement: str = None
    maximumPostponementCount: str = None
    allowTrial: str = None
    startContractAfterTrialEnds: str = None
    trialPeriod: str = None
    trialEndDate: str = None
    allowDowngrade: str = None
    periodBeforeDowngrade: str = None
    allowDowngradeCharge: str = None
    downgradeChargeType: str = None
    downgradeChargeFixed: str = None
    downgradeChargePercentage: str = None
    downgradeBillingPeriodCount: str = None
    allowUpgrade: str = None
    terminationFixedCharge: str = None
    terminationNoticePeriod: str = None


@dataclass(kw_only=True)
class OrderUpgradeDTO(ABBaseDTO):
    effectiveDate: str = None
    lines: list[OrderLineDTO] = None


@dataclass(kw_only=True)
class OrderItemPriceTaxDTO(ABBaseDTO):
    uuid: str = None
    code: str = None
    rate: str = None

@dataclass(kw_only=True)
class UpgradeDowngradePreviewDTO(ABBaseDTO):
    subTotal: str = None
    taxTotal: str = None
    discountTotal: str = None
    shippingTotal: str = None
    total: str = None
    currency: str = None




@dataclass(kw_only=True)
class KpisDTO(ABBaseDTO):
    startDate: str = None
    estimatedTotal: float = None
    totalRevenue: float = None
    monthlyRecurringRevenue: float = None
    totalCollected: float = None
    totalOutstanding: float = None
    totalDue: float = None
    lastInvoiceIssueDate: str = None
    lastInvoiceTotal: float = None
    totalInvoice: float = None
    nextInvoiceIssueDate: str = None
    lastReactivatedOn: str = None
    lastCancelledOn: str = None
    lastChangedOn: str = None
    lastDeletedOn: str = None