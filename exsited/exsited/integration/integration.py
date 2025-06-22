from exsited.exsited.integration.dto.integration_dto import LinkedAccountsResponseDTO, LinkedAccountResponseDTO
from exsited.exsited.integration.integration_api_url import IntegrationApiUrl
from exsited.http.ab_rest_processor import ABRestProcessor


class Integration(ABRestProcessor):

    def get_list_linked_objects_by_account(self, provider_uuid: str) -> LinkedAccountsResponseDTO:
        response = self.get(url=IntegrationApiUrl.INTEGRATION_LIST_LINKED_OBJECTS_BY_ACCOUNT.format(provider_uuid=provider_uuid),
                            response_obj=LinkedAccountsResponseDTO())
        return response

    def get_linked_objects_by_account_details(self, provider_uuid: str, linked_account_uuid: str) -> LinkedAccountResponseDTO:
        response = self.get(url=IntegrationApiUrl.INTEGRATION_LINKED_OBJECTS_BY_ACCOUNT_DETAILS.format(provider_uuid=provider_uuid, linked_account_uuid=linked_account_uuid),
                            response_obj=LinkedAccountResponseDTO())
        return response
