from exsited.exsited.exsited_sdk import ExsitedSDK
from exsited.common.ab_exception import ABException
from exsited.common.sdk_conf import SDKConfig
from tests.common.common_data import CommonData
from exsited.exsited.payment.dto.payment_dto import PaymentCreateDTO, PaymentDataDTO, PaymentAppliedDTO, \
    CardDirectDebitPaymentAppliedDTO, CardDirectDebitPaymentDataDTO, CardDirectDebitPaymentCreateDTO
from exsited.exsited.payment.dto.payment_dto import CardPaymentCreateDTO, CardPaymentDataDTO, CardPaymentAppliedDTO


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
        payment_applied = PaymentAppliedDTO(processor="", amount="", reference="")
        payment_data = PaymentDataDTO(date="", paymentApplied=[payment_applied], note="")
        request_data = PaymentCreateDTO(payment=payment_data)
        response = exsited_sdk.payment.create(invoice_id="", request_data=request_data)
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
            processor="",
            amount="",
            cardType="",
            token="",
            cardNumber="",
            expiryMonth="",
            expiryYear="",
            additionalFields={"host_ip": ""}
        )
        card_payment_data = CardPaymentDataDTO(date="", paymentApplied=[card_payment_applied], note="")
        request_data = CardPaymentCreateDTO(payment=card_payment_data)
        response = exsited_sdk.payment.create_card(invoice_id="", request_data=request_data)
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
            processor="",
            amount="",
            reference="",
        )
        card_direct_debit_data = CardDirectDebitPaymentDataDTO(
            date="",
            paymentApplied=[card_direct_debit_applied]
        )
        request_data = CardDirectDebitPaymentCreateDTO(payment=card_direct_debit_data)
        response = exsited_sdk.payment.create_direct_debit(invoice_id="",
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
