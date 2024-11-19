from exsited.exsited.exsited_sdk import ExsitedSDK
from exsited.common.ab_exception import ABException
from exsited.common.sdk_conf import SDKConfig
from tests.common.common_data import CommonData


def test_get_settings():
    SDKConfig.PRINT_REQUEST_DATA = False
    SDKConfig.PRINT_RAW_RESPONSE = True

    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(request_token_dto=CommonData.get_request_token_dto())

    try:
        response = exsited_sdk.setting.get_settings()
        print(response)
    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


def test_get_settings_payment_processor():
    SDKConfig.PRINT_REQUEST_DATA = False
    SDKConfig.PRINT_RAW_RESPONSE = True

    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(request_token_dto=CommonData.get_request_token_dto())

    try:
        response = exsited_sdk.setting.get_settings_payment_processor()
        print(response)
    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)

# Run the test
# test_get_settings()
test_get_settings_payment_processor()