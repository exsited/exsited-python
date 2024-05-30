from dataclasses import dataclass
from ab_py.sdlize.ab_base_dto import ABBaseDTO


@dataclass(kw_only=True)
class PaymentProcessorDetailsDTO(ABBaseDTO):
    uuid: str = None
    name: str = None
    link: str = None


@dataclass(kw_only=True)
class PaymentMethodsDataDTO(ABBaseDTO):
    processorType: str = None
    paymentProcessor: str = None
    status: str = None
    default: str = None
    reference: str = None
    paymentCount: str = None
    lastUsedOn: str = None
    createdBy: str = None
    createdOn: str = None
    lastUpdatedBy: str = None
    lastUpdatedOn: str = None
    uuid: str = None
    version: str = None
    specifiedOrders: str = None
    useForSpecifiedOrders: str = None
    processor: PaymentProcessorDetailsDTO = None


@dataclass(kw_only=True)
class PaymentMethodsDTO(ABBaseDTO):
    paymentMethod: PaymentMethodsDataDTO


@dataclass(kw_only=True)
class PaymentMethodListDTO(ABBaseDTO):
    paymentMethods: list[PaymentMethodsDataDTO] = None


@dataclass(kw_only=True)
class PaymentCardMethodsDataDTO(PaymentMethodsDataDTO):
    cardType: str = None
    token: str = None
    cardNumber: str = None
    expiryMonth: str = None
    expiryYear: str = None


@dataclass(kw_only=True)
class PaymentCardMethodsDTO(ABBaseDTO):
    paymentMethod: PaymentCardMethodsDataDTO


@dataclass(kw_only=True)
class BillingPreferencesDTO(ABBaseDTO):
    communicationProfile: str = None
    invoiceMode: str = None
    invoiceTerm: str = None
    billingPeriod: str = None
    billingStartDate: str = None
    billingStartDayOfMonth: str = None
    chargingAndBillingAlignment: str = None
    payment_processor: str = None
    paymentMode: str = None
    paymentTerm: str = None
    paymentTermAlignment: str = None


@dataclass(kw_only=True)
class CommunicationPreferenceDTO(ABBaseDTO):
    media: str = None
    isEnabled: bool = None


@dataclass(kw_only=True)
class AccountingCodeDTO(ABBaseDTO):
    accountReceivable: str = None
