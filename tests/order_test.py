from ab_py.autobill.autobill_sdk import AutoBillSDK
from ab_py.autobill.order.dto.order_dto import OrderCreateDTO, OrderDataDTO
from ab_py.autobill.order.dto.usage_dto import UsageCreateDTO, UsageDataDTO
from ab_py.common.ab_exception import ABException
from ab_py.common.sdk_conf import SDKConfig
from tests.common.common_data import CommonData


def test_order_create_basic():
    SDKConfig.PRINT_REQUEST_DATA = True
    SDKConfig.PRINT_RAW_RESPONSE = False

    autobill_sdk: AutoBillSDK = AutoBillSDK().init_sdk(request_token_dto=CommonData.get_request_token_dto())

    try:
        request_data = OrderCreateDTO(order=OrderDataDTO(accountId="30PS79").add_line(item_id="ITEM-0055", quantity="1"))
        response = autobill_sdk.order.create(request_data=request_data)
        print(response)
        # ResponseToObj().process(response=response)
    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


def test_order_list_basic():
    SDKConfig.PRINT_REQUEST_DATA = False
    SDKConfig.PRINT_RAW_RESPONSE = False

    autobill_sdk: AutoBillSDK = AutoBillSDK().init_sdk(request_token_dto=CommonData.get_request_token_dto())

    try:
        response = autobill_sdk.order.list()
        print(response)
        # ResponseToObj().process(response=response["accounts"][0])
    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


def test_order_details():
    SDKConfig.PRINT_REQUEST_DATA = False
    SDKConfig.PRINT_RAW_RESPONSE = False

    autobill_sdk: AutoBillSDK = AutoBillSDK().init_sdk(request_token_dto=CommonData.get_request_token_dto())

    try:
        response = autobill_sdk.order.details(id="ORD-KZ558V-0001")
        print(response)
        # ResponseToObj().process(response=resid (Account ID)ponse["accounts"][0])
    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


def test_order_cancel():
    SDKConfig.PRINT_REQUEST_DATA = True
    SDKConfig.PRINT_RAW_RESPONSE = False

    autobill_sdk: AutoBillSDK = AutoBillSDK().init_sdk(request_token_dto=CommonData.get_request_token_dto())

    try:
        response = autobill_sdk.order.cancel(id="ORD-KZ558V-0006", effective_date="2024-05-16")
        print(response)
        # ResponseToObj().process(response=response["accounts"][0])
    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)

def test_order_usage_add():
    SDKConfig.PRINT_REQUEST_DATA = True
    SDKConfig.PRINT_RAW_RESPONSE = False

    autobill_sdk: AutoBillSDK = AutoBillSDK().init_sdk(request_token_dto=CommonData.get_request_token_dto())

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
        response = autobill_sdk.order.add_usage(request_data=request_data)
    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


# test_order_cancel()
test_order_create_basic()

# test_order_usage_add()