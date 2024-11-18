from ab_py.common.ab_exception import ABException
from ab_py.common.sdk_conf import SDKConfig
from ab_py.exsited.exsited_sdk import ExsitedSDK
from ab_py.exsited.item_fulfillment.dto.item_fulfillment_dto import ItemFulfillmentDataDTO, FulfillmentDTO, \
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
        fulfillment = FulfillmentDTO(itemUuid="5c869d45-115b-43e6-9c95-bb5e5dbec951",
                                     uuid="01a252fb-9d81-4ae1-8a3a-d0a45e350aa4", fulfillmentQuantity="1")
        item_fulfillment = ItemFulfillmentDataDTO(status="SHIPPED", date="2024-10-28", note="Test",
                                                  fulfillments=[fulfillment])
        response = exsited_sdk.item_fulfillment.create(id="INV-QP38FA-0401", request_data=ItemFulfillmentCreateDTO(
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
        response = exsited_sdk.item_fulfillment.details(id="FF-67081064")
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
        response = exsited_sdk.item_fulfillment.invoice_fulfillments(id="INV-QP38FA-0393")
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
        response = exsited_sdk.item_fulfillment.invoice_fulfillment_by_uuid(id="INV-QP38FA-0393", uuid="FF-70795451")
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
