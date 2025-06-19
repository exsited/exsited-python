
class IntegrationApiUrl:
    INTEGRATION_CONNECTION = "api/v2/integration-connections"
    INTEGRATION_DELETE = "/api/v3/integration/{connection_uuid}"
    INTEGRATION_CONNECTION_CREATE = "/api/v3/integration"
    INTEGRATION_CONNECTION_ENABLE = "/api/v3/integration/{connection_uuid}/enable"
    INTEGRATION_CONNECTION_DISABLE = "/api/v3/integration/{connection_uuid}/disable"
    INTEGRATION_CONNECTION_BY_ID = "/api/v2/integration-connections/{connection_uuid}"
    INTEGRATION_LIST_LINKED_OBJECTS_BY_ACCOUNT = "/api/v3/integration/{provider_name}/linked-objects/account"
    INTEGRATION_LINKED_OBJECTS_BY_ACCOUNT_DETAILS = "/api/v3/integration/{provider_name}/linked-objects/account/{linked_account_uuid}"
    PARTNER_FUNCTION_UPDATE = "/api/v3/integration/{connection_uuid}/partner-function/{partner_function_uuid}"
