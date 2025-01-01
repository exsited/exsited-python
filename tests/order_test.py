from exsited.exsited.account.dto.account_nested_dto import CommunicationPreferenceDTO
from exsited.exsited.common.dto.common_dto import TaxDTO
from exsited.exsited.exsited_sdk import ExsitedSDK
from exsited.exsited.order.dto.order_dto import OrderCreateDTO, OrderDataDTO
from exsited.exsited.order.dto.usage_dto import UsageCreateDTO, UsageDataDTO
from exsited.common.ab_exception import ABException
from exsited.common.sdk_conf import SDKConfig
from order_usage_db.save_to_db import SaveToDB
from tests.common.common_data import CommonData
from exsited.exsited.order.dto.order_nested_dto import OrderPropertiesDTO, OrderPurchaseDTO, POInformationDTO, \
    OrderItemPriceSnapshotDTO, OrderItemPricingRuleDTO, OrderLineDTO, ContractPropertiesDTO, OrderUpgradeDTO, \
    OrderItemPriceTaxDTO, OrderItemAccountingCodeDTO
from exsited.exsited.order.dto.order_nested_dto import OrderPropertiesDTO, OrderPurchaseDTO, POInformationDTO, \
    OrderItemPriceSnapshotDTO, OrderItemPricingRuleDTO, OrderLineDTO, ContractPropertiesDTO

def test_order_create_basic():
    SDKConfig.PRINT_REQUEST_DATA = False
    SDKConfig.PRINT_RAW_RESPONSE = False

    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(request_token_dto=CommonData.get_request_token_dto())

    try:
        request_data = OrderCreateDTO(
            order=OrderDataDTO(accountId="").add_line(item_id="", quantity="1"))
        response = exsited_sdk.order.create(request_data=request_data)
        print(response)

        # if response.order:
        #     account_id = response.order.accountId
        #     order_id = response.order.id
        #     for line in response.order.lines:
        #         if line.itemChargeType == 'METERED':
        #             SaveToDB.process(_account_id=account_id, _order_id=order_id, _item_id=line.itemId,
        #                              _item_name=line.itemName, _charge_item_uuid=line.chargeItemUuid)

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
            accountId="",
            id="",  #Order ID
            properties=order_properties
        )
        order_data.add_line(item_id="", quantity="", price=10)
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

    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


def test_order_details(id: str):
    SDKConfig.PRINT_REQUEST_DATA = False
    SDKConfig.PRINT_RAW_RESPONSE = False

    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(request_token_dto=CommonData.get_request_token_dto())

    try:
        response = exsited_sdk.order.details(id=id)
        print(response)
        return response

    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)
        error_code = None
        if ab.get_errors() and "errors" in ab.raw_response:
            error_code = ab.raw_response["errors"][0].get("code", None)
        print(f" {error_code}")


def test_order_usages_details():
    SDKConfig.PRINT_REQUEST_DATA = False
    SDKConfig.PRINT_RAW_RESPONSE = False

    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(request_token_dto=CommonData.get_request_token_dto())

    try:
        response = exsited_sdk.order.usage_details(uuid='')
        print(response)
        return response

    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


def test_order_usages_delete():
    SDKConfig.PRINT_REQUEST_DATA = False
    SDKConfig.PRINT_RAW_RESPONSE = False

    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(request_token_dto=CommonData.get_request_token_dto())

    try:
        response = exsited_sdk.order.usage_delete(uuid="")
        print(response)

    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


def test_order_cancel():
    SDKConfig.PRINT_REQUEST_DATA = False
    SDKConfig.PRINT_RAW_RESPONSE = False

    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(request_token_dto=CommonData.get_request_token_dto())

    try:
        response = exsited_sdk.order.cancel(id="", effective_date="") # Order ID and DATE (YYYY-MM-DD)
        print(response)

    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


def test_order_usage_add():
    SDKConfig.PRINT_REQUEST_DATA = False
    SDKConfig.PRINT_RAW_RESPONSE = False

    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(request_token_dto=CommonData.get_request_token_dto())

    try:
        request_data = UsageCreateDTO(
            usage=UsageDataDTO(chargeItemUuid="",
                               chargingPeriod="", #Date
                               quantity="10",
                               startTime="", #Date
                               endTime="", #Date
                               type="INCREMENTAL",
                               )
        )

        response = exsited_sdk.order.add_usage(request_data=request_data)
        print(response)

    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


def test_order_usage_modify():
    SDKConfig.PRINT_REQUEST_DATA = False
    SDKConfig.PRINT_RAW_RESPONSE = False

    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(request_token_dto=CommonData.get_request_token_dto())

    request_data = UsageCreateDTO(usage=UsageDataDTO(quantity="1", startTime="", endTime=""))

    try:
        response = exsited_sdk.order.usage_modify(uuid='', request_data=request_data)
        print(response)
        return response
    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


def test_order_usage_update():
    SDKConfig.PRINT_REQUEST_DATA = False
    SDKConfig.PRINT_RAW_RESPONSE = False

    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(request_token_dto=CommonData.get_request_token_dto())

    request_data = UsageCreateDTO(usage=UsageDataDTO(quantity="1", startTime="", endTime=""))

    try:
        response = exsited_sdk.order.usage_update(uuid='', request_data=request_data)
        print(response)
        return response

    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


def test_order_usage_list():
    SDKConfig.PRINT_REQUEST_DATA = False
    SDKConfig.PRINT_RAW_RESPONSE = False

    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(request_token_dto=CommonData.get_request_token_dto())

    try:
        response = exsited_sdk.order.usage_list()
        print(response)

    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


def test_order_create_with_purchase_order():
    SDKConfig.PRINT_REQUEST_DATA = False
    SDKConfig.PRINT_RAW_RESPONSE = False

    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(request_token_dto=CommonData.get_request_token_dto())

    try:

        land_owner_purchase = OrderPurchaseDTO(createPo="true",
                                               poInformation=POInformationDTO(id="", accountId="",
                                                                              currency="AUD", itemQuantity="1",
                                                                              itemPriceSnapshot=OrderItemPriceSnapshotDTO
                                                                                  (pricingRule=OrderItemPricingRuleDTO(
                                                                                  price="100.00"))))
        land_owner_line = OrderLineDTO(itemId="", itemOrderQuantity="1",
                                       itemPriceSnapshot=OrderItemPriceSnapshotDTO
                                       (pricingRule=OrderItemPricingRuleDTO(price="50.00")),
                                       purchaseOrder=land_owner_purchase
                                       )

        software_owner_purchase = OrderPurchaseDTO(createPo="true",
                                                   poInformation=POInformationDTO(id="", accountId="",
                                                                                  currency="AUD",
                                                                                  itemQuantity="1",
                                                                                  itemPriceSnapshot=OrderItemPriceSnapshotDTO
                                                                                      (
                                                                                      pricingRule=OrderItemPricingRuleDTO(
                                                                                          price="25.00"))))
        software_owner_line = OrderLineDTO(itemId="", itemOrderQuantity="1",
                                           itemPriceSnapshot=OrderItemPriceSnapshotDTO
                                           (pricingRule=OrderItemPricingRuleDTO(price="10.00")),
                                           purchaseOrder=software_owner_purchase
                                           )

        order_properties = OrderPropertiesDTO(
            communicationProfile="",
            invoiceMode="AUTOMATIC",
            invoiceTerm="NET -7",
            billingPeriod="1 Week",
            paymentProcessor="Cash",
            paymentMode="MANUAL",
            paymentTerm="NET 30",
            paymentTermAlignment="BILLING_DATE",
            fulfillmentMode="MANUAL",
            fulfillmentTerm="Immediately"
        )

        request_data = OrderCreateDTO(
            order=OrderDataDTO(accountId="", name="", id="",
                               billingStartDate="ORDER_START_DATE", orderStartDate="",
                               properties=order_properties,
                               lines=[land_owner_line, software_owner_line]))

        response = exsited_sdk.order.create_with_purchase(request_data=request_data)
        print(response)

    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


def test_order_create_with_contract():
    SDKConfig.PRINT_REQUEST_DATA = False
    SDKConfig.PRINT_RAW_RESPONSE = False

    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(request_token_dto=CommonData.get_request_token_dto())

    try:
        request_data = OrderCreateDTO(
            order=OrderDataDTO(
                # id="",
                accountId="1U5S3S",
                allowContract="True",
                contractProperties=ContractPropertiesDTO(
                    requireCustomerAcceptance="True",
                    requiresPaymentMethod="False",
                    initialContractTerm="1 Year",
                    renewAutomatically="False",
                    autoRenewalTerm="1 Week",
                    allowEarlyTermination="True",
                    earlyTerminationMinimumPeriod="1 Day",
                    applyEarlyTerminationCharge="False",
                    allowPostponement="True",
                    maximumDurationPerPostponement="1 Day",
                    maximumPostponementCount="1",
                    allowTrial="True",
                    startContractAfterTrialEnds="true",
                    trialPeriod="1 Day",
                    allowDowngrade="False",
                    periodBeforeDowngrade="1 Day",
                    allowUpgrade="False",
                    terminationNoticePeriod="1 week"
                ),
                lines=[
                    OrderLineDTO(
                        itemId="ITEM-0009",
                        packageName="Pack-1",
                        itemOrderQuantity="1",
                        itemPriceSnapshot=OrderItemPriceSnapshotDTO(
                            pricingRule=OrderItemPricingRuleDTO(price="10.00")
                        )
                    )
                ]
            )
        )

        response = exsited_sdk.order.create_with_contract(request_data=request_data)
        print(response)

    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


def test_order_reactivate():
    SDKConfig.PRINT_REQUEST_DATA = False
    SDKConfig.PRINT_RAW_RESPONSE = False

    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(request_token_dto=CommonData.get_request_token_dto())

    try:
        response = exsited_sdk.order.reactivate(id="", effective_date="")
        print(response)

    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


def test_order_preorder():
    SDKConfig.PRINT_REQUEST_DATA = False
    SDKConfig.PRINT_RAW_RESPONSE = False

    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(request_token_dto=CommonData.get_request_token_dto())

    try:
        request_data = OrderCreateDTO(
            order=OrderDataDTO(accountId="", preOrder="true", priceTaxInclusive="true").
            add_line(item_id="", quantity="1"))
        response = exsited_sdk.order.preorder(request_data=request_data)
        print(response)

    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


def test_order_delete():
    SDKConfig.PRINT_REQUEST_DATA = False
    SDKConfig.PRINT_RAW_RESPONSE = False

    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(request_token_dto=CommonData.get_request_token_dto())

    try:
        response = exsited_sdk.order.delete(id="")
        print(response)

    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


def test_order_get_information():
    SDKConfig.PRINT_REQUEST_DATA = False
    SDKConfig.PRINT_RAW_RESPONSE = False

    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(request_token_dto=CommonData.get_request_token_dto())

    try:
        response = exsited_sdk.order.information(id="")
        print(response)

    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


def test_order_get_billing_preferences():
    SDKConfig.PRINT_REQUEST_DATA = False
    SDKConfig.PRINT_RAW_RESPONSE = False

    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(request_token_dto=CommonData.get_request_token_dto())

    try:
        response = exsited_sdk.order.billing_preferences(id="")
        print(response)

    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


def test_order_get_lines():
    SDKConfig.PRINT_REQUEST_DATA = False
    SDKConfig.PRINT_RAW_RESPONSE = False

    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(request_token_dto=CommonData.get_request_token_dto())

    try:
        response = exsited_sdk.order.lines(id="")
        print(response)

    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


def test_get_order_by_account():
    SDKConfig.PRINT_REQUEST_DATA = False
    SDKConfig.PRINT_RAW_RESPONSE = False

    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(request_token_dto=CommonData.get_request_token_dto())

    try:
        response = exsited_sdk.order.account_list(id="", limit=1)
        print(response)

    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


def test_get_order_lines_by_charge_uuid():
    SDKConfig.PRINT_REQUEST_DATA = False
    SDKConfig.PRINT_RAW_RESPONSE = False

    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(request_token_dto=CommonData.get_request_token_dto())

    try:
        response = exsited_sdk.order.lines_charge(id="", charge_uuid="")
        print(response)

    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


def test_order_update_information():
    SDKConfig.PRINT_REQUEST_DATA = False
    SDKConfig.PRINT_RAW_RESPONSE = False

    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(request_token_dto=CommonData.get_request_token_dto())

    try:
        communication_preference_one = [CommunicationPreferenceDTO(media="EMAIL", isEnabled=True)]
        request_data = OrderCreateDTO(
            order=OrderDataDTO(
                name="",
                displayName="",
                description="",
                manager="Administrator",
                communicationPreference=communication_preference_one
            )
        )

        response = exsited_sdk.order.update_information(id="", request_data=request_data)
        print(response)

    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


def test_update_order_line_information():
    SDKConfig.PRINT_REQUEST_DATA = False
    SDKConfig.PRINT_RAW_RESPONSE = False

    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(request_token_dto=CommonData.get_request_token_dto())

    try:
        line_data = OrderLineDTO(itemName="", itemInvoiceNote="", itemDescription="")
        request_data = OrderCreateDTO(order=OrderDataDTO(line=line_data))
        response = exsited_sdk.order.update_line_information(id="", uuid="", request_data=request_data)
        print(response)

    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


def test_update_order_billing_preference():
    SDKConfig.PRINT_REQUEST_DATA = False
    SDKConfig.PRINT_RAW_RESPONSE = False

    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(request_token_dto=CommonData.get_request_token_dto())

    try:
        order_properties = OrderPropertiesDTO(
            communicationProfile="AutoBill Communication Profile",
            invoiceMode="AUTOMATIC",
            invoiceTerm="Billing Start DATE",
            billingPeriod="1 Month",
            paymentProcessor="Bank Deposit",
            paymentMode="MANUAL",
            paymentTerm="Net 15",
            paymentTermAlignment="BILLING_DATE",
            fulfillmentMode="MANUAL",
            fulfillmentTerm="IMMEDIATELY"
        )
        request_data = OrderCreateDTO(order=OrderDataDTO(properties=order_properties))
        response = exsited_sdk.order.update_billing_preference(id="", request_data=request_data)
        print(response)

    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


def test_order_relinquish():
    SDKConfig.PRINT_REQUEST_DATA = False
    SDKConfig.PRINT_RAW_RESPONSE = False

    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(request_token_dto=CommonData.get_request_token_dto())

    try:
        request_data = OrderCreateDTO(
            order=OrderDataDTO(effectiveDate="")
        )
        response = exsited_sdk.order.relinquish(id="", request_data=request_data)
        print(response)

    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)

test_order_create_with_contract()