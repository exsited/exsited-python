from ab_py.autobill.account.account_api_url import AccountApiUrl
from ab_py.autobill.account.dto.account_dto import AccountCreateDTO, AccountDetailsDTO, AccountListDTO, \
    AccountUpdateInformationDTO, PaymentMethodsAddDTO, PaymentMethodsDetailsDTO, PaymentCardMethodsAddDTO, \
    PaymentMethodsListDTO
from ab_py.autobill.common.common_enum import SortDirection
from ab_py.common.sdk_util import SDKUtil
from ab_py.http.ab_rest_processor import ABRestProcessor


class Account(ABRestProcessor):

    def create(self, request_data: AccountCreateDTO) -> AccountDetailsDTO:
        response = self.post(url=AccountApiUrl.ACCOUNTS, request_obj=request_data, response_obj=AccountDetailsDTO())
        return response

    def update_information(self, id: str, request_data: AccountUpdateInformationDTO) -> AccountDetailsDTO:
        response = self.patch(url=AccountApiUrl.ACCOUNT_UPDATE_INFORMATION.format(id=id), request_obj=request_data, response_obj=AccountDetailsDTO())
        return response

    def list(self, limit: int = None, offset: int = None, direction: SortDirection = None, order_by: str = None) -> AccountListDTO:
        params = SDKUtil.init_pagination_params(limit=limit, offset=offset, direction=direction, order_by=order_by)
        response = self.get(url=AccountApiUrl.ACCOUNTS, params=params, response_obj=AccountListDTO())
        return response

    def details(self, id: str) -> AccountDetailsDTO:
        response = self.get(url=AccountApiUrl.ACCOUNTS + f"/{id}", response_obj=AccountDetailsDTO())
        return response

    def delete(self, id: str):
        response = self.delete_request(url=AccountApiUrl.ACCOUNTS + f"/{id}")
        return response

    def add_payment_method(self, account_id: str, request_data: PaymentMethodsAddDTO) -> PaymentMethodsDetailsDTO:
        response = self.post(url=AccountApiUrl.ACCOUNT_PAYMENT_METHODS.format(id=account_id), request_obj=request_data, response_obj=PaymentMethodsDetailsDTO())
        return response

    def add_payment_card_method(self, account_id: str, request_data: PaymentCardMethodsAddDTO) -> PaymentMethodsDetailsDTO:
        response = self.post(url=AccountApiUrl.ACCOUNT_PAYMENT_METHODS.format(id=account_id), request_obj=request_data, response_obj=PaymentMethodsDetailsDTO())
        return response

    def list_payment_method(self, account_id: str) -> PaymentMethodsListDTO:
        response = self.get(url=AccountApiUrl.ACCOUNT_PAYMENT_METHODS.format(id=account_id), response_obj=PaymentMethodsListDTO())
        return response

    def delete_payment_method(self, account_id: str, reference: str):
        response = self.delete_request(url=AccountApiUrl.EACH_PAYMENT_METHODS.format(id=account_id, reference=reference))
        return response

    def payment_method_details(self, account_id: str, reference: str) -> PaymentMethodsDetailsDTO:
        response = self.get(url=AccountApiUrl.EACH_PAYMENT_METHODS.format(id=account_id, reference=reference), response_obj=PaymentMethodsDetailsDTO())
        return response
