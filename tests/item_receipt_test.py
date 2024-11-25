from exsited.exsited.common.dto.common_dto import TaxDTO
from exsited.exsited.exsited_sdk import ExsitedSDK
from exsited.common.ab_exception import ABException
from exsited.common.sdk_conf import SDKConfig
from tests.common.common_data import CommonData


def test_item_receipt_list_basic():
    SDKConfig.PRINT_REQUEST_DATA = False
    SDKConfig.PRINT_RAW_RESPONSE = False

    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(request_token_dto=CommonData.get_request_token_dto())

    try:
        response = exsited_sdk.item_receipt.list()
        print(response)
        # ResponseToObj().process(response=response["purchase_orders"][0])
    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


def test_item_receipt_details():
    SDKConfig.PRINT_REQUEST_DATA = False
    SDKConfig.PRINT_RAW_RESPONSE = False

    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(request_token_dto=CommonData.get_request_token_dto())

    try:
        response = exsited_sdk.item_receipt.details(id='ORD_A81SU1_AJ7J8A')
        print(response)
        return response
        # ResponseToObj().process(response=response["purchase_order"])
    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)

def test_purchase_order_item_receipt_details():
    SDKConfig.PRINT_REQUEST_DATA = False
    SDKConfig.PRINT_RAW_RESPONSE = False

    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(request_token_dto=CommonData.get_request_token_dto())

    try:
        response = exsited_sdk.item_receipt.purchase_order_details(id='ORD_A81SU1_AJ7J8A')
        print(response)
        return response
        # ResponseToObj().process(response=response["purchase_order"])
    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)

test_item_receipt_details()
