from exsited.http.file_token_manager import FileTokenManager

from exsited.exsited.exsited_sdk import ExsitedSDK
from exsited.common.ab_exception import ABException
from exsited.common.sdk_conf import SDKConfig
from tests.common.common_data import CommonData


def test_credit_note_details():
    SDKConfig.PRINT_REQUEST_DATA = False
    SDKConfig.PRINT_RAW_RESPONSE = False

    token_file_path = "shared_token.json"
    file_token_mgr = FileTokenManager(token_file_path)

    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(
        request_token_dto=CommonData.get_request_token_dto(),
        file_token_mgr=file_token_mgr
    )

    try:
        response = exsited_sdk.credit_note.details(id='')
        print(response)
        return response

    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


def test_credit_note_application_list():
    SDKConfig.PRINT_REQUEST_DATA = False
    SDKConfig.PRINT_RAW_RESPONSE = False

    token_file_path = "shared_token.json"
    file_token_mgr = FileTokenManager(token_file_path)

    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(
        request_token_dto=CommonData.get_request_token_dto(),
        file_token_mgr=file_token_mgr
    )

    try:
        response = exsited_sdk.credit_note.credit_note_application_list()
        print(response)
        return response

    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


def test_credit_note_application_details():
    SDKConfig.PRINT_REQUEST_DATA = False
    SDKConfig.PRINT_RAW_RESPONSE = False

    token_file_path = "shared_token.json"
    file_token_mgr = FileTokenManager(token_file_path)

    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(
        request_token_dto=CommonData.get_request_token_dto(),
        file_token_mgr=file_token_mgr
    )

    try:
        response = exsited_sdk.credit_note.credit_note_application_details(uuid='')
        print(response)
        return response

    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)

def test_invoice_credit_note_application_list():
    SDKConfig.PRINT_REQUEST_DATA = False
    SDKConfig.PRINT_RAW_RESPONSE = False

    token_file_path = "shared_token.json"
    file_token_mgr = FileTokenManager(token_file_path)

    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(
        request_token_dto=CommonData.get_request_token_dto(),
        file_token_mgr=file_token_mgr
    )

    try:
        response = exsited_sdk.credit_note.invoice_credit_note_application_list(id='')
        print(response)
        return response

    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)