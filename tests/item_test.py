from ab_py.common.ab_exception import ABException
from ab_py.common.sdk_conf import SDKConfig
from ab_py.exsited.exsited_sdk import ExsitedSDK
from ab_py.exsited.item.dto.item_dto import *
from tests.common.common_data import CommonData


def test_item_list():
    SDKConfig.PRINT_REQUEST_DATA = True
    SDKConfig.PRINT_RAW_RESPONSE = False
    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(request_token_dto=CommonData.get_request_token_dto())
    try:

        response = exsited_sdk.item.list()
        print(response)
    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


def test_item_standard():
    SDKConfig.PRINT_REQUEST_DATA = True
    SDKConfig.PRINT_RAW_RESPONSE = False
    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(request_token_dto=CommonData.get_request_token_dto())
    try:

        response = exsited_sdk.item.standard(id='ITEM-0049')
        print(response)
    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


def test_item_information():
    SDKConfig.PRINT_REQUEST_DATA = True
    SDKConfig.PRINT_RAW_RESPONSE = False
    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(request_token_dto=CommonData.get_request_token_dto())
    try:

        response = exsited_sdk.item.information(id='ITEM-0049')
        print(response)
    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


def test_get_item_sale():
    SDKConfig.PRINT_REQUEST_DATA = True
    SDKConfig.PRINT_RAW_RESPONSE = False
    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(request_token_dto=CommonData.get_request_token_dto())
    try:

        response = exsited_sdk.item.sale(id='ITEM-0007')
        print(response)
    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


def test_get_item_purchase():
    SDKConfig.PRINT_REQUEST_DATA = True
    SDKConfig.PRINT_RAW_RESPONSE = False
    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(request_token_dto=CommonData.get_request_token_dto())
    try:

        response = exsited_sdk.item.purchase(id='ITEM-0007')
        print(response)
    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


def test_get_item_inventories():
    SDKConfig.PRINT_REQUEST_DATA = True
    SDKConfig.PRINT_RAW_RESPONSE = False
    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(request_token_dto=CommonData.get_request_token_dto())
    try:

        response = exsited_sdk.item.inventory(id='ITEM-0007')
        print(response)
    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


def test_create_item():
    SDKConfig.PRINT_REQUEST_DATA = True
    SDKConfig.PRINT_RAW_RESPONSE = False
    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(request_token_dto=CommonData.get_request_token_dto())

    try:
        # Currencies
        currency_one = CurrenciesDTO(
            name="AUD",
            isUsedForSale="true",
            isDefaultForSale="true",
            isUsedForPurchase="true",
            isDefaultForPurchase="true"
        )
        currency_two = CurrenciesDTO(
            name="USD",
            isUsedForSale="true",
            isDefaultForSale="false",
            isUsedForPurchase="true",
            isDefaultForPurchase="false"
        )
        currencies = []

        # UOMs
        uom_one = UomDTO(
            name="Grams",
            # isBase="true",
            saleConversionRate="1",
            purchaseConversionRate="5",
            isUsedForSale="true",
            isUsedForPurchase="true"
        )
        uom_two = UomDTO(
            name="Kilogram",
            # isBase="false",
            saleConversionRate="2",
            purchaseConversionRate="10",
            isUsedForSale="true",
            isUsedForPurchase="true"
        )
        uoms = []

        # Sale charge properties
        sale_charge_properties_one = SaleChargePropertiesDTO(name="fulfillment_mode", value="MANUAL")
        sale_charge_properties_two = SaleChargePropertiesDTO(name="fulfillment_term", value="Net 14")
        sale_charge_properties = [sale_charge_properties_one, sale_charge_properties_two]

        # Sale charge
        sale_charge = SaleChargeDTO(
            type="ONE_OFF",
            # pricePeriod=None,  # Not provided in the example
            properties=sale_charge_properties
        )

        # Sale pricing module
        sale_pricing_module = PricingModuleDTO(
            price="15.000100",
            currency="AUD",
            uom="Grams"
        )
        sale_pricing = PricingDTO(
            type="PER_UNIT_PRICING",
            version="1",
            latestUsedPricingVersion="",
            pricingModule=[sale_pricing_module]
        )

        # Sale DTO
        sale_dto = SaleDTO(
            enabled="true",
            invoiceNote="sale invoice notee",
            width=DimensionDTO(uom="centimeter", value="100.000000"),
            height=DimensionDTO(uom="centimeter", value="150.000000"),
            length=DimensionDTO(uom="centimeter", value="-180.000000"),
            weight=DimensionDTO(uom="kilogram", value="20.000005"),
            accountingCode=AccountingCodeDTO(salesRevenue="Sales Revenue"),
            defaultSalePrice="100.0",
            taxExemptWhenSold="true",
            pricingMethod="STANDARD",
            pricingSchedules=["true"],
            charge=sale_charge,
            paymentProperties=[
                SaleChargePropertiesDTO(name="payment_processor", value=""),
                SaleChargePropertiesDTO(name="payment_mode", value="MANUAL"),
                SaleChargePropertiesDTO(name="payment_term", value="Net 30")
            ],
            pricing=sale_pricing,
            pricingLevels=[PricingLevelDTO(name="Wholesale")]
        )

        # Purchase pricing module
        purchase_pricing_module_one = PricingModuleDTO(
            price="15.000100",
            currency="AUD",
            uom="Grams"
        )
        purchase_pricing_module_two = PricingModuleDTO(
            price="11.000100",
            currency="USD",
            uom="Kilogram"
        )
        purchase_pricing = PricingDTO(
            type="PER_UNIT_PRICING",
            pricingModule=[purchase_pricing_module_one, purchase_pricing_module_two]
        )

        # Purchase DTO
        purchase_dto = PurchaseDTO(
            enabled="true",
            enableSupplierManagement="false",
            purchaseOrderNote="Note",
            defaultPurchasePrice="10.000000",
            taxExemptWhenPurchase="true",
            taxConfiguration=PurchaseTaxConfigurationDTO(purchasePriceEnteredIsInclusiveOfTax="false"),
            purchaseProperties=[
                PurchasePropertiesDTO(name="receive_mode", value="MANUAL"),
                PurchasePropertiesDTO(name="receive_term", value="NET 30")
            ],
            pricing=purchase_pricing
        )

        # Create item data DTO
        item_data_dto = ItemDataDTO(
            name="SDK Item",
            displayName="from SDK",
            description="description From SDK",
            type="STANDARD",
            origin="NET_SUITE",
            invoiceNote="item invoice note 222",
            currencies=currencies,
            uoms=uoms,
            sale=sale_dto,
            purchase=purchase_dto
        )

        request_obj = ItemActionDTO(items=item_data_dto)
        response = exsited_sdk.item.create(request_data=request_obj)
        print(response)

    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


def test_item_reactivate():
    SDKConfig.PRINT_REQUEST_DATA = True
    SDKConfig.PRINT_RAW_RESPONSE = False
    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(request_token_dto=CommonData.get_request_token_dto())
    try:

        response = exsited_sdk.item.reactivate(id='ITEM-0007')
        print(response)
    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


def test_item_deactivate():
    SDKConfig.PRINT_REQUEST_DATA = True
    SDKConfig.PRINT_RAW_RESPONSE = False
    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(request_token_dto=CommonData.get_request_token_dto())
    try:

        response = exsited_sdk.item.deactivate(id='ITEM-0007')
        print(response)
    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


def test_item_delete():
    SDKConfig.PRINT_REQUEST_DATA = True
    SDKConfig.PRINT_RAW_RESPONSE = False
    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(request_token_dto=CommonData.get_request_token_dto())
    try:

        response = exsited_sdk.item.delete(id='ITEM-0077')
        print(response)
    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


# test_item_list()
# test_item_standard()
# test_item_information()
# test_get_item_sale()
# test_get_item_purchase()
# test_get_item_inventories()
# test_create_item()
# test_item_deactivate()
# test_item_reactivate()
test_item_delete()
