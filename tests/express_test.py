from ab_py.exsited.common.dto.common_dto import TaxDTO
from ab_py.exsited.express.dto.express_dto import ItemPriceSnapshotDTO, PricingRuleDTO, ItemPriceTaxDTO, PaymentDTO, \
    PaymentAppliedDTO, InvoiceDTO, OrderDTO, AccountDTO, ExpressDTO
from ab_py.exsited.exsited_sdk import ExsitedSDK
from ab_py.common.sdk_conf import SDKConfig
from tests.common.common_data import CommonData
from ab_py.exsited.order.dto.order_nested_dto import OrderPropertiesDTO, OrderLineDTO, ContractPropertiesDTO, \
    OrderItemPriceSnapshotDTO, OrderItemPricingRuleDTO


def test_express_order():
    SDKConfig.PRINT_REQUEST_DATA = True
    SDKConfig.PRINT_RAW_RESPONSE = False

    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(request_token_dto=CommonData.get_request_token_dto())

    try:
        order_line = OrderLineDTO(
            itemId="addon_family",
            itemOrderQuantity="1",
            itemPriceSnapshot=OrderItemPriceSnapshotDTO(
                pricingRule=OrderItemPricingRuleDTO(price="50.00")
            ),
            itemPriceTax=TaxDTO(
                uuid="5da85c94-2c63-409b-a2ab-41094582df26",
                code="FRE",
                rate="1"
            ),
            packageName="monthly package",
            itemName="addon family",
            quantity="1",
            accountingCode="Sales Revenue"
        )

        payment_applied = PaymentAppliedDTO(
            processor="Cash",
            amount="50"
        )

        payment = PaymentDTO(
            paymentApplied=[payment_applied]
        )

        invoice = InvoiceDTO(
            payment=payment
        )

        contract_properties = ContractPropertiesDTO(
            requireCustomerAcceptance="False",
            requiresPaymentMethod="False",
            initialContractTerm="1 Year",
            renewAutomatically="True",
            autoRenewalTerm="1 Week",
            allowEarlyTermination="True",
            applyEarlyTerminationCharge="False",
            allowPostponement="True",
            maximumDurationPerPostponement="1 Day",
            maximumPostponementCount="1",
            allowTrial="False",
            startContractAfterTrialEnds="True",
            trialPeriod="1 day",
            allowDowngrade="True",
            periodBeforeDowngrade="1 Day",
            allowDowngradeCharge="False",
            downgradeChargeType="Fixed",
            downgradeChargeFixed="1.000000",
            allowUpgrade="True"
        )

        # Create the order data
        order = OrderDTO(
            lines=[order_line],
            invoice=invoice,
            allowContract="True",
            contractProperties=contract_properties,
            properties=OrderPropertiesDTO(billingPeriod="1 Month")

        )

        account = AccountDTO(
            id="IE1DSN",
            order=order
        )

        request_data = ExpressDTO(
            account=account
        )

        response = exsited_sdk.express.create(request_data=request_data)

        print(response)

    except Exception as e:
        print(f"Error occurred: {e}")



test_express_order()
