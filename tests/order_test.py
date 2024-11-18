from ab_py.exsited.account.dto.account_nested_dto import CommunicationPreferenceDTO
from ab_py.exsited.common.dto.common_dto import TaxDTO
from ab_py.exsited.exsited_sdk import ExsitedSDK
from ab_py.exsited.order.dto.order_dto import OrderCreateDTO, OrderDataDTO
from ab_py.exsited.order.dto.usage_dto import UsageCreateDTO, UsageDataDTO
from ab_py.common.ab_exception import ABException
from ab_py.common.sdk_conf import SDKConfig
from order_usage_db.save_to_db import SaveToDB
from tests.common.common_data import CommonData
from ab_py.exsited.order.dto.order_nested_dto import OrderPropertiesDTO, OrderPurchaseDTO, POInformationDTO, \
    OrderItemPriceSnapshotDTO, OrderItemPricingRuleDTO, OrderLineDTO, ContractPropertiesDTO, OrderUpgradeDTO, \
    OrderItemPriceTaxDTO, OrderItemAccountingCodeDTO
from ab_py.exsited.order.dto.order_nested_dto import OrderPropertiesDTO, OrderPurchaseDTO, POInformationDTO, \
    OrderItemPriceSnapshotDTO, OrderItemPricingRuleDTO, OrderLineDTO, ContractPropertiesDTO


def test_order_create_basic():
    SDKConfig.PRINT_REQUEST_DATA = True
    SDKConfig.PRINT_RAW_RESPONSE = False

    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(request_token_dto=CommonData.get_request_token_dto())

    try:
        request_data = OrderCreateDTO(
            order=OrderDataDTO(accountId="").add_line(item_id="", quantity=""))
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
            accountId="",
            id="",
            properties=order_properties
        )
        order_data.add_line(item_id="", quantity="", price=000)
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


def test_order_details(id: str):
    SDKConfig.PRINT_REQUEST_DATA = False
    SDKConfig.PRINT_RAW_RESPONSE = False

    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(request_token_dto=CommonData.get_request_token_dto())

    try:
        response = exsited_sdk.order.details(id=id)
        print(response)
        return response
        # ResponseToObj().process(response=response["accounts"][0])
    except ABException as ab:
        # print(ab)
        # print(ab.get_errors())
        # print(ab.raw_response)
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
        # ResponseToObj().process(response=response["accounts"][0])
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
        # ResponseToObj().process(response=response["accounts"][0])
    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


def test_order_cancel():
    SDKConfig.PRINT_REQUEST_DATA = True
    SDKConfig.PRINT_RAW_RESPONSE = False

    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(request_token_dto=CommonData.get_request_token_dto())

    try:
        response = exsited_sdk.order.cancel(id="", effective_date="")
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
            usage=UsageDataDTO(chargeItemUuid="",
                               chargingPeriod="",
                               quantity="",
                               startTime="",
                               endTime="",
                               type="",
                               )
        )
        response = exsited_sdk.order.add_usage(request_data=request_data)
    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


def test_order_usage_modify():
    SDKConfig.PRINT_REQUEST_DATA = False
    SDKConfig.PRINT_RAW_RESPONSE = False

    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(request_token_dto=CommonData.get_request_token_dto())


    request_data = UsageCreateDTO(usage=UsageDataDTO( quantity="",startTime="",endTime=""))

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


    request_data = UsageCreateDTO(usage=UsageDataDTO( quantity="",startTime="",endTime=""))

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
        # ResponseToObj().process(response=response["accounts"][0])
    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


def test_order_create_with_purchase_order():
    SDKConfig.PRINT_REQUEST_DATA = True
    SDKConfig.PRINT_RAW_RESPONSE = False

    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(request_token_dto=CommonData.get_request_token_dto())

    try:

        land_owner_purchase = OrderPurchaseDTO(createPo="true",
                                               poInformation=POInformationDTO(id="", accountId="",
                                                                              currency="", itemQuantity="",
                                                                              itemPriceSnapshot=OrderItemPriceSnapshotDTO
                                                                                  (pricingRule=OrderItemPricingRuleDTO(
                                                                                  price=""))))
        land_owner_line = OrderLineDTO(itemId="", itemOrderQuantity="",
                                       itemPriceSnapshot=OrderItemPriceSnapshotDTO
                                       (pricingRule=OrderItemPricingRuleDTO(price="")),
                                       purchaseOrder=land_owner_purchase
                                       )

        software_owner_purchase = OrderPurchaseDTO(createPo="true",
                                                   poInformation=POInformationDTO(id="", accountId="",
                                                                                  currency="",
                                                                                  itemQuantity="",
                                                                                  itemPriceSnapshot=OrderItemPriceSnapshotDTO
                                                                                      (
                                                                                      pricingRule=OrderItemPricingRuleDTO(
                                                                                          price=""))))
        software_owner_line = OrderLineDTO(itemId="", itemOrderQuantity="1",
                                           itemPriceSnapshot=OrderItemPriceSnapshotDTO
                                           (pricingRule=OrderItemPricingRuleDTO(price="")),
                                           purchaseOrder=software_owner_purchase
                                           )

        order_properties = OrderPropertiesDTO(
            communicationProfile="",
            invoiceMode="",
            invoiceTerm="",
            billingPeriod="",
            paymentProcessor="",
            paymentMode="",
            paymentTerm="",
            paymentTermAlignment="",
            fulfillmentMode="",
            fulfillmentTerm=""
        )

        request_data = OrderCreateDTO(
            order=OrderDataDTO(accountId="", name="", id="",
                               billingStartDate="", orderStartDate="",
                               properties=order_properties,
                               lines=[land_owner_line, software_owner_line]))

        response = exsited_sdk.order.create_with_purchase(request_data=request_data)
        print(response)
        # ResponseToObj().process(response=response)

    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


def test_order_create_with_contract():
    SDKConfig.PRINT_REQUEST_DATA = True
    SDKConfig.PRINT_RAW_RESPONSE = False

    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(request_token_dto=CommonData.get_request_token_dto())

    try:

        request_data = OrderCreateDTO(
            order=OrderDataDTO(
                id="",
                accountId="",
                allowContract="",
                contractProperties=ContractPropertiesDTO(
                    requireCustomerAcceptance="",
                    requiresPaymentMethod="",
                    initialContractTerm="1 ",
                    renewAutomatically="",
                    autoRenewalTerm="",
                    allowEarlyTermination="",
                    earlyTerminationMinimumPeriod="",
                    applyEarlyTerminationCharge="",
                    allowPostponement="",
                    maximumDurationPerPostponement="",
                    maximumPostponementCount="",
                    allowTrial="",
                    startContractAfterTrialEnds="",
                    trialPeriod="",
                    allowDowngrade="",
                    periodBeforeDowngrade="",
                    allowUpgrade="",
                    terminationNoticePeriod=""
                ),
                lines=[
                    OrderLineDTO(
                        itemId="",
                        packageName="",
                        itemOrderQuantity="",
                        itemPriceSnapshot=OrderItemPriceSnapshotDTO(
                            pricingRule=OrderItemPricingRuleDTO(price="")
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


def test_order_family_upgrade():
    SDKConfig.PRINT_REQUEST_DATA = True
    SDKConfig.PRINT_RAW_RESPONSE = False

    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(request_token_dto=CommonData.get_request_token_dto())

    try:
        order_line = OrderLineDTO(
            itemId="",
            itemName="",
            chargeItemUuid="",
            packageName="",
            quantity="",
            itemPriceSnapshot=OrderItemPriceSnapshotDTO(
                pricingRule=OrderItemPricingRuleDTO(price="")
            ),
            discount="",
            shippingCost="",
            uom="",
            warehouse="",
            isTaxExemptWhenSold="",
            itemPriceTax=TaxDTO(
                uuid="",
                code="",
                rate=""
            ),
            accountingCode=" ",
            itemInvoiceNote="",
            itemDescription="",
            itemCustomAttributes=[
                {"name": "cus_attr_number", "value": ""},
                {"name": "cus_attr_string", "value": ""}
            ]
        )

        request_data = OrderUpgradeDTO(
            effectiveDate="",
            lines=[order_line]
        )

        response = exsited_sdk.order.upgrade(order_id="", request_data=request_data)

        print(response)

    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


def test_order_family_downgrade():
    SDKConfig.PRINT_REQUEST_DATA = True
    SDKConfig.PRINT_RAW_RESPONSE = False

    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(request_token_dto=CommonData.get_request_token_dto())

    try:
        order_line = OrderLineDTO(
            itemId="",
            itemName="",
            chargeItemUuid="",
            packageName="",
            quantity="",
            itemPriceSnapshot=OrderItemPriceSnapshotDTO(
                pricingRule=OrderItemPricingRuleDTO(price="")
            ),
            discount="",
            shippingCost="",
            uom="",
            warehouse="",
            isTaxExemptWhenSold="",
            itemPriceTax=TaxDTO(
                uuid="",
                code="",
                rate=""
            ),
            accountingCode=" ",
            itemInvoiceNote="",
            itemDescription="",
            itemCustomAttributes=[
                {"name": "cus_attr_number", "value": ""},
                {"name": "cus_attr_string", "value": ""}
            ]
        )

        request_data = OrderUpgradeDTO(
            effectiveDate="",
            lines=[order_line]
        )

        response = exsited_sdk.order.downgrade(order_id="", request_data=request_data)

        print(response)

    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


def test_order_family_upgrade_preview():
    SDKConfig.PRINT_REQUEST_DATA = True
    SDKConfig.PRINT_RAW_RESPONSE = False

    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(request_token_dto=CommonData.get_request_token_dto())

    try:
        order_line = OrderLineDTO(
            itemId="",
            itemName="",
            chargeItemUuid="",
            packageName="",
            quantity="",
            itemPriceSnapshot=OrderItemPriceSnapshotDTO(
                pricingRule=OrderItemPricingRuleDTO(price="")
            ),
            discount="",
            shippingCost="",
            uom="",
            warehouse="",
            isTaxExemptWhenSold="",
            itemPriceTax=TaxDTO(
                uuid="",
                code="",
                rate=""
            ),
            accountingCode="",
            itemInvoiceNote="",
            itemDescription="",
            itemCustomAttributes=[
                {"name": "cus_attr_number", "value": ""},
                {"name": "cus_attr_string", "value": ""}
            ]
        )

        request_data = OrderUpgradeDTO(
            effectiveDate="",
            lines=[order_line]
        )

        response = exsited_sdk.order.upgrade_preview(order_id="", request_data=request_data)

        print(response)

    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


def test_order_family_downgrade_preview():
    SDKConfig.PRINT_REQUEST_DATA = True
    SDKConfig.PRINT_RAW_RESPONSE = False

    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(request_token_dto=CommonData.get_request_token_dto())

    try:
        order_line = OrderLineDTO(
            itemId="",
            itemName="",
            chargeItemUuid="",
            packageName="",
            quantity="",
            itemPriceSnapshot=OrderItemPriceSnapshotDTO(
                pricingRule=OrderItemPricingRuleDTO(price="")
            ),
            discount="",
            shippingCost="",
            uom="",
            warehouse="",
            isTaxExemptWhenSold="",
            itemPriceTax=TaxDTO(
                uuid="",
                code="",
                rate=""
            ),
            accountingCode="",
            itemInvoiceNote="",
            itemDescription="",
            itemCustomAttributes=[
                {"name": "cus_attr_number", "value": ""},
                {"name": "cus_attr_string", "value": ""}
            ]
        )

        request_data = OrderUpgradeDTO(
            effectiveDate="",
            lines=[order_line]
        )

        response = exsited_sdk.order.downgrade_preview(order_id="", request_data=request_data)

        print(response)

    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


def test_order_reactivate():
    SDKConfig.PRINT_REQUEST_DATA = True
    SDKConfig.PRINT_RAW_RESPONSE = False

    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(request_token_dto=CommonData.get_request_token_dto())

    try:
        response = exsited_sdk.order.reactivate(id="", effective_date="")
        print(response)
        # ResponseToObj().process(response=response["accounts"][0])
    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


def test_order_preorder():
    SDKConfig.PRINT_REQUEST_DATA = True
    SDKConfig.PRINT_RAW_RESPONSE = False

    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(request_token_dto=CommonData.get_request_token_dto())

    try:
        request_data = OrderCreateDTO(
            order=OrderDataDTO(accountId="", preOrder="", priceTaxInclusive="").
            add_line(item_id="", quantity=""))
        response = exsited_sdk.order.preorder(request_data=request_data)
        print(response)

    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


def test_order_change():
    SDKConfig.PRINT_REQUEST_DATA = True
    SDKConfig.PRINT_RAW_RESPONSE = False

    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(request_token_dto=CommonData.get_request_token_dto())

    try:
        line = OrderLineDTO(op="", uuid="", itemOrderQuantity="",
                            itemPriceSnapshot=OrderItemPriceSnapshotDTO(
                                pricingRule=OrderItemPricingRuleDTO(price="")))

        request_data = OrderCreateDTO(order=OrderDataDTO(effectiveDate="", lines=[line]))

        response = exsited_sdk.order.change(id="", request_data=request_data)
        print(response)

    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


def test_order_delete():
    SDKConfig.PRINT_REQUEST_DATA = True
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
    SDKConfig.PRINT_REQUEST_DATA = True
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
    SDKConfig.PRINT_REQUEST_DATA = True
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
    SDKConfig.PRINT_REQUEST_DATA = True
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
    SDKConfig.PRINT_REQUEST_DATA = True
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
    SDKConfig.PRINT_REQUEST_DATA = True
    SDKConfig.PRINT_RAW_RESPONSE = False

    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(request_token_dto=CommonData.get_request_token_dto())

    try:
        response = exsited_sdk.order.lines_charge(id="",
                                                  charge_uuid="")
        print(response)

    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


def test_order_update_information():
    SDKConfig.PRINT_REQUEST_DATA = True
    SDKConfig.PRINT_RAW_RESPONSE = False

    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(request_token_dto=CommonData.get_request_token_dto())

    try:
        communication_preference_one = CommunicationPreferenceDTO(media="EMAIL", isEnabled=True)
        request_data = OrderCreateDTO(
            order=OrderDataDTO(
                name="",
                displayName="",
                description="",
                manager="",

            )
        )

        response = exsited_sdk.order.update_information(id="", request_data=request_data)
        print(response)

    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


def test_update_order_line_information():
    SDKConfig.PRINT_REQUEST_DATA = True
    SDKConfig.PRINT_RAW_RESPONSE = False

    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(request_token_dto=CommonData.get_request_token_dto())

    try:
        line_data = OrderLineDTO(itemName="", itemInvoiceNote="", itemDescription="")
        request_data = OrderCreateDTO(order=OrderDataDTO(line=line_data))
        response = exsited_sdk.order.update_line_information(id="",
                                                             uuid="",
                                                             request_data=request_data)
        print(response)

    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


def test_update_order_billing_preference():
    SDKConfig.PRINT_REQUEST_DATA = True
    SDKConfig.PRINT_RAW_RESPONSE = False

    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(request_token_dto=CommonData.get_request_token_dto())

    try:
        order_properties = OrderPropertiesDTO(
            communicationProfile="",
            invoiceMode="",
            invoiceTerm="",
            billingPeriod="",
            paymentProcessor="",
            paymentMode="",
            paymentTerm="",
            paymentTermAlignment="",
            fulfillmentMode="",
            fulfillmentTerm=""
        )
        request_data = OrderCreateDTO(order=OrderDataDTO(properties=order_properties))
        response = exsited_sdk.order.update_billing_preference(id="",
                                                               request_data=request_data)
        print(response)

    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


def test_order_relinquish():
    SDKConfig.PRINT_REQUEST_DATA = True
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


# test_order_create_with_property()
# test_order_create_basic()
# test_order_details()
test_order_cancel()
# test_order_create_with_purchase_order()
# test_order_create_with_contract()
# test_order_reactivate()
# test_order_get_information()
# test_order_get_billing_preferences()
# test_order_get_lines()
# test_get_order_by_account()
# test_get_order_lines_by_charge_uuid()
test_get_order_lines_by_charge_uuid()
test_order_preorder()
# test_order_preorder()
# test_order_preorder()
# test_order_change()
# test_order_family_downgrade_preview()
# test_order_family_upgrade_preview()
# test_order_family_upgrade()
# test_order_family_downgrade()
# test_order_delete()
# test_update_order_line_information()
test_order_relinquish()
# test_order_create_with_contract()
# test_order_usage_list()
# test_order_usages_details()
# test_order_usage_modify()
# test_order_usage_update()
# test_order_usages_delete()

# test_order_delete()
# test_update_order_line_information()
test_order_relinquish()