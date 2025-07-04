
class IntegrationApiUrl:
    INTEGRATION_CONNECTION = "api/v2/integration-connections"
    INTEGRATION_DELETE = "/api/v3/integration/{connection_uuid}"
    INTEGRATION_CONNECTION_CREATE = "/api/v3/integration"
    INTEGRATION_CONNECTION_ENABLE = "/api/v3/integration/{connection_uuid}/enable"
    INTEGRATION_CONNECTION_DISABLE = "/api/v3/integration/{connection_uuid}/disable"
    INTEGRATION_AUTOMATION_LIST = "/api/v3/integration/{integration_uuid}/automation"
    INTEGRATION_AUTOMATION_DETAILS = "/api/v3/integration/{integration_uuid}/automation/{automation_uuid}"
    PARTNER_FUNCTION_LIST = "/api/v3/integration/{integration_uuid}/partner-function/"
    PARTNER_FUNCTION_DETAILS = "/api/v3/integration/{integration_uuid}/partner-function/{partner_function_uuid}"
    INTEGRATION_CONFIGURATION = "/api/v3/integration/{integration_uuid}/configuration"
    INTEGRATION_CONNECTION_BY_ID = "/api/v2/integration-connections/{connection_uuid}"
    PARTNER_FUNCTION_CREATE = "/api/v3/integration/{connection_uuid}/partner-function/"
    INTEGRATION_LIST_LINKED_OBJECTS_BY_ACCOUNT = "/api/v3/integration/{provider_uuid}/linked-accounts"
    INTEGRATION_LIST_LINKED_OBJECTS_BY_CUSTOMER = "/api/v3/integration/{provider_uuid}/linked-customers"
    INTEGRATION_LINKED_OBJECTS_BY_ACCOUNT_DETAILS = "/api/v3/integration/{provider_uuid}/linked-accounts/{linked_account_uuid}"
    INTEGRATION_LINKED_OBJECTS_BY_CUSTOMER_DETAILS = "/api/v3/integration/{provider_uuid}/linked-customers/{linked_account_uuid}"
    INTEGRATION_LINKED_OBJECTS_BY_CUSTOMER_QUOTES = "/api/v3/integration/{provider_uuid}/linked-customers/{linked_account_uuid}/quotes"
    INTEGRATION_LINKED_QUOTES_LIST = "/api/v3/integration/{provider_uuid}/linked-quotes"
    INTEGRATION_LINKED_QUOTE_DETAILS = "/api/v3/integration/{provider_uuid}/linked-quotes/{quotes_uuid}"
    PARTNER_FUNCTION_UPDATE = "/api/v3/integration/{connection_uuid}/partner-function/{partner_function_uuid}"
    INTEGRATION_CONNECTION_CONFIGURATION = "/api/v3/integration/{connection_uuid}/configuration"
    AUTOMATION_UPDATE = "/api/v3/integration/{connection_uuid}/automation/{automation_uuid}"
    PARTNER_FUNCTION_ENABLE = "/api/v3/integration/{connection_uuid}/partner-function/{partner_function_uuid}/enable"
    PARTNER_FUNCTION_DISABLE = "/api/v3/integration/{connection_uuid}/partner-function/{partner_function_uuid}/disable"
    AUTOMATION_CREATE = "/api/v3/integration/{connection_uuid}/automation"