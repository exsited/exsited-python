from exsited.common.sdk_util import SDKUtil
from exsited.exsited.common.common_enum import SortDirection
from exsited.exsited.integration.dto.integration_dto import IntegrationConnectionListResponseDTO, \
    IntegrationConnectionCreateResponseDTO, IntegrationConnectionCreateRequestDTO, \
    PartnerFunctionCreateResponseDTO, LinkedAccountsResponseDTO, LinkedAccountResponseDTO, \
    IntegrationConnectionEnableResponseDTO, IntegrationConnectionDisableResponseDTO, \
    PartnerFunctionRequestDTO, PartnerFunctionUpdateResponseDTO, \
    IntegrationConnectionGetResponseDTO, PartnerFunctionEnableResponseDTO, PartnerFunctionDisableResponseDTO, \
    IntegrationConnectionConfigRequestDTO, IntegrationConnectionConfigResponseDTO, AutomationUpdateResponseDTO, \
    IntegrationAutomationListResponseDTO, IntegrationAutomationDetailsResponseDTO, PartnerFunctionListResponseDTO, \
    PartnerFunctionDetailsResponseDTO, XeroIntegrationConfigurationResponseDTO, AutomationRequestDTO, \
    AutomationCreateResponseDTO, LinkedCustomersListResponseDTO, LinkedCustomersDetailsResponseDTO
from exsited.exsited.integration.integration_api_url import IntegrationApiUrl
from exsited.http.ab_rest_processor import ABRestProcessor


class Integration(ABRestProcessor):
    def __init__(self, request_token_dto, file_token_mgr=None):
        super().__init__(request_token_dto, file_token_mgr)

    def connection_list(self) -> IntegrationConnectionListResponseDTO:
        response = self.get(url=IntegrationApiUrl.INTEGRATION_CONNECTION,
                            response_obj=IntegrationConnectionListResponseDTO())
        return response

    def automation_list(self, integration_uuid: str ) -> IntegrationAutomationListResponseDTO:
        response = self.get(url=IntegrationApiUrl.INTEGRATION_AUTOMATION_LIST.format(integration_uuid=integration_uuid),
                            response_obj=IntegrationAutomationListResponseDTO())
        return response

    def integration_configuration(self, integration_uuid: str ) -> XeroIntegrationConfigurationResponseDTO:
        response = self.get(url=IntegrationApiUrl.INTEGRATION_CONFIGURATION.format(integration_uuid=integration_uuid),
                            response_obj=XeroIntegrationConfigurationResponseDTO())
        return response

    def partner_function_list(self, integration_uuid: str ) -> PartnerFunctionListResponseDTO:
        response = self.get(url=IntegrationApiUrl.PARTNER_FUNCTION_LIST.format(integration_uuid=integration_uuid),
                            response_obj=PartnerFunctionListResponseDTO())
        return response

    def automation_details(self, integration_uuid: str, automation_uuid: str ) -> IntegrationAutomationDetailsResponseDTO:
        response = self.get(url=IntegrationApiUrl.INTEGRATION_AUTOMATION_DETAILS.format(integration_uuid=integration_uuid,automation_uuid=automation_uuid),
                            response_obj=IntegrationAutomationDetailsResponseDTO())
        return response

    def partner_function_details(self, integration_uuid: str, partner_function_uuid: str ) -> PartnerFunctionDetailsResponseDTO:
        response = self.get(url=IntegrationApiUrl.PARTNER_FUNCTION_DETAILS.format(integration_uuid=integration_uuid,partner_function_uuid=partner_function_uuid),
                            response_obj=PartnerFunctionDetailsResponseDTO())
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

    def create_automation(self, connection_uuid: str, request_data: AutomationRequestDTO) -> AutomationCreateResponseDTO:
        response = self.post(url=IntegrationApiUrl.AUTOMATION_CREATE.format(connection_uuid=connection_uuid), request_obj=request_data, response_obj=AutomationCreateResponseDTO())
        return response

    def create_partner_function(self, connection_uuid: str, request_data: PartnerFunctionRequestDTO) -> PartnerFunctionCreateResponseDTO:
        response = self.post(url=IntegrationApiUrl.PARTNER_FUNCTION_CREATE.format(connection_uuid=connection_uuid), request_obj=request_data, response_obj=PartnerFunctionCreateResponseDTO())
        return response

    def enable_partner_function(self, connection_uuid: str, partner_function_uuid: str) -> PartnerFunctionEnableResponseDTO:
        response = self.post(url=IntegrationApiUrl.PARTNER_FUNCTION_ENABLE.format(connection_uuid=connection_uuid, partner_function_uuid= partner_function_uuid),
                             response_obj=PartnerFunctionEnableResponseDTO())
        return response

    def disable_partner_function(self, connection_uuid: str, partner_function_uuid: str) -> PartnerFunctionDisableResponseDTO:
        response = self.post(url=IntegrationApiUrl.PARTNER_FUNCTION_DISABLE.format(connection_uuid=connection_uuid, partner_function_uuid= partner_function_uuid),
                             response_obj=PartnerFunctionDisableResponseDTO())
        return response

    def update_partner_function(self, connection_uuid: str, partner_function_uuid: str, request_data: PartnerFunctionRequestDTO) -> PartnerFunctionUpdateResponseDTO:
        response = self.patch(url=IntegrationApiUrl.PARTNER_FUNCTION_UPDATE.format(connection_uuid=connection_uuid, partner_function_uuid=partner_function_uuid),
                              request_obj=request_data, response_obj=PartnerFunctionUpdateResponseDTO())
        return response

    def update_automation(self, connection_uuid: str, automation_uuid: str, request_data: AutomationRequestDTO) -> AutomationUpdateResponseDTO:
        response = self.patch(url=IntegrationApiUrl.AUTOMATION_UPDATE.format(connection_uuid=connection_uuid, automation_uuid=automation_uuid),
                             request_obj=request_data, response_obj=AutomationUpdateResponseDTO())
        return response

    def update_integration_configuration(self, connection_uuid: str, request_data: IntegrationConnectionConfigRequestDTO) -> IntegrationConnectionConfigResponseDTO:
        response = self.patch(url=IntegrationApiUrl.INTEGRATION_CONNECTION_CONFIGURATION.format(connection_uuid=connection_uuid),
                              request_obj=request_data, response_obj=IntegrationConnectionConfigResponseDTO())
        return response

    def get_list_linked_objects_by_account(self, provider_uuid: str, limit: int = None, offset: int = None, direction: SortDirection = None, order_by: str = None) -> LinkedAccountsResponseDTO:
        params = SDKUtil.init_pagination_params(limit=limit, offset=offset, direction=direction, order_by=order_by)
        response = self.get(url=IntegrationApiUrl.INTEGRATION_LIST_LINKED_OBJECTS_BY_ACCOUNT.format(provider_uuid=provider_uuid), params=params,
                            response_obj=LinkedAccountsResponseDTO())
        return response

    def get_linked_objects_by_account_details(self, provider_uuid: str, linked_account_uuid: str) -> LinkedAccountResponseDTO:
        response = self.get(url=IntegrationApiUrl.INTEGRATION_LINKED_OBJECTS_BY_ACCOUNT_DETAILS.format(provider_uuid=provider_uuid, linked_account_uuid=linked_account_uuid),
                            response_obj=LinkedAccountResponseDTO())
        return response

    def get_list_linked_objects_by_customer(self, provider_uuid: str, limit: int = None, offset: int = None, direction: SortDirection = None, order_by: str = None) -> LinkedCustomersListResponseDTO:
        params = SDKUtil.init_pagination_params(limit=limit, offset=offset, direction=direction, order_by=order_by)
        response = self.get(url=IntegrationApiUrl.INTEGRATION_LIST_LINKED_OBJECTS_BY_CUSTOMER.format(provider_uuid=provider_uuid), params=params,
                            response_obj=LinkedCustomersListResponseDTO())
        return response

    def get_linked_objects_by_customer_details(self, provider_uuid: str, linked_account_uuid: str) -> LinkedCustomersDetailsResponseDTO:
        response = self.get(url=IntegrationApiUrl.INTEGRATION_LINKED_OBJECTS_BY_CUSTOMER_DETAILS.format(provider_uuid=provider_uuid, linked_account_uuid=linked_account_uuid),
                            response_obj=LinkedCustomersDetailsResponseDTO())
        return response
