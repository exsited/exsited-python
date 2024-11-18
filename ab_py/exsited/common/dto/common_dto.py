from dataclasses import dataclass
from ab_py.sdlize.ab_base_dto import ABBaseDTO


@dataclass(kw_only=True)
class CurrencyDTO(ABBaseDTO):
    uuid: str = None
    name: str = None
    link: str = None


@dataclass(kw_only=True)
class TimeZoneDTO(ABBaseDTO):
    uuid: str = None
    name: str = None
    link: str = None


@dataclass(kw_only=True)
class TaxDTO(ABBaseDTO):
    uuid: str = None
    code: str = None
    rate: str = None
    link: str = None

    amount: str = None


@dataclass(kw_only=True)
class PaginationDTO(ABBaseDTO):
    records: int = None
    limit: int = None
    offset: int = None
    previousPage: str = None
    nextPage: str = None


@dataclass(kw_only=True)
class AddressDTO(ABBaseDTO):
    addressLine1: str = None
    addressLine2: str = None
    addressLine3: str = None
    addressLine4: str = None
    addressLine5: str = None
    post_code: str = None
    city: str = None
    state: str = None
    country: str = None
    isDefaultBilling: bool = None
    isDefaultShipping: bool = None


@dataclass(kw_only=True)
class CustomAttributesDTO(ABBaseDTO):
    name: str = None
    value: str = None


@dataclass(kw_only=True)
class CustomFormsDTO(ABBaseDTO):
    uuid: str = None
    name: str = None
