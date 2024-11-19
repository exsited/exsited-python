from exsited.common.ab_exception import ABException
from exsited.common.sdk_conf import SDKConfig
from exsited.exsited.exsited_sdk import ExsitedSDK
from exsited.exsited.item_fulfillment.dto.item_fulfillment_dto import ItemFulfillmentDataDTO, FulfillmentDTO, \
    ItemFulfillmentCreateDTO
from tests.common.common_data import CommonData


def test_item_fulfillment_list():
    SDKConfig.PRINT_REQUEST_DATA = True
    SDKConfig.PRINT_RAW_RESPONSE = False
    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(request_token_dto=CommonData.get_request_token_dto())
    try:

        response = exsited_sdk.item_fulfillment.list()
        print(response)
    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


def test_item_fulfillment_create():
    SDKConfig.PRINT_REQUEST_DATA = True
    SDKConfig.PRINT_RAW_RESPONSE = False
    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(request_token_dto=CommonData.get_request_token_dto())
    try:
        fulfillment = FulfillmentDTO(itemUuid="",
                                     uuid="", fulfillmentQuantity="")
        item_fulfillment = ItemFulfillmentDataDTO(status="", date="", note="",
                                                  fulfillments=[fulfillment])
        response = exsited_sdk.item_fulfillment.create(id="", request_data=ItemFulfillmentCreateDTO(
            item_fulfillments=item_fulfillment))
        print(response)
    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


def test_item_fulfillment_details():
    SDKConfig.PRINT_REQUEST_DATA = True
    SDKConfig.PRINT_RAW_RESPONSE = False
    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(request_token_dto=CommonData.get_request_token_dto())
    try:
        response = exsited_sdk.item_fulfillment.details(id="")
        print(response)
    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


def test_item_invoice_fulfillment_list():
    SDKConfig.PRINT_REQUEST_DATA = True
    SDKConfig.PRINT_RAW_RESPONSE = False
    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(request_token_dto=CommonData.get_request_token_dto())
    try:
        response = exsited_sdk.item_fulfillment.invoice_fulfillments(id="")
        print(response)
    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


def test_item_invoice_fulfillment_by_uuid():
    SDKConfig.PRINT_REQUEST_DATA = True
    SDKConfig.PRINT_RAW_RESPONSE = False
    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(request_token_dto=CommonData.get_request_token_dto())
    try:
        response = exsited_sdk.item_fulfillment.invoice_fulfillment_by_uuid(id="", uuid="")
        print(response)
    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


# test_item_fulfillment_list()
test_item_fulfillment_create()
# test_item_fulfillment_details()
# test_item_invoice_fulfillment_list()
# test_item_invoice_fulfillment_by_uuid()
