from exsited.common.ab_exception import ABException
from exsited.common.sdk_conf import SDKConfig
from exsited.exsited.exsited_sdk import ExsitedSDK
from exsited.exsited.integration.dto.integration_dto import *
from exsited.http.file_token_manager import FileTokenManager
from tests.common.common_data import CommonData


def test_get_integration_connections():
    SDKConfig.PRINT_REQUEST_DATA = True
    SDKConfig.PRINT_RAW_RESPONSE = False

    token_file_path = "shared_token.json"
    file_token_mgr = FileTokenManager(token_file_path)

    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(
        request_token_dto=CommonData.get_request_token_dto(),
        file_token_mgr=file_token_mgr
    )

    try:
        response = exsited_sdk.integration.connection_list()
        print(response)

    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


def test_get_integration_automation_list():
    SDKConfig.PRINT_REQUEST_DATA = True
    SDKConfig.PRINT_RAW_RESPONSE = False

    token_file_path = "shared_token.json"
    file_token_mgr = FileTokenManager(token_file_path)

    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(
        request_token_dto=CommonData.get_request_token_dto(),
        file_token_mgr=file_token_mgr
    )

    try:
        response = exsited_sdk.integration.automation_list(integration_uuid='integration_uuid')
        print(response)

    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


def test_get_integration_partner_function_list():
    SDKConfig.PRINT_REQUEST_DATA = True
    SDKConfig.PRINT_RAW_RESPONSE = False

    token_file_path = "shared_token.json"
    file_token_mgr = FileTokenManager(token_file_path)

    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(
        request_token_dto=CommonData.get_request_token_dto(),
        file_token_mgr=file_token_mgr
    )

    try:
        response = exsited_sdk.integration.partner_function_list(integration_uuid='integration_uuid')
        print(response)

    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


def test_get_integration_configuration():
    SDKConfig.PRINT_REQUEST_DATA = True
    SDKConfig.PRINT_RAW_RESPONSE = False

    token_file_path = "shared_token.json"
    file_token_mgr = FileTokenManager(token_file_path)

    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(
        request_token_dto=CommonData.get_request_token_dto(),
        file_token_mgr=file_token_mgr
    )

    try:
        response = exsited_sdk.integration.integration_configuration(integration_uuid='integration_uuid')
        print(response)

    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


def test_get_integration_automation_details():
    SDKConfig.PRINT_REQUEST_DATA = True
    SDKConfig.PRINT_RAW_RESPONSE = False

    token_file_path = "shared_token.json"
    file_token_mgr = FileTokenManager(token_file_path)

    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(
        request_token_dto=CommonData.get_request_token_dto(),
        file_token_mgr=file_token_mgr
    )

    try:

        response = exsited_sdk.integration.automation_details(integration_uuid='integration_uuid',automation_uuid='automation_uuid')
        print(response)

    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


def test_get_integration_partner_function_details():
    SDKConfig.PRINT_REQUEST_DATA = True
    SDKConfig.PRINT_RAW_RESPONSE = False

    token_file_path = "shared_token.json"
    file_token_mgr = FileTokenManager(token_file_path)

    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(
        request_token_dto=CommonData.get_request_token_dto(),
        file_token_mgr=file_token_mgr
    )

    try:
        response = exsited_sdk.integration.partner_function_details(integration_uuid='integration_uuid',partner_function_uuid='partner_function_uuid')
        print(response)

    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


def test_delete_integration_connections():
    SDKConfig.PRINT_REQUEST_DATA = True
    SDKConfig.PRINT_RAW_RESPONSE = False

    token_file_path = "shared_token.json"
    file_token_mgr = FileTokenManager(token_file_path)

    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(
        request_token_dto=CommonData.get_request_token_dto(),
        file_token_mgr=file_token_mgr
    )

    try:
        response = exsited_sdk.integration.connection_delete(connection_uuid='connection_uuid')
        print(response)

    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


def test_create_integration_connections():
    SDKConfig.PRINT_REQUEST_DATA = True
    SDKConfig.PRINT_RAW_RESPONSE = False

    token_file_path = "shared_token.json"
    file_token_mgr = FileTokenManager(token_file_path)

    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(
        request_token_dto=CommonData.get_request_token_dto(),
        file_token_mgr=file_token_mgr
    )

    try:
        request_obj = IntegrationConnectionCreateRequestDTO(
            provider="XERO",
            remoteInstanceId="dummy-tenant-id-001",
            remoteInstanceCode="TENANT-XYZ",
            remoteInstanceName="Xero Test Company",
            remoteInstanceDisplay="Xero Test Company (dummy-tenant-id-001)",

            integrationClientId="dummy-client-id",
            integrationClientSecret="dummy-client-secret",

            integrationAccessToken="dummy-access-token",
            integrationRefreshToken="dummy-refresh-token",
            tokenType="Bearer",
            expiresIn="2026-01-01",

            accountServer="https://api.xero.com",
            apiDomain="https://api.trena.xero.com",

            supportingFields='{"region":"US","tax":"NONE"}',

            userName="test_user",
            userPassword="test_password",

            requireAuthentication=True,
            state="development",

            companyFile="00000000-0000-0000-0000-000000000000",
            companyName="Demo Bitmascot",
        )

        response = exsited_sdk.integration.create_connection(request_data=request_obj)
        print(response)

    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


def test_enable_integration_connection():
    SDKConfig.PRINT_REQUEST_DATA = True
    SDKConfig.PRINT_RAW_RESPONSE = False

    token_file_path = "shared_token.json"
    file_token_mgr = FileTokenManager(token_file_path)

    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(
        request_token_dto=CommonData.get_request_token_dto(),
        file_token_mgr=file_token_mgr
    )

    try:

        response = exsited_sdk.integration.enable_connection(connection_uuid='connection-uuid')
        print(response)

    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


def test_disable_integration_connection():
    SDKConfig.PRINT_REQUEST_DATA = True
    SDKConfig.PRINT_RAW_RESPONSE = False

    token_file_path = "shared_token.json"
    file_token_mgr = FileTokenManager(token_file_path)

    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(
        request_token_dto=CommonData.get_request_token_dto(),
        file_token_mgr=file_token_mgr
    )

    try:
        response = exsited_sdk.integration.disable_connection(connection_uuid='connection-uuid')
        print(response)

    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


def test_get_integration_connection_by_id():
    SDKConfig.PRINT_REQUEST_DATA = True
    SDKConfig.PRINT_RAW_RESPONSE = False

    token_file_path = "shared_token.json"
    file_token_mgr = FileTokenManager(token_file_path)

    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(
        request_token_dto=CommonData.get_request_token_dto(),
        file_token_mgr=file_token_mgr
    )

    try:

        response = exsited_sdk.integration.get_connection_by_id(connection_uuid='connection-uuid')
        print(response)

    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


def test_create_partner_function():
    SDKConfig.PRINT_REQUEST_DATA = True
    SDKConfig.PRINT_RAW_RESPONSE = False

    token_file_path = "shared_token.json"
    file_token_mgr = FileTokenManager(token_file_path)

    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(
        request_token_dto=CommonData.get_request_token_dto(),
        file_token_mgr=file_token_mgr
    )

    try:

        request_obj = PartnerFunctionRequestDTO(
            partnerFunction=PartnerFunctionDTO(
                name="Partner Function 340",
                direction="IMPORT",
                description="Description",
                objectName="customer",
                objectMapping="customer_customer",
                eventName="update",
                tag="import_only_inventory"
            )
        )

        connection_uuid = "connection-uuid"

        response = exsited_sdk.integration.create_partner_function(connection_uuid=connection_uuid, request_data=request_obj)
        print(response)

    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


def test_enable_partner_function():
    SDKConfig.PRINT_REQUEST_DATA = True
    SDKConfig.PRINT_RAW_RESPONSE = False

    token_file_path = "shared_token.json"
    file_token_mgr = FileTokenManager(token_file_path)

    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(
        request_token_dto=CommonData.get_request_token_dto(),
        file_token_mgr=file_token_mgr
    )

    try:

        connection_uuid = "connection-uuid"
        partner_function_uuid = "partner-function-uuid"

        response = exsited_sdk.integration.enable_partner_function(connection_uuid, partner_function_uuid)
        print(response)

    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


def test_disable_partner_function():
    SDKConfig.PRINT_REQUEST_DATA = True
    SDKConfig.PRINT_RAW_RESPONSE = False

    token_file_path = "shared_token.json"
    file_token_mgr = FileTokenManager(token_file_path)

    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(
        request_token_dto=CommonData.get_request_token_dto(),
        file_token_mgr=file_token_mgr
    )

    try:
        connection_uuid = "connection-uuid"
        partner_function_uuid = "partner-function-uuid"

        response = exsited_sdk.integration.disable_partner_function(connection_uuid, partner_function_uuid)
        print(response)

    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


def test_update_partner_function():
    SDKConfig.PRINT_REQUEST_DATA = True
    SDKConfig.PRINT_RAW_RESPONSE = False

    token_file_path = "shared_token.json"
    file_token_mgr = FileTokenManager(token_file_path)

    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(
        request_token_dto=CommonData.get_request_token_dto(),
        file_token_mgr=file_token_mgr
    )

    try:

        request_obj = PartnerFunctionRequestDTO(
            partnerFunction=PartnerFunctionDTO(
                name="Partner Function 99",
                direction="IMPORT",
                description="Description",
                objectName="customer",
                objectMapping="customer_customer",
                eventName="update",
                tag="import_only_inventory"
            )
        )

        connection_uuid = "connection-uuid"
        partner_function_uuid = "partner-function-uuid"


        response = exsited_sdk.integration.update_partner_function(connection_uuid=connection_uuid, partner_function_uuid=partner_function_uuid, request_data=request_obj)
        print(response)

    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


def test_update_integration_configuration():
    SDKConfig.PRINT_REQUEST_DATA = True
    SDKConfig.PRINT_RAW_RESPONSE = False

    token_file_path = "shared_token.json"
    file_token_mgr = FileTokenManager(token_file_path)

    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(
        request_token_dto=CommonData.get_request_token_dto(),
        file_token_mgr=file_token_mgr
    )

    try:

        request_obj = IntegrationConnectionConfigRequestDTO(
            account=AccountDTO(
                export=AccountImportExportDTO(
                    enabled="true",
                    defaultAccountReceivable="Sales",
                    accountReceivableMapping=AccountMappingDTO(
                        enabled="true",
                        mappings=[
                            MappingDTO(source="Test", target="Sales"),
                            MappingDTO(source="Test 2", target="Other Revenue"),
                        ],
                    ),
                    defaultAccountPayable="Sales",
                    accountPayableMapping=AccountMappingDTO(
                        enabled="true",
                        mappings=[
                            MappingDTO(source="Account Payable", target="Other Revenue"),
                            MappingDTO(source="Payable 2", target="Sales"),
                        ],
                    ),
                    defaultTax=None,
                    taxMapping=AccountMappingDTO(
                        enabled="false",
                        mappings=[],
                    ),
                    xeroAccountNumberField="assigned_by_xero",
                    syncToXero="true",
                ),
                import_=AccountImportExportDTO(
                    enabled="true",
                    defaultAccountReceivable="Account Receivable",
                    accountReceivableMapping=AccountMappingDTO(
                        enabled="true",
                        mappings=[
                            MappingDTO(source="Sales", target="Account Receivable"),
                            MappingDTO(source="Other Revenue", target="Test 2"),
                        ],
                    ),
                    defaultAccountPayable="Account Payable",
                    accountPayableMapping=AccountMappingDTO(
                        enabled="true",
                        mappings=[
                            MappingDTO(source="Cleaning", target="Account Payable"),
                            MappingDTO(source="Depreciation", target="Payable 2"),
                        ],
                    ),
                    xeroAccountIdField="assigned_by_exsited",
                ),
            ),
            transaction=TransactionDTO(
                invoice=InvoiceDTO(
                    export=InvoiceExportDTO(
                        enabled="true",
                        defaultSalesRevenue="Other Revenue",
                        salesRevenueMapping=SalesRevenueMappingDTO(
                            enabled="true",
                            mappings=[
                                MappingDTO(source="Sales Revenue", target="Sales"),
                                MappingDTO(source="SR 2", target="Other Revenue"),
                            ],
                        ),
                        xeroInvoiceNumberField="assigned_by_xero",
                        syncToXero="true",
                    )
                )
            )
        )

        connection_uuid = "connection-uuid"

        response = exsited_sdk.integration.update_integration_configuration(connection_uuid, request_data=request_obj)
        print(response)

    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


def test_update_automation():
    SDKConfig.PRINT_REQUEST_DATA = True
    SDKConfig.PRINT_RAW_RESPONSE = False

    token_file_path = "shared_token.json"
    file_token_mgr = FileTokenManager(token_file_path)

    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(
        request_token_dto=CommonData.get_request_token_dto(),
        file_token_mgr=file_token_mgr
    )

    try:

        request_obj = AutomationRequestDTO(
            integration=IntegrationDTO(
                automationDetails=AutomationDetailsDTO(
                    name="Edited Copy 54",
                    displayName="Automation three",
                    code="Code123",
                    descriptionEnabled="True",
                    description="description added",
                    anotherAutomation="",
                    appliesTo="supplier",
                    appliesToFunction="new",
                    automationType="timerBased",
                    checkOn="4 hours",
                    customDay="thursday",
                    customTime="06:45:23",
                    direction="EXPORT",
                    doNotOverWriteLatestData="true",
                    ignoreThreshold="2",
                    performAction="performAction_uuid",
                    sinceLastLookUp="true",
                    additionalCriteria="true",
                    propertyName=""
                ),
                additionalCriteriaDetails=[
                    AdditionalCriteriaDTO(
                        groupCondition="AND",
                        rules=[
                            CriteriaRuleDTO(
                                fieldName="AccountNumber",
                                operator="EQUALS",
                                value="1",
                                condition="AND"
                            )
                        ]
                    ),
                    AdditionalCriteriaDTO(
                        groupCondition="OR",
                        rules=[
                            CriteriaRuleDTO(
                                fieldName="Accounts Payable Tax Type",
                                operator="HAS_VALUE",
                                value=None,
                                condition="OR"
                            ),
                            CriteriaRuleDTO(
                                fieldName="Accounts Receivable Tax Type",
                                operator="CONTAINS",
                                value="@yopmail.com",
                                condition="AND"
                            )
                        ]
                    ),
                    AdditionalCriteriaDTO(
                        groupCondition="AND",
                        rules=[
                            CriteriaRuleDTO(
                                fieldName="Contact ID",
                                operator="DOES_NOT_HAVE_VALUE",
                                value=None,
                                condition="AND"
                            ),
                            CriteriaRuleDTO(
                                fieldName="Bank Account Details",
                                operator="EQUALS",
                                value="429",
                                condition="AND"
                            )
                        ]
                    )
                ]
            )
        )

        connection_uuid = "connection-uuid"
        automation_uuid = "automation-uuid"

        response = exsited_sdk.integration.update_automation(connection_uuid, automation_uuid, request_data=request_obj)
        print(response)

    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


def test_create_automation():
    SDKConfig.PRINT_REQUEST_DATA = True
    SDKConfig.PRINT_RAW_RESPONSE = False

    token_file_path = "shared_token.json"
    file_token_mgr = FileTokenManager(token_file_path)

    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(
        request_token_dto=CommonData.get_request_token_dto(),
        file_token_mgr=file_token_mgr
    )

    try:

        request_obj = AutomationRequestDTO(
                integration=IntegrationDTO(
                    automationDetails=AutomationDetailsDTO(
                        name="Test auto 258",
                        displayName="Test auto 1",
                        code="test2",
                        descriptionEnabled="true",
                        description="checking3578",
                        anotherAutomation="Automation four",
                        appliesTo="supplier",
                        appliesToFunction="new",
                        automationType="timerBased",
                        direction="IMPORT",
                        checkOn="8 hours",
                        customDay="thursday",
                        customTime="06:45:23",
                        doNotOverWriteLatestData="true",
                        ignoreThreshold="1",
                        performAction="performAction-uuid",
                        sinceLastLookUp="true",
                        additionalCriteria="true",
                        propertyName=""
                    ),
                    additionalCriteriaDetails=[
                        AdditionalCriteriaDTO(
                            groupCondition="AND",
                            rules=[
                                CriteriaRuleDTO(
                                    fieldName="AccountNumber",
                                    operator="EQUALS",
                                    value="1QKGUL",
                                    condition="AND"
                                ),
                                CriteriaRuleDTO(
                                    fieldName="ContactID",
                                    operator="DOES_NOT_HAVE_VALUE",
                                    value=None,
                                    condition="AND"
                                )
                            ]
                        )
                    ]
                )
            )

        connection_uuid = "connection-uuid"

        response = exsited_sdk.integration.create_automation(connection_uuid, request_data=request_obj)
        print(response)

    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


def test_get_integration_linked_objects_account():
    SDKConfig.PRINT_REQUEST_DATA = True
    SDKConfig.PRINT_RAW_RESPONSE = False

    token_file_path = "shared_token.json"
    file_token_mgr = FileTokenManager(token_file_path)

    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(
        request_token_dto=CommonData.get_request_token_dto(),
        file_token_mgr=file_token_mgr
    )

    try:
        provider_uuid = "provider-uuid"
        response = exsited_sdk.integration.get_list_linked_objects_by_account(provider_uuid=provider_uuid)
        print(response)

    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


def test_get_integration_linked_objects_account_details():
    SDKConfig.PRINT_REQUEST_DATA = True
    SDKConfig.PRINT_RAW_RESPONSE = True

    token_file_path = "shared_token.json"
    file_token_mgr = FileTokenManager(token_file_path)

    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(
        request_token_dto=CommonData.get_request_token_dto(),
        file_token_mgr=file_token_mgr
    )

    try:
        provider_uuid = "provider_uuid"
        linked_account_uuid = "linked_account_uuid"
        response = exsited_sdk.integration.get_linked_objects_by_account_details(provider_uuid=provider_uuid, linked_account_uuid=linked_account_uuid)
        print(response)

    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)

def test_get_integration_linked_objects_customer():
    SDKConfig.PRINT_REQUEST_DATA = True
    SDKConfig.PRINT_RAW_RESPONSE = False

    token_file_path = "shared_token.json"
    file_token_mgr = FileTokenManager(token_file_path)

    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(
        request_token_dto=CommonData.get_request_token_dto(),
        file_token_mgr=file_token_mgr
    )

    try:
        provider_uuid = "provider_uuid"
        response = exsited_sdk.integration.get_list_linked_objects_by_customer(provider_uuid=provider_uuid)
        print(response)

    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


def test_get_integration_linked_objects_customer_details():
    SDKConfig.PRINT_REQUEST_DATA = True
    SDKConfig.PRINT_RAW_RESPONSE = True

    token_file_path = "shared_token.json"
    file_token_mgr = FileTokenManager(token_file_path)

    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(
        request_token_dto=CommonData.get_request_token_dto(),
        file_token_mgr=file_token_mgr
    )

    try:
        provider_uuid = "provider_uuid"
        linked_account_uuid = "linked_account_uuid"
        response = exsited_sdk.integration.get_linked_objects_by_customer_details(provider_uuid=provider_uuid, linked_account_uuid=linked_account_uuid)
        print(response)

    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)

def test_get_integration_linked_objects_customer_quotes():
    SDKConfig.PRINT_REQUEST_DATA = True
    SDKConfig.PRINT_RAW_RESPONSE = True

    token_file_path = "shared_token.json"
    file_token_mgr = FileTokenManager(token_file_path)

    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(
        request_token_dto=CommonData.get_request_token_dto(),
        file_token_mgr=file_token_mgr
    )

    try:
        provider_uuid = "provider_uuid"
        linked_account_uuid = "linked_account_uuid"
        response = exsited_sdk.integration.get_linked_objects_by_customer_quotes(provider_uuid=provider_uuid, linked_account_uuid=linked_account_uuid, limit=1)
        print(response)

    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)