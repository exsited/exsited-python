from ab_py.common.sdk_util import SDKUtil
from ab_py.exsited.common.common_enum import SortDirection
from ab_py.exsited.gift_certificates.dto.gift_certificates_dto import GiftCertificatesListDTO, \
    GiftCertificateDetailsDTO, GiftCertificateAllocationListDTO, GiftCertificateTransactionsListDTO
from ab_py.exsited.gift_certificates.gift_certificates_api_url import GiftCertificatesApiUrl
from ab_py.http.ab_rest_processor import ABRestProcessor


class GiftCertificates(ABRestProcessor):

    def list(self, limit: int = None, offset: int = None, direction: SortDirection = None,
             order_by: str = None) -> GiftCertificatesListDTO:
        params = SDKUtil.init_pagination_params(limit=limit, offset=offset, direction=direction, order_by=order_by)
        response = self.get(url=GiftCertificatesApiUrl.GIFT_CERTIFICATES, params=params,
                            response_obj=GiftCertificatesListDTO())
        return response

    def details(self, id: str) -> GiftCertificateDetailsDTO:
        response = self.get(url=GiftCertificatesApiUrl.GIFT_CERTIFICATE_DETAIL.format(uuid=id),
                            response_obj=GiftCertificateDetailsDTO())
        return response

    def allocation_list(self, id: str, limit: int = None, offset: int = None, direction: SortDirection = None,
                        order_by: str = None) -> GiftCertificateAllocationListDTO:
        params = SDKUtil.init_pagination_params(limit=limit, offset=offset, direction=direction, order_by=order_by)
        response = self.get(url=GiftCertificatesApiUrl.GIFT_CERTIFICATE_ALLOCATIONS.format(uuid=id), params=params,
                            response_obj=GiftCertificateAllocationListDTO())
        return response

    def transaction_list(self, id: str, limit: int = None, offset: int = None, direction: SortDirection = None,
                         order_by: str = None) -> GiftCertificateTransactionsListDTO:
        params = SDKUtil.init_pagination_params(limit=limit, offset=offset, direction=direction, order_by=order_by)
        response = self.get(url=GiftCertificatesApiUrl.GIFT_CERTIFICATE_TRANSACTIONS.format(uuid=id), params=params,
                            response_obj=GiftCertificateTransactionsListDTO())
        return response

    def create(self, request_data: GiftCertificateDetailsDTO) -> GiftCertificateDetailsDTO:
        response = self.post(url=GiftCertificatesApiUrl.GIFT_CERTIFICATES, request_obj=request_data,
                             response_obj=GiftCertificateDetailsDTO())
        return response

    def disable(self, id: str) -> GiftCertificateDetailsDTO:
        response = self.post(url=GiftCertificatesApiUrl.GIFT_CERTIFICATE_DISABLE.format(uuid=id),
                             response_obj=GiftCertificateDetailsDTO())
        return response

    def enable(self, id: str) -> GiftCertificateDetailsDTO:
        response = self.post(url=GiftCertificatesApiUrl.GIFT_CERTIFICATE_ENABLE.format(uuid=id),
                             response_obj=GiftCertificateDetailsDTO())
        return response

    def allocate(self, id: str, request_data: GiftCertificateDetailsDTO) -> GiftCertificateAllocationListDTO:
        response = self.post(url=GiftCertificatesApiUrl.GIFT_CERTIFICATE_ALLOCATE.format(uuid=id),
                             request_obj=request_data, response_obj=GiftCertificateAllocationListDTO())
        return response

    def deallocate(self, id: str, request_data: GiftCertificateDetailsDTO) -> GiftCertificateAllocationListDTO:
        response = self.post(url=GiftCertificatesApiUrl.GIFT_CERTIFICATE_DEALLOCATE.format(uuid=id),
                             request_obj=request_data, response_obj=GiftCertificateAllocationListDTO())
        return response

    def amend(self, id: str, request_data: GiftCertificateDetailsDTO) -> GiftCertificateDetailsDTO:
        response = self.post(url=GiftCertificatesApiUrl.GIFT_CERTIFICATE_AMEND.format(uuid=id),
                             request_obj=request_data, response_obj=GiftCertificateDetailsDTO())
        return response

    def update(self, id: str, request_data: GiftCertificateDetailsDTO) -> GiftCertificateDetailsDTO:
        response = self.patch(url=GiftCertificatesApiUrl.GIFT_CERTIFICATE_DETAIL.format(uuid=id),
                              request_obj=request_data, response_obj=GiftCertificateDetailsDTO())
        return response

    def delete(self, id: str):
        response = self.delete_request(url=GiftCertificatesApiUrl.GIFT_CERTIFICATE_DETAIL.format(uuid=id),
                                       response_obj=dict())
        return response
