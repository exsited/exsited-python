from exsited.common.sdk_util import SDKUtil
from exsited.exsited.common.common_enum import SortDirection
from exsited.exsited.integration.dto.integration_dto import LinkedAccountsResponseDTO, LinkedAccountResponseDTO
from exsited.exsited.integration.integration_api_url import IntegrationApiUrl
from exsited.http.ab_rest_processor import ABRestProcessor


class Integration(ABRestProcessor):

    def get_list_linked_objects_by_account(self, provider_uuid: str, limit: int = None, offset: int = None, direction: SortDirection = None,
                                           order_by: str = None) -> LinkedAccountsResponseDTO:
        params = SDKUtil.init_pagination_params(limit=limit, offset=offset, direction=direction, order_by=order_by)
        response = self.get(url=IntegrationApiUrl.INTEGRATION_LIST_LINKED_OBJECTS_BY_ACCOUNT.format(provider_uuid=provider_uuid), params=params,
                            response_obj=LinkedAccountsResponseDTO())
        return response

    def get_linked_objects_by_account_details(self, provider_uuid: str, linked_account_uuid: str) -> LinkedAccountResponseDTO:
        response = self.get(url=IntegrationApiUrl.INTEGRATION_LINKED_OBJECTS_BY_ACCOUNT_DETAILS.format(provider_uuid=provider_uuid, linked_account_uuid=linked_account_uuid),
                            response_obj=LinkedAccountResponseDTO())
        return response
