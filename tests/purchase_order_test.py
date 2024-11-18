from ab_py.exsited.common.dto.common_dto import TaxDTO
from ab_py.exsited.exsited_sdk import ExsitedSDK
from ab_py.exsited.purchase_order.dto.purchase_order_dto import PurchaseOrderListDTO, PurchaseOrderDetailsDTO, \
    PurchaseOrderDTO, PurchaseOrderCurrencyDTO, PurchaseOrderLineDTO, PurchaseOrderItemPriceSnapshotDTO, \
    PurchaseOrderPricingRuleDTO, PurchaseOrderItemPurchaseTaxConfigurationDTO, PurchaseOrderTaxCodeDTO, \
    PurchaseOrderItemAccountingCodeDTO, PurchaseOrderCreateDTO, PurchaseOrderDataDTO
from ab_py.common.ab_exception import ABException
from ab_py.common.sdk_conf import SDKConfig
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
        response = exsited_sdk.purchase_order.details(id='ownerxyz12456')
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
            currency="AUD",
            issueDate="2024-10-31",
            dueDate="2024-11-01",
            expectedCompletionDate="2024-11-01",
            priceTaxInclusive="true",
            purchaseOrderNote="",
            accountId="QJ2OWQ",
            lines=[
                PurchaseOrderLineDTO(
                    itemUuid="0d257e95-7a10-490f-a716-b77a2cdb2ea5",
                    itemQuantity="1.000000",
                    itemPriceSnapshot=PurchaseOrderItemPriceSnapshotDTO(
                        pricingRule=PurchaseOrderPricingRuleDTO(
                            priceType="INCREMENTAL_PER_UNIT_PRICING",
                            price="200.000000"
                        )
                    ),
                    itemPurchaseTaxConfiguration=PurchaseOrderItemPurchaseTaxConfigurationDTO(
                        purchasePriceIsTaxInclusive="true",
                        taxCode=PurchaseOrderTaxCodeDTO(
                            uuid="d166b28c-395b-4692-87b9-7408a01b72c0",
                            code="GST",
                            rate="10.000000",
                            link="https://app-stage.exsited.com/api/v1/taxes/d166b28c-395b-4692-87b9-7408a01b72c0"
                        )
                    ),
                    itemPriceTaxExempt="false",
                    itemPriceTax=TaxDTO(
                        uuid="d166b28c-395b-4692-87b9-7408a01b72c0",
                        code="GST",
                        rate="10.000000",
                        link="https://app-stage.exsited.com/api/v1/taxes/d166b28c-395b-4692-87b9-7408a01b72c0"
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
