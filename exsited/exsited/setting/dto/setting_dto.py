from dataclasses import dataclass
from exsited.sdlize.ab_base_dto import ABBaseDTO


@dataclass(kw_only=True)
class PaymentProcessorDTO(ABBaseDTO):
    uuid: str = None
    status: str = None
    default: str = None
    name: str = None
    displayName: str = None
    description: str = None
    provider: str = None
    currency: str = None


@dataclass(kw_only=True)
class SettingPaymentProcessorListDTO(ABBaseDTO):
    paymentProcessors: list[PaymentProcessorDTO] = None
