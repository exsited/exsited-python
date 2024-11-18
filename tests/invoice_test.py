from ab_py.exsited.exsited_sdk import ExsitedSDK
from ab_py.common.ab_exception import ABException
from ab_py.common.sdk_conf import SDKConfig
from ab_py.exsited.order.dto.order_nested_dto import OrderLineDTO
from tests.common.common_data import CommonData
from ab_py.exsited.invoice.dto.invoice_dto import InvoiceCreateDTO, InvoiceDataDTO


def test_invoice_create_basic():
    SDKConfig.PRINT_REQUEST_DATA = True
    SDKConfig.PRINT_RAW_RESPONSE = False
    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(request_token_dto=CommonData.get_request_token_dto())
    try:
        request_data = InvoiceCreateDTO(invoice=InvoiceDataDTO(invoiceNote="Created From Python SDK"))
        response = exsited_sdk.invoice.create(id="ORD-69VUT0-0181", request_data=request_data)
    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


def test_invoice_list():
    SDKConfig.PRINT_REQUEST_DATA = False
    SDKConfig.PRINT_RAW_RESPONSE = False

    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(request_token_dto=CommonData.get_request_token_dto())

    try:
        response = exsited_sdk.invoice.list()
        print(response)
        # ResponseToObj().process(response=response["accounts"][0])
    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


def test_invoice_details():
    SDKConfig.PRINT_REQUEST_DATA = False
    SDKConfig.PRINT_RAW_RESPONSE = False

    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(request_token_dto=CommonData.get_request_token_dto())

    try:
        response = exsited_sdk.invoice.details(id="INV-JQY12I-0051")
        print(response)
    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


def test_invoice_information():
    SDKConfig.PRINT_REQUEST_DATA = False
    SDKConfig.PRINT_RAW_RESPONSE = False

    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(request_token_dto=CommonData.get_request_token_dto())

    try:
        response = exsited_sdk.invoice.information(id="INV-JQY12I-0051")
        print(response)
    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


def test_invoice_delete():
    SDKConfig.PRINT_REQUEST_DATA = False
    SDKConfig.PRINT_RAW_RESPONSE = False

    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(request_token_dto=CommonData.get_request_token_dto())

    try:
        response = exsited_sdk.invoice.delete(id="INV-2XR7V0-0416")
        print(response)
        # ResponseToObj().process(response=response["accounts"][0])
    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


def test_invoice_update_amend():
    SDKConfig.PRINT_REQUEST_DATA = True
    SDKConfig.PRINT_RAW_RESPONSE = False

    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(request_token_dto=CommonData.get_request_token_dto())

    try:
        line_dto = OrderLineDTO(
            operation="UPDATE",
            itemPrice="166.00",
            itemDiscountAmount="150.00",
            uuid="d9b49d38-f52a-4efb-a2f5-9d9423e22092", #From Line[uuid:]
        )

        request_data = InvoiceCreateDTO(invoice=InvoiceDataDTO(lines=[line_dto]))

        response = exsited_sdk.invoice.update_amend(id='INV-X011SE-0430', request_data=request_data)
        print(response)

    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)

def test_invoice_against_account():
    SDKConfig.PRINT_REQUEST_DATA = False
    SDKConfig.PRINT_RAW_RESPONSE = False

    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(request_token_dto=CommonData.get_request_token_dto())

    try:
        response = exsited_sdk.invoice.invoice_account(accountId="GPLUFW")
        print(response)
    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


def test_invoice_details_against_order():
    SDKConfig.PRINT_REQUEST_DATA = False
    SDKConfig.PRINT_RAW_RESPONSE = False

    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(request_token_dto=CommonData.get_request_token_dto())

    try:
        response = exsited_sdk.invoice.invoice_details_against_order(order_id="ORD-28A3E1-0075")
        print(response)
    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


def test_invoice_list_against_order():
    SDKConfig.PRINT_REQUEST_DATA = False
    SDKConfig.PRINT_RAW_RESPONSE = False

    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(request_token_dto=CommonData.get_request_token_dto())

    try:
        response = exsited_sdk.invoice.invoice_details_list_against_order(order_id="ORD-OSM5-000-0140")
        print(response)
    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


test_invoice_create_basic()
# test_invoice_details()
# test_invoice_list()
# test_invoice_details_against_order()
# test_invoice_information()
# test_invoice_against_account()
# test_invoice_delete()
# test_invoice_update_amend()