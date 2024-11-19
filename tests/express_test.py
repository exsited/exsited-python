from exsited.exsited.common.dto.common_dto import TaxDTO
from exsited.exsited.express.dto.express_dto import ItemPriceSnapshotDTO, PricingRuleDTO, ItemPriceTaxDTO, PaymentDTO, \
    PaymentAppliedDTO, InvoiceDTO, OrderDTO, AccountDTO, ExpressDTO
from exsited.exsited.exsited_sdk import ExsitedSDK
from exsited.common.sdk_conf import SDKConfig
from tests.common.common_data import CommonData
from exsited.exsited.order.dto.order_nested_dto import OrderPropertiesDTO, OrderLineDTO, ContractPropertiesDTO, \
    OrderItemPriceSnapshotDTO, OrderItemPricingRuleDTO


def test_express_order():
    SDKConfig.PRINT_REQUEST_DATA = True
    SDKConfig.PRINT_RAW_RESPONSE = False

    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(request_token_dto=CommonData.get_request_token_dto())

    try:
        order_line = OrderLineDTO(
            itemId="",
            itemOrderQuantity="",
            itemPriceSnapshot=OrderItemPriceSnapshotDTO(
                pricingRule=OrderItemPricingRuleDTO(price="")
            ),
            itemPriceTax=TaxDTO(
                uuid="",
                code="",
                rate=""
            ),
            packageName="",
            itemName="",
            quantity="",
            accountingCode=""
        )

        payment_applied = PaymentAppliedDTO(
            processor="",
            amount=""
        )

        payment = PaymentDTO(
            paymentApplied=[payment_applied]
        )

        invoice = InvoiceDTO(
            payment=payment
        )

        contract_properties = ContractPropertiesDTO(
            requireCustomerAcceptance="",
            requiresPaymentMethod="",
            initialContractTerm="",
            renewAutomatically="",
            autoRenewalTerm="",
            allowEarlyTermination="",
            applyEarlyTerminationCharge="",
            allowPostponement="",
            maximumDurationPerPostponement="",
            maximumPostponementCount="",
            allowTrial="",
            startContractAfterTrialEnds="",
            trialPeriod="",
            allowDowngrade="",
            periodBeforeDowngrade="",
            allowDowngradeCharge="",
            downgradeChargeType="",
            downgradeChargeFixed="",
            allowUpgrade=""
        )

        # Create the order data
        order = OrderDTO(
            lines=[order_line],
            invoice=invoice,
            allowContract="",
            contractProperties=contract_properties,
            properties=OrderPropertiesDTO(billingPeriod="")

        )

        account = AccountDTO(
            id="",
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
