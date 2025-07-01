from exsited.http.file_token_manager import FileTokenManager

from exsited.exsited.common.dto.common_dto import TaxDTO
from exsited.exsited.exsited_sdk import ExsitedSDK
from exsited.exsited.purchase_order.dto.purchase_order_dto import PurchaseOrderListDTO, PurchaseOrderDetailsDTO, \
    PurchaseOrderDTO, PurchaseOrderCurrencyDTO, PurchaseOrderLineDTO, PurchaseOrderItemPriceSnapshotDTO, \
    PurchaseOrderPricingRuleDTO, PurchaseOrderItemPurchaseTaxConfigurationDTO, PurchaseOrderTaxCodeDTO, \
    PurchaseOrderItemAccountingCodeDTO, PurchaseOrderCreateDTO, PurchaseOrderDataDTO
from exsited.common.ab_exception import ABException
from exsited.common.sdk_conf import SDKConfig
from tests.common.common_data import CommonData


def test_purchase_order_list_basic():
    SDKConfig.PRINT_REQUEST_DATA = False
    SDKConfig.PRINT_RAW_RESPONSE = False

    token_file_path = "shared_token.json"
    file_token_mgr = FileTokenManager(token_file_path)

    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(
        request_token_dto=CommonData.get_request_token_dto(),
        file_token_mgr=file_token_mgr
    )

    try:
        response = exsited_sdk.purchase_order.list()
        print(response)

    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


def test_purchase_order_details():
    SDKConfig.PRINT_REQUEST_DATA = False
    SDKConfig.PRINT_RAW_RESPONSE = False

    token_file_path = "shared_token.json"
    file_token_mgr = FileTokenManager(token_file_path)

    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(
        request_token_dto=CommonData.get_request_token_dto(),
        file_token_mgr=file_token_mgr
    )

    try:
        response = exsited_sdk.purchase_order.details(id='')
        print(response)
        return response

    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


def test_purchase_order_reactivate():
    SDKConfig.PRINT_REQUEST_DATA = False
    SDKConfig.PRINT_RAW_RESPONSE = False

    token_file_path = "shared_token.json"
    file_token_mgr = FileTokenManager(token_file_path)

    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(
        request_token_dto=CommonData.get_request_token_dto(),
        file_token_mgr=file_token_mgr
    )

    try:
        response = exsited_sdk.purchase_order.reactivate(id="")
        print(response)
    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


def test_purchase_order_cancel():
    SDKConfig.PRINT_REQUEST_DATA = False
    SDKConfig.PRINT_RAW_RESPONSE = False

    token_file_path = "shared_token.json"
    file_token_mgr = FileTokenManager(token_file_path)

    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(
        request_token_dto=CommonData.get_request_token_dto(),
        file_token_mgr=file_token_mgr
    )

    try:
        response = exsited_sdk.purchase_order.cancel(id="")
        print(response)
    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


def test_purchase_order_delete():
    SDKConfig.PRINT_REQUEST_DATA = False
    SDKConfig.PRINT_RAW_RESPONSE = False

    token_file_path = "shared_token.json"
    file_token_mgr = FileTokenManager(token_file_path)

    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(
        request_token_dto=CommonData.get_request_token_dto(),
        file_token_mgr=file_token_mgr
    )

    try:
        response = exsited_sdk.purchase_order.delete(id='')
        print(response)
        return response

    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


def test_purchase_order_information():
    SDKConfig.PRINT_REQUEST_DATA = False
    SDKConfig.PRINT_RAW_RESPONSE = False

    token_file_path = "shared_token.json"
    file_token_mgr = FileTokenManager(token_file_path)

    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(
        request_token_dto=CommonData.get_request_token_dto(),
        file_token_mgr=file_token_mgr
    )

    try:
        response = exsited_sdk.purchase_order.information(id='')
        print(response)
        return response

    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)

def test_purchase_order_line_uuid():
    SDKConfig.PRINT_REQUEST_DATA = False
    SDKConfig.PRINT_RAW_RESPONSE = False

    token_file_path = "shared_token.json"
    file_token_mgr = FileTokenManager(token_file_path)

    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(
        request_token_dto=CommonData.get_request_token_dto(),
        file_token_mgr=file_token_mgr
    )

    try:
        response = exsited_sdk.purchase_order.line_uuid(id='', uuid='')
        print(response)
        return response

    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


def test_purchase_order_line():
    SDKConfig.PRINT_REQUEST_DATA = False
    SDKConfig.PRINT_RAW_RESPONSE = False

    token_file_path = "shared_token.json"
    file_token_mgr = FileTokenManager(token_file_path)

    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(
        request_token_dto=CommonData.get_request_token_dto(),
        file_token_mgr=file_token_mgr
    )

    try:
        response = exsited_sdk.purchase_order.po_line(id='')
        print(response)
        return response

    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


def test_purchase_order_create():
    SDKConfig.PRINT_REQUEST_DATA = False
    SDKConfig.PRINT_RAW_RESPONSE = False

    token_file_path = "shared_token.json"
    file_token_mgr = FileTokenManager(token_file_path)

    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(
        request_token_dto=CommonData.get_request_token_dto(),
        file_token_mgr=file_token_mgr
    )

    try:
        purchase_order_data = PurchaseOrderDataDTO(
            currency="",
            issueDate="",
            dueDate="",
            expectedCompletionDate="",
            priceTaxInclusive="False",
            purchaseOrderNote="",
            accountId="",
            lines=[
                PurchaseOrderLineDTO(
                    itemUuid="",
                    itemQuantity="",
                    itemPriceSnapshot=PurchaseOrderItemPriceSnapshotDTO(
                        pricingRule=PurchaseOrderPricingRuleDTO(
                            priceType="",
                            price=""
                        )
                    ),
                    itemPurchaseTaxConfiguration=PurchaseOrderItemPurchaseTaxConfigurationDTO(
                        purchasePriceIsTaxInclusive="False",
                        taxCode=PurchaseOrderTaxCodeDTO(
                            uuid="",
                            code="",
                            rate="",
                            link=""
                        )
                    ),
                    itemPriceTaxExempt="false",
                    itemPriceTax=TaxDTO(
                        uuid="",
                        code="",
                        rate="",
                        link=""
                    ),
                    purchaseOrderNote="",
                    itemAccountingCode=PurchaseOrderItemAccountingCodeDTO(
                        costOfGoodsSold=""
                    )
                )
            ]
        )
        request_obj = PurchaseOrderCreateDTO(purchaseOrder=purchase_order_data)
        response = exsited_sdk.purchase_order.create(request_data=request_obj)
        print(response)

    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)
