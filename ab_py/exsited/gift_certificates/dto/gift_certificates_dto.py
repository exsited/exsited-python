from dataclasses import dataclass

from ab_py.exsited.item.dto.item_dto import PaginationDTO
from ab_py.exsited.order.dto.order_dto import CustomAttributesDataDTO
from ab_py.sdlize.ab_base_dto import ABBaseDTO


@dataclass(kw_only=True)
class AllocationDTO(ABBaseDTO):
    account: str = None
    type: str = None
    date: str = None


@dataclass(kw_only=True)
class TransactionDTO(ABBaseDTO):
    accountingCode: str = None
    type: str = None
    date: str = None
    amount: float = None
    currency: str = None
    reference: str = None


@dataclass(kw_only=True)
class GiftCertificateDTO(ABBaseDTO):
    status: str = None
    account: str = None
    accountingCode: str = None
    code: str = None
    amount: str = None
    remainingBalance: str = None
    usedAmount: str = None
    currency: str = None
    expiryDate: str = None
    createdBy: str = None
    createdOn: str = None
    lastUpdatedBy: str = None
    lastUpdatedOn: str = None
    uuid: str = None
    customAttributes: list[CustomAttributesDataDTO] = None
    allocations: list[AllocationDTO] = None
    transactions: list[TransactionDTO] = None


@dataclass(kw_only=True)
class AllocationListDataDTO(ABBaseDTO):
    allocations: list[AllocationDTO] = None
    pagination: PaginationDTO = None


@dataclass(kw_only=True)
class TransactionListDataDTO(ABBaseDTO):
    transactions: list[TransactionDTO] = None
    pagination: PaginationDTO = None


@dataclass(kw_only=True)
class GiftCertificatesListDTO(ABBaseDTO):
    giftCertificates: list[GiftCertificateDTO] = None
    pagination: PaginationDTO = None


@dataclass(kw_only=True)
class GiftCertificateAllocationListDTO(ABBaseDTO):
    giftCertificate: AllocationListDataDTO = None


@dataclass(kw_only=True)
class GiftCertificateTransactionsListDTO(ABBaseDTO):
    giftCertificate: TransactionListDataDTO = None


@dataclass(kw_only=True)
class GiftCertificateDetailsDTO(ABBaseDTO):
    giftCertificate: GiftCertificateDTO = None
