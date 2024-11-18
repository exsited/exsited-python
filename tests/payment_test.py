from ab_py.exsited.exsited_sdk import ExsitedSDK
from ab_py.common.ab_exception import ABException
from ab_py.common.sdk_conf import SDKConfig
from tests.common.common_data import CommonData
from ab_py.exsited.payment.dto.payment_dto import PaymentCreateDTO, PaymentDataDTO, PaymentAppliedDTO, \
    CardDirectDebitPaymentAppliedDTO, CardDirectDebitPaymentDataDTO, CardDirectDebitPaymentCreateDTO
from ab_py.exsited.payment.dto.payment_dto import CardPaymentCreateDTO, CardPaymentDataDTO, CardPaymentAppliedDTO


def test_payment_details_against_invoice():
    SDKConfig.PRINT_REQUEST_DATA = False
    SDKConfig.PRINT_RAW_RESPONSE = False

    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(request_token_dto=CommonData.get_request_token_dto())

    try:
        response = exsited_sdk.payment.details(id='INV-0YH0A1-0010')
        print(response)
        return response
        # ResponseToObj().process(response=response["accounts"][0])
    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)

def test_payment_create_basic():
    SDKConfig.PRINT_REQUEST_DATA = True
    SDKConfig.PRINT_RAW_RESPONSE = False
    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(request_token_dto=CommonData.get_request_token_dto())
    try:
        payment_applied = PaymentAppliedDTO(processor="Cash", amount="20.00", reference="abc")
        payment_data = PaymentDataDTO(date="2024-11-12", paymentApplied=[payment_applied], note="fghgfh")
        request_data = PaymentCreateDTO(payment=payment_data)
        response = exsited_sdk.payment.create(invoice_id="INV-4LXPH3-1550", request_data=request_data)
        print(response)
    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)

def test_payment_create_card():
    SDKConfig.PRINT_REQUEST_DATA = True
    SDKConfig.PRINT_RAW_RESPONSE = False
    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(request_token_dto=CommonData.get_request_token_dto())
    try:
        card_payment_applied = CardPaymentAppliedDTO(
            processor="Stripe card",
            amount="1.00",
            cardType="Visa",
            token="tok_1PpLKAKfTp0ACfgNyrGN0fFL",
            cardNumber="XXXXXXXXXXXX4242",
            expiryMonth="12",
            expiryYear="2025",
            additionalFields={"host_ip": "192.168.116.34"}
        )
        card_payment_data = CardPaymentDataDTO(date="2024-08-19", paymentApplied=[card_payment_applied], note="fghgfh")
        request_data = CardPaymentCreateDTO(payment=card_payment_data)
        response = exsited_sdk.payment.create_card(invoice_id="INV-JQY12I-0051", request_data=request_data)
        print(response)
    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)

def test_payment_create_direct_debit():
    SDKConfig.PRINT_REQUEST_DATA = True
    SDKConfig.PRINT_RAW_RESPONSE = False
    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(request_token_dto=CommonData.get_request_token_dto())
    try:
        card_direct_debit_applied = CardDirectDebitPaymentAppliedDTO(
            processor="Stripe Direct Debit",
            amount="1",
            reference="514a10db-f731-4fd0-b4d7-569ffe1fbfa7",
        )
        card_direct_debit_data = CardDirectDebitPaymentDataDTO(
            date="2024-03-30",
            paymentApplied=[card_direct_debit_applied]
        )
        request_data = CardDirectDebitPaymentCreateDTO(payment=card_direct_debit_data)
        response = exsited_sdk.payment.create_direct_debit(invoice_id="INV-9RN3OC-0011",
                                                           request_data=request_data)
        print(response)
    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


# Call the test function
#test_payment_create_card()
test_payment_create_basic()
#test_payment_create_direct_debit()
# test_payment_details_against_invoice()
