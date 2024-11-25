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

    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(request_token_dto=CommonData.get_request_token_dto())

    try:
        response = exsited_sdk.purchase_order.list()
        print(response)
        # ResponseToObj().process(response=response["purchase_orders"][0])
    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


def test_purchase_order_details():
    SDKConfig.PRINT_REQUEST_DATA = False
    SDKConfig.PRINT_RAW_RESPONSE = False

    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(request_token_dto=CommonData.get_request_token_dto())

    try:
        response = exsited_sdk.purchase_order.details(id='')
        print(response)
        return response
        # ResponseToObj().process(response=response["purchase_order"])
    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


def test_purchase_order_create():
    SDKConfig.PRINT_REQUEST_DATA = False
    SDKConfig.PRINT_RAW_RESPONSE = False

    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(request_token_dto=CommonData.get_request_token_dto())

    try:
        purchase_order_data = PurchaseOrderDataDTO(
            currency="",
            issueDate="",
            dueDate="",
            expectedCompletionDate="",
            priceTaxInclusive="",
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
                        purchasePriceIsTaxInclusive="true",
                        taxCode=PurchaseOrderTaxCodeDTO(
                            uuid="",
                            code="",
                            rate="",
                            link=""
                        )
                    ),
                    itemPriceTaxExempt="",
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



test_purchase_order_list_basic()
# test_purchase_order_details()
# test_purchase_order_create()
