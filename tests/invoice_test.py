from ab_py.autobill.autobill_sdk import AutoBillSDK
from ab_py.common.ab_exception import ABException
from ab_py.common.sdk_conf import SDKConfig
from tests.common.common_data import CommonData


def test_invoice_list():
    SDKConfig.PRINT_REQUEST_DATA = False
    SDKConfig.PRINT_RAW_RESPONSE = False

    autobill_sdk: AutoBillSDK = AutoBillSDK().init_sdk(request_token_dto=CommonData.get_request_token_dto())

    try:
        response = autobill_sdk.invoice.list()
        print(response)
        # ResponseToObj().process(response=response["accounts"][0])
    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


def test_invoice_details():
    SDKConfig.PRINT_REQUEST_DATA = False
    SDKConfig.PRINT_RAW_RESPONSE = False

    autobill_sdk: AutoBillSDK = AutoBillSDK().init_sdk(request_token_dto=CommonData.get_request_token_dto())

    try:
        response = autobill_sdk.invoice.details(id="INV-KZ558V-0004")
        print(response)
    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


test_invoice_list()
# test_invoice_details()
