from exsited.common.ab_exception import ABException
from exsited.common.sdk_conf import SDKConfig
from exsited.exsited.exsited_sdk import ExsitedSDK
from exsited.exsited.item.dto.item_dto import *
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

        response = exsited_sdk.item.standard(id='')
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

        response = exsited_sdk.item.information(id='')
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

        response = exsited_sdk.item.sale(id='')
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

        response = exsited_sdk.item.purchase(id='')
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

        response = exsited_sdk.item.inventory(id='')
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
            name="",
            isUsedForSale="",
            isDefaultForSale="",
            isUsedForPurchase="",
            isDefaultForPurchase=""
        )
        currency_two = CurrenciesDTO(
            name="",
            isUsedForSale="",
            isDefaultForSale="",
            isUsedForPurchase="",
            isDefaultForPurchase=""
        )
        currencies = []

        # UOMs
        uom_one = UomDTO(
            name="",
            # isBase="true",
            saleConversionRate="",
            purchaseConversionRate="",
            isUsedForSale="",
            isUsedForPurchase=""
        )
        uom_two = UomDTO(
            name="",
            # isBase="false",
            saleConversionRate="",
            purchaseConversionRate="",
            isUsedForSale="",
            isUsedForPurchase=""
        )
        uoms = []

        # Sale charge properties
        sale_charge_properties_one = SaleChargePropertiesDTO(name="", value="")
        sale_charge_properties_two = SaleChargePropertiesDTO(name="", value="")
        sale_charge_properties = [sale_charge_properties_one, sale_charge_properties_two]

        # Sale charge
        sale_charge = SaleChargeDTO(
            type="",
            # pricePeriod=None,  # Not provided in the example
            properties=sale_charge_properties
        )

        # Sale pricing module
        sale_pricing_module = PricingModuleDTO(
            price="",
            currency="",
            uom=""
        )
        sale_pricing = PricingDTO(
            type="",
            version="",
            latestUsedPricingVersion="",
            pricingModule=[sale_pricing_module]
        )

        # Sale DTO
        sale_dto = SaleDTO(
            enabled="true",
            invoiceNote="",
            width=DimensionDTO(uom="", value=""),
            height=DimensionDTO(uom="", value=""),
            length=DimensionDTO(uom="", value="-"),
            weight=DimensionDTO(uom="", value=""),
            accountingCode=AccountingCodeDTO(salesRevenue=""),
            defaultSalePrice="",
            taxExemptWhenSold="",
            pricingMethod="",
            pricingSchedules=[""],
            charge=sale_charge,
            paymentProperties=[
                SaleChargePropertiesDTO(name="", value=""),
                SaleChargePropertiesDTO(name="", value=""),
                SaleChargePropertiesDTO(name="", value=" ")
            ],
            pricing=sale_pricing,
            pricingLevels=[PricingLevelDTO(name="")]
        )

        # Purchase pricing module
        purchase_pricing_module_one = PricingModuleDTO(
            price="",
            currency="",
            uom=""
        )
        purchase_pricing_module_two = PricingModuleDTO(
            price="",
            currency="",
            uom=""
        )
        purchase_pricing = PricingDTO(
            type="",
            pricingModule=[purchase_pricing_module_one, purchase_pricing_module_two]
        )

        # Purchase DTO
        purchase_dto = PurchaseDTO(
            enabled="",
            enableSupplierManagement="",
            purchaseOrderNote="",
            defaultPurchasePrice="",
            taxExemptWhenPurchase="",
            taxConfiguration=PurchaseTaxConfigurationDTO(purchasePriceEnteredIsInclusiveOfTax=""),
            purchaseProperties=[
                PurchasePropertiesDTO(name="", value=""),
                PurchasePropertiesDTO(name="", value="")
            ],
            pricing=purchase_pricing
        )

        # Create item data DTO
        item_data_dto = ItemDataDTO(
            name="",
            displayName="",
            description="",
            type="",
            origin="",
            invoiceNote="",
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

        response = exsited_sdk.item.reactivate(id='')
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

        response = exsited_sdk.item.deactivate(id='')
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

        response = exsited_sdk.item.delete(id='')
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
