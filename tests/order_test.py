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
            order=OrderDataDTO(accountId="QP38FA").add_line(item_id="ITEM-0014", quantity="1"))
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
        response = exsited_sdk.order.usage_details(uuid='eebc7977-cc2d-4a41-ad6f-4184b9b2142c')
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
        response = exsited_sdk.order.usage_delete(uuid="2d0accb4-c35a-42a2-8a09-a819111afdd0")
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
        response = exsited_sdk.order.cancel(id="orderRenterSDKxyz1245", effective_date="2024-11-14")
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


def test_order_usage_modify():
    SDKConfig.PRINT_REQUEST_DATA = False
    SDKConfig.PRINT_RAW_RESPONSE = False

    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(request_token_dto=CommonData.get_request_token_dto())


    request_data = UsageCreateDTO(usage=UsageDataDTO( quantity="2",startTime="2024-11-01 00:00:00",endTime="2024-11-03 00:00:20"))

    try:
        response = exsited_sdk.order.usage_modify(uuid='2d0accb4-c35a-42a2-8a09-a819111afdd0', request_data=request_data)
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


    request_data = UsageCreateDTO(usage=UsageDataDTO( quantity="2",startTime="2024-11-01 00:00:00",endTime="2024-11-03 00:00:20"))

    try:
        response = exsited_sdk.order.usage_update(uuid='2d0accb4-c35a-42a2-8a09-a819111afdd0', request_data=request_data)
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
                                               poInformation=POInformationDTO(id="landxyz12", accountId="5P51SQ",
                                                                              currency="AUD", itemQuantity="1",
                                                                              itemPriceSnapshot=OrderItemPriceSnapshotDTO
                                                                                  (pricingRule=OrderItemPricingRuleDTO(
                                                                                  price="98.00"))))
        land_owner_line = OrderLineDTO(itemId="ITEM-0016", itemOrderQuantity="1",
                                       itemPriceSnapshot=OrderItemPriceSnapshotDTO
                                       (pricingRule=OrderItemPricingRuleDTO(price="100.00")),
                                       purchaseOrder=land_owner_purchase
                                       )

        software_owner_purchase = OrderPurchaseDTO(createPo="true",
                                                   poInformation=POInformationDTO(id="ownerxyz12", accountId="QJ2OWQ",
                                                                                  currency="AUD",
                                                                                  itemQuantity="1",
                                                                                  itemPriceSnapshot=OrderItemPriceSnapshotDTO
                                                                                      (
                                                                                      pricingRule=OrderItemPricingRuleDTO(
                                                                                          price="2.00"))))
        software_owner_line = OrderLineDTO(itemId="ITEM-0018", itemOrderQuantity="1",
                                           itemPriceSnapshot=OrderItemPriceSnapshotDTO
                                           (pricingRule=OrderItemPricingRuleDTO(price="0.00")),
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
            order=OrderDataDTO(accountId="WP06N4", name="renterSDKx", id="orderRenterSDKxyz12",
                               billingStartDate="ORDER_START_DATE", orderStartDate="2024-09-04",
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
                id="SDK_test-recheck002",
                accountId="1AF35J",
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
                        itemId="ITEM-0029",
                        packageName="weekly_Package",
                        itemOrderQuantity="1",
                        itemPriceSnapshot=OrderItemPriceSnapshotDTO(
                            pricingRule=OrderItemPricingRuleDTO(price="10.000000")
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
            itemId="addon_family",
            itemName="addon family",
            chargeItemUuid="670bbb32-2959-4ef1-a939-98d45293fdde",
            packageName="yearly package",
            quantity="10",
            itemPriceSnapshot=OrderItemPriceSnapshotDTO(
                pricingRule=OrderItemPricingRuleDTO(price="20.000000")
            ),
            discount="9.99",
            shippingCost="2.50",
            uom="kilogram",
            warehouse="warehouse1",
            isTaxExemptWhenSold="false",
            itemPriceTax=TaxDTO(
                uuid="d166b28c-395b-4692-87b9-7408a01b72c0",
                code="GST",
                rate="10.000000"
            ),
            accountingCode="Sales Revenue",
            itemInvoiceNote="this is an invoice note",
            itemDescription="One hot day, a thirsty crow flew all over the fields looking for water. For a long time, he could not find any.",
            itemCustomAttributes=[
                {"name": "cus_attr_number", "value": ""},
                {"name": "cus_attr_string", "value": ""}
            ]
        )

        request_data = OrderUpgradeDTO(
            effectiveDate="2024-10-22",
            lines=[order_line]
        )

        response = exsited_sdk.order.upgrade(order_id="ORD-76GOU2-1288", request_data=request_data)

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
            itemId="addon_family",
            itemName="addon family",
            chargeItemUuid="10d96d4c-3a1a-4539-9d37-ff7b45eae91a",
            packageName="monthly package",
            quantity="10",
            itemPriceSnapshot=OrderItemPriceSnapshotDTO(
                pricingRule=OrderItemPricingRuleDTO(price="20.000000")
            ),
            discount="9.99",
            shippingCost="2.50",
            uom="kilogram",
            warehouse="warehouse1",
            isTaxExemptWhenSold="false",
            itemPriceTax=TaxDTO(
                uuid="d166b28c-395b-4692-87b9-7408a01b72c0",
                code="GST",
                rate="10.000000"
            ),
            accountingCode="Sales Revenue",
            itemInvoiceNote="this is an invoice note",
            itemDescription="One hot day, a thirsty crow flew all over the fields looking for water. For a long time, he could not find any.",
            itemCustomAttributes=[
                {"name": "cus_attr_number", "value": ""},
                {"name": "cus_attr_string", "value": ""}
            ]
        )

        request_data = OrderUpgradeDTO(
            effectiveDate="2024-10-23",
            lines=[order_line]
        )

        response = exsited_sdk.order.downgrade(order_id="ORD-76GOU2-1289", request_data=request_data)

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
            itemId="addon_family",
            itemName="addon family",
            chargeItemUuid="9cf55a63-790b-4bb2-8335-09c77cb21d03",
            packageName="yearly package",
            quantity="10",
            itemPriceSnapshot=OrderItemPriceSnapshotDTO(
                pricingRule=OrderItemPricingRuleDTO(price="20.000000")
            ),
            discount="9.99",
            shippingCost="2.50",
            uom="kilogram",
            warehouse="warehouse1",
            isTaxExemptWhenSold="false",
            itemPriceTax=TaxDTO(
                uuid="d166b28c-395b-4692-87b9-7408a01b72c0",
                code="GST",
                rate="10.000000"
            ),
            accountingCode="Sales Revenue",
            itemInvoiceNote="this is an invoice note",
            itemDescription="One hot day, a thirsty crow flew all over the fields looking for water. For a long time, he could not find any.",
            itemCustomAttributes=[
                {"name": "cus_attr_number", "value": ""},
                {"name": "cus_attr_string", "value": ""}
            ]
        )

        request_data = OrderUpgradeDTO(
            effectiveDate="2024-10-23",
            lines=[order_line]
        )

        response = exsited_sdk.order.upgrade_preview(order_id="ORD-76GOU2-1304", request_data=request_data)

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
            itemId="addon_family",
            itemName="addon family",
            chargeItemUuid="ff3712d6-d4a5-48cc-a935-33388b064158",
            packageName="monthly package",
            quantity="10",
            itemPriceSnapshot=OrderItemPriceSnapshotDTO(
                pricingRule=OrderItemPricingRuleDTO(price="20.000000")
            ),
            discount="9.99",
            shippingCost="2.50",
            uom="kilogram",
            warehouse="warehouse1",
            isTaxExemptWhenSold="false",
            itemPriceTax=TaxDTO(
                uuid="d166b28c-395b-4692-87b9-7408a01b72c0",
                code="GST",
                rate="10.000000"
            ),
            accountingCode="Sales Revenue",
            itemInvoiceNote="this is an invoice note",
            itemDescription="One hot day, a thirsty crow flew all over the fields looking for water. For a long time, he could not find any.",
            itemCustomAttributes=[
                {"name": "cus_attr_number", "value": ""},
                {"name": "cus_attr_string", "value": ""}
            ]
        )

        request_data = OrderUpgradeDTO(
            effectiveDate="2024-10-24",
            lines=[order_line]
        )

        response = exsited_sdk.order.downgrade_preview(order_id="ORD-76GOU2-1307", request_data=request_data)

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
        response = exsited_sdk.order.reactivate(id="ORD-QP38FA-0115", effective_date="2024-10-21")
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
            order=OrderDataDTO(accountId="QP38FA", preOrder="true", priceTaxInclusive="true").
            add_line(item_id="ITEM-0080", quantity="1"))
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
        line = OrderLineDTO(op="change", uuid="20caa580-c6d4-465c-99f6-1db66f4a432e", itemOrderQuantity="4",
                            itemPriceSnapshot=OrderItemPriceSnapshotDTO(
                                pricingRule=OrderItemPricingRuleDTO(price="40.0000")))

        request_data = OrderCreateDTO(order=OrderDataDTO(effectiveDate="2024-10-23", lines=[line]))

        response = exsited_sdk.order.change(id="ORD-QP38FA-0123", request_data=request_data)
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
        response = exsited_sdk.order.delete(id="ORD-QP38FA-0125")
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
        response = exsited_sdk.order.information(id="ORD-QP38FA-0123")
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
        response = exsited_sdk.order.billing_preferences(id="ORD-QP38FA-0123")
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
        response = exsited_sdk.order.lines(id="ORD-WP06N4-0035")
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
        response = exsited_sdk.order.account_list(id="5CRBUQ", limit=1)
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
        response = exsited_sdk.order.lines_charge(id="ORD-WP06N4-0035",
                                                  charge_uuid="489161a6-c3f2-4605-b141-4a732f85777b")
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
                name="SDK",
                displayName="SDK",
                description="Updated from SDK",
                manager="Administrator",

            )
        )

        response = exsited_sdk.order.update_information(id="ORD-QP38FA-0130", request_data=request_data)
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
        line_data = OrderLineDTO(itemName="Updated From SDK", itemInvoiceNote="Note", itemDescription="description")
        request_data = OrderCreateDTO(order=OrderDataDTO(line=line_data))
        response = exsited_sdk.order.update_line_information(id="ORD-WP06N4-0035",
                                                             uuid="489161a6-c3f2-4605-b141-4a732f85777b",
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
        response = exsited_sdk.order.update_billing_preference(id="ORD-QP38FA-0130",
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
            order=OrderDataDTO(effectiveDate="2024-10-27")
        )
        response = exsited_sdk.order.relinquish(id="ORD-QP38FA-0132", request_data=request_data)
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