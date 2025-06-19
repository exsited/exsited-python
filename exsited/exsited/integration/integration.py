from exsited.exsited.integration.dto.integration_dto import IntegrationConnectionListResponseDTO, \
    IntegrationConnectionCreateResponseDTO, IntegrationConnectionCreateRequestDTO, \
    IntegrationConnectionEnableResponseDTO, IntegrationConnectionDisableResponseDTO, LinkedAccountsResponseDTO, \
    IntegrationConnectionGetResponseDTO, PartnerFunctionRequestDTO, PartnerFunctionUpdateResponseDTO, LinkedAccountResponseDTO
from exsited.exsited.integration.integration_api_url import IntegrationApiUrl
from exsited.http.ab_rest_processor import ABRestProcessor


class Integration(ABRestProcessor):

    def connection_list(self) -> IntegrationConnectionListResponseDTO:
        response = self.get(url=IntegrationApiUrl.INTEGRATION_CONNECTION,
                            response_obj=IntegrationConnectionListResponseDTO())
        return response

    def connection_delete(self, connection_uuid: str):
        response = self.delete_request(url=IntegrationApiUrl.INTEGRATION_DELETE.format(connection_uuid=connection_uuid),
                                       response_obj={})
        return response

    def create_connection(self, request_data: IntegrationConnectionCreateRequestDTO) -> IntegrationConnectionCreateResponseDTO:
        response = self.post(url=IntegrationApiUrl.INTEGRATION_CONNECTION_CREATE,
                             request_obj=request_data, response_obj=IntegrationConnectionCreateResponseDTO())
        return response

    def enable_connection(self, connection_uuid: str) -> IntegrationConnectionEnableResponseDTO:
        response = self.post(url=IntegrationApiUrl.INTEGRATION_CONNECTION_ENABLE.format(connection_uuid=connection_uuid),
                             response_obj=IntegrationConnectionEnableResponseDTO())
        return response

    def disable_connection(self, connection_uuid: str) -> IntegrationConnectionDisableResponseDTO:
        response = self.post(url=IntegrationApiUrl.INTEGRATION_CONNECTION_DISABLE.format(connection_uuid=connection_uuid),
                             response_obj=IntegrationConnectionDisableResponseDTO())
        return response

    def get_connection_by_id(self, connection_uuid: str) -> IntegrationConnectionGetResponseDTO:
        response = self.get(url=IntegrationApiUrl.INTEGRATION_CONNECTION_BY_ID.format(connection_uuid=connection_uuid),
                            response_obj=IntegrationConnectionGetResponseDTO())
        return response

    def update_partner_function(self, connection_uuid: str, partner_function_uuid: str, request_data: PartnerFunctionRequestDTO) -> PartnerFunctionUpdateResponseDTO:
        response = self.patch(url=IntegrationApiUrl.PARTNER_FUNCTION_UPDATE.format(connection_uuid=connection_uuid, partner_function_uuid=partner_function_uuid),
                              request_obj=request_data, response_obj=PartnerFunctionUpdateResponseDTO())
        return response

    def get_list_linked_objects_by_account(self, provider_name: str) -> LinkedAccountsResponseDTO:
        response = self.get(url=IntegrationApiUrl.INTEGRATION_LIST_LINKED_OBJECTS_BY_ACCOUNT.format(provider_name=provider_name),
                            response_obj=LinkedAccountsResponseDTO())
        return response

    def get_linked_objects_by_account_details(self, provider_name: str, linked_account_uuid: str) -> LinkedAccountResponseDTO:
        response = self.get(url=IntegrationApiUrl.INTEGRATION_LINKED_OBJECTS_BY_ACCOUNT_DETAILS.format(provider_name=provider_name, linked_account_uuid=linked_account_uuid),
                            response_obj=LinkedAccountResponseDTO())
        return response
