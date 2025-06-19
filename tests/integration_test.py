from exsited.common.ab_exception import ABException
from exsited.common.sdk_conf import SDKConfig
from exsited.exsited.exsited_sdk import ExsitedSDK
from exsited.exsited.integration.dto.integration_dto import *
from tests.common.common_data import CommonData


def test_get_integration_connections():
    SDKConfig.PRINT_REQUEST_DATA = True
    SDKConfig.PRINT_RAW_RESPONSE = False
    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(request_token_dto=CommonData.get_request_token_dto())

    try:

        response = exsited_sdk.integration.connection_list()
        print(response)

    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


def test_delete_integration_connections():
    SDKConfig.PRINT_REQUEST_DATA = True
    SDKConfig.PRINT_RAW_RESPONSE = False
    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(request_token_dto=CommonData.get_request_token_dto())

    try:

        response = exsited_sdk.integration.connection_delete(connection_uuid='922ffe4a-439f-4b1c-b671-d4387bc2ec59')
        print(response)

    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


def test_create_integration_connections():
    SDKConfig.PRINT_REQUEST_DATA = True
    SDKConfig.PRINT_RAW_RESPONSE = False
    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(request_token_dto=CommonData.get_request_token_dto())

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
    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(request_token_dto=CommonData.get_request_token_dto())

    try:

        response = exsited_sdk.integration.enable_connection(connection_uuid='f18f18c6-ac24-4b92-8a26-0a205168e966')
        print(response)

    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


def test_disable_integration_connection():
    SDKConfig.PRINT_REQUEST_DATA = True
    SDKConfig.PRINT_RAW_RESPONSE = False
    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(request_token_dto=CommonData.get_request_token_dto())

    try:

        response = exsited_sdk.integration.disable_connection(connection_uuid='f18f18c6-ac24-4b92-8a26-0a205168e966')
        print(response)

    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


def test_get_integration_connection_by_id():
    SDKConfig.PRINT_REQUEST_DATA = True
    SDKConfig.PRINT_RAW_RESPONSE = False
    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(request_token_dto=CommonData.get_request_token_dto())

    try:

        response = exsited_sdk.integration.get_connection_by_id(connection_uuid='f18f18c6-ac24-4b92-8a26-0a205168e966')
        print(response)

    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


def test_update_partner_function():
    SDKConfig.PRINT_REQUEST_DATA = True
    SDKConfig.PRINT_RAW_RESPONSE = False
    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(request_token_dto=CommonData.get_request_token_dto())

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

        connection_uuid = "75de84a3-6e62-4972-90d8-2ca5e1d36eab"
        partner_function_uuid = "08815023-9a45-4e78-9dd2-8f75c1065b9f"


        response = exsited_sdk.integration.update_partner_function(connection_uuid=connection_uuid, partner_function_uuid=partner_function_uuid, request_data=request_obj)
        print(response)

    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


def test_get_integration_linked_objects_account():
    SDKConfig.PRINT_REQUEST_DATA = True
    SDKConfig.PRINT_RAW_RESPONSE = False
    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(request_token_dto=CommonData.get_request_token_dto())

    try:
        provider_name = "aro_flo"
        response = exsited_sdk.integration.get_list_linked_objects_by_account(provider_name=provider_name)
        print(response)

    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


def test_get_integration_linked_objects_account_details():
    SDKConfig.PRINT_REQUEST_DATA = True
    SDKConfig.PRINT_RAW_RESPONSE = False
    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(request_token_dto=CommonData.get_request_token_dto())

    try:
        provider_name = "aro_flo"
        linked_account_uuid = "90a7259e-a73b-4d1c-9504-658fe8249ffb"
        response = exsited_sdk.integration.get_linked_objects_by_account_details(provider_name=provider_name, linked_account_uuid=linked_account_uuid)
        print(response)

    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


test_get_integration_linked_objects_account()
test_get_integration_linked_objects_account_details()
