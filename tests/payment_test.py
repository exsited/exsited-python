from exsited.http.file_token_manager import FileTokenManager

from exsited.exsited.exsited_sdk import ExsitedSDK
from exsited.common.ab_exception import ABException
from exsited.common.sdk_conf import SDKConfig
from tests.common.common_data import CommonData
from exsited.exsited.payment.dto.payment_dto import PaymentCreateDTO, PaymentDataDTO, PaymentAppliedDTO, \
    CardDirectDebitPaymentAppliedDTO, CardDirectDebitPaymentDataDTO, CardDirectDebitPaymentCreateDTO, \
    PaymentMultipleRequestDTO, PaymentMultipleDataDTO, InvoiceMultipleDTO, PaymentAppliedMultipleDTO, \
    AdditionalFieldsDTO, CreditAppliedDTO, GiftCertificateDTO, CustomAttributeDTO
from exsited.exsited.payment.dto.payment_dto import CardPaymentCreateDTO, CardPaymentDataDTO, CardPaymentAppliedDTO


def test_payment_details_against_invoice():
    SDKConfig.PRINT_REQUEST_DATA = False
    SDKConfig.PRINT_RAW_RESPONSE = False

    token_file_path = "shared_token.json"
    file_token_mgr = FileTokenManager(token_file_path)

    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(
        request_token_dto=CommonData.get_request_token_dto(),
        file_token_mgr=file_token_mgr
    )

    try:
        response = exsited_sdk.payment.invoice_details(id='')
        print(response)
        return response

    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)

def test_payment_list_basic():
    SDKConfig.PRINT_REQUEST_DATA = False
    SDKConfig.PRINT_RAW_RESPONSE = False

    token_file_path = "shared_token.json"
    file_token_mgr = FileTokenManager(token_file_path)

    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(
        request_token_dto=CommonData.get_request_token_dto(),
        file_token_mgr=file_token_mgr
    )

    try:
        response = exsited_sdk.payment.list()
        print(response)

    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)

def test_payment_details():
    SDKConfig.PRINT_REQUEST_DATA = False
    SDKConfig.PRINT_RAW_RESPONSE = False

    token_file_path = "shared_token.json"
    file_token_mgr = FileTokenManager(token_file_path)

    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(
        request_token_dto=CommonData.get_request_token_dto(),
        file_token_mgr=file_token_mgr
    )

    try:
        response = exsited_sdk.payment.details(id='')
        print(response)
        return response

    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


def test_payment_account_details():
    SDKConfig.PRINT_REQUEST_DATA = False
    SDKConfig.PRINT_RAW_RESPONSE = False

    token_file_path = "shared_token.json"
    file_token_mgr = FileTokenManager(token_file_path)

    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(
        request_token_dto=CommonData.get_request_token_dto(),
        file_token_mgr=file_token_mgr
    )

    try:
        response = exsited_sdk.payment.account_details(id='')
        print(response)
        return response

    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


def test_payment_order_details():
    SDKConfig.PRINT_REQUEST_DATA = False
    SDKConfig.PRINT_RAW_RESPONSE = False

    token_file_path = "shared_token.json"
    file_token_mgr = FileTokenManager(token_file_path)

    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(
        request_token_dto=CommonData.get_request_token_dto(),
        file_token_mgr=file_token_mgr
    )

    try:
        response = exsited_sdk.payment.order_details(id='')
        print(response)
        return response

    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)

def test_payment_create_basic():
    SDKConfig.PRINT_REQUEST_DATA = False
    SDKConfig.PRINT_RAW_RESPONSE = False

    token_file_path = "shared_token.json"
    file_token_mgr = FileTokenManager(token_file_path)

    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(
        request_token_dto=CommonData.get_request_token_dto(),
        file_token_mgr=file_token_mgr
    )

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


def test_payment_delete():
    SDKConfig.PRINT_REQUEST_DATA = False
    SDKConfig.PRINT_RAW_RESPONSE = False

    token_file_path = "shared_token.json"
    file_token_mgr = FileTokenManager(token_file_path)

    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(
        request_token_dto=CommonData.get_request_token_dto(),
        file_token_mgr=file_token_mgr
    )

    try:
        response = exsited_sdk.payment.delete(id="")
        print(response)

    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)
