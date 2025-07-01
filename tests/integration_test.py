from exsited.http.file_token_manager import FileTokenManager

from exsited.common.ab_exception import ABException
from exsited.common.sdk_conf import SDKConfig
from exsited.exsited.exsited_sdk import ExsitedSDK
from exsited.exsited.integration.dto.integration_dto import *
from tests.common.common_data import CommonData


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
        provider_uuid = "provider_uuid"
        response = exsited_sdk.integration.get_list_linked_objects_by_account(provider_uuid=provider_uuid)
        print(response)

    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


def test_get_integration_linked_objects_account_details():
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
        linked_account_uuid = "linked_account_uuid"
        response = exsited_sdk.integration.get_linked_objects_by_account_details(provider_uuid=provider_uuid, linked_account_uuid=linked_account_uuid)
        print(response)

    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


test_get_integration_linked_objects_account()
test_get_integration_linked_objects_account_details()
