from ab_py.exsited.exsited_sdk import ExsitedSDK
from ab_py.exsited.order.dto.order_dto import OrderCreateDTO, OrderDataDTO
from ab_py.exsited.order.dto.usage_dto import UsageCreateDTO, UsageDataDTO
from ab_py.common.ab_exception import ABException
from ab_py.common.sdk_conf import SDKConfig
from order_usage_db.save_to_db import SaveToDB
from tests.common.common_data import CommonData
from ab_py.exsited.order.dto.order_nested_dto import OrderPropertiesDTO


def test_order_create_basic():
    SDKConfig.PRINT_REQUEST_DATA = True
    SDKConfig.PRINT_RAW_RESPONSE = False

    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(request_token_dto=CommonData.get_request_token_dto())

    try:
        request_data = OrderCreateDTO(
            order=OrderDataDTO(accountId="QP38FA").add_line(item_id="ITEM-0015", quantity="1"))
        response = exsited_sdk.order.create(request_data=request_data)
        print(response)
        # ResponseToObj().process(response=response)

        if response.order:
            account_id = response.order.accountId
            order_id = response.order.id
            for line in response.order.lines:
                if line.itemChargeType == 'METERED':
                    SaveToDB.process(_account_id=account_id, _order_id=order_id, _item_id=line.itemId,
                                     _item_name=line.itemName, _charge_item_uuid=line.chargeItemUuid)
    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


def test_order_create_with_property():
    SDKConfig.PRINT_REQUEST_DATA = True
    SDKConfig.PRINT_RAW_RESPONSE = False
    autobill_sdk: ExsitedSDK = ExsitedSDK().init_sdk(request_token_dto=CommonData.get_request_token_dto())
    try:
        order_properties = OrderPropertiesDTO(
            invoiceMode="AUTOMATIC",
            paymentMode="MANUAL",
        )
        order_data = OrderDataDTO(
            accountId="U80A-0000000171",
            id="32446FB3-3DD0-11EF-A268-C025A5CEBA52",
            properties=order_properties
        )
        order_data.add_line(item_id="ITEM-0296", quantity="1", price=400)
        request_data = OrderCreateDTO(order=order_data)
        response = autobill_sdk.order.create(request_data=request_data)
        print(response)
    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


def test_order_list_basic():
    SDKConfig.PRINT_REQUEST_DATA = False
    SDKConfig.PRINT_RAW_RESPONSE = False

    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(request_token_dto=CommonData.get_request_token_dto())

    try:
        response = exsited_sdk.order.list()
        print(response)
        # ResponseToObj().process(response=response["accounts"][0])
    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


def test_order_details():
    SDKConfig.PRINT_REQUEST_DATA = False
    SDKConfig.PRINT_RAW_RESPONSE = False

    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(request_token_dto=CommonData.get_request_token_dto())

    try:
        response = exsited_sdk.order.details(id="B9F6DF26-39F2-11EF-8E22-C025A5CEBA5")
        print(response)
        # ResponseToObj().process(response=response["accounts"][0])
    except ABException as ab:
        # print(ab)
        # print(ab.get_errors())
        # print(ab.raw_response)
        error_code = None
        if ab.get_errors() and "errors" in ab.raw_response:
            error_code = ab.raw_response["errors"][0].get("code", None)
        print(f" {error_code}")


def test_order_cancel():
    SDKConfig.PRINT_REQUEST_DATA = True
    SDKConfig.PRINT_RAW_RESPONSE = False

    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(request_token_dto=CommonData.get_request_token_dto())

    try:
        response = exsited_sdk.order.cancel(id="32446FB3-3DD0-11EF-A268-C025A5CEBA52", effective_date="2024-07-07")
        print(response)
        # ResponseToObj().process(response=response["accounts"][0])
    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


def test_order_usage_add():
    SDKConfig.PRINT_REQUEST_DATA = True
    SDKConfig.PRINT_RAW_RESPONSE = False

    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(request_token_dto=CommonData.get_request_token_dto())

    try:
        request_data = UsageCreateDTO(
            usage=UsageDataDTO(chargeItemUuid="3cbf2ca7-ce1f-44dc-98ed-9d08716e9250",
                               chargingPeriod="2024-05-21-2024-06-20",
                               quantity="82",
                               startTime="2024-05-21 16:58:57",
                               endTime="2024-06-04 16:58:57",
                               type="INCREMENTAL",
                               )
        )
        response = exsited_sdk.order.add_usage(request_data=request_data)
    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


# test_order_create_with_property()
test_order_create_basic()
# test_order_details()
# test_order_cancel()
