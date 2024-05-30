from ab_py.autobill.account.dto.account_dto import AccountDataDTO, AccountCreateDTO, AccountUpdateInformationDTO, \
    PaymentMethodsAddDTO, PaymentCardMethodsAddDTO
from ab_py.autobill.account.dto.account_nested_dto import PaymentMethodsDataDTO, PaymentCardMethodsDataDTO
from ab_py.autobill.autobill_sdk import AutoBillSDK
from ab_py.common.ab_exception import ABException
from ab_py.common.sdk_conf import SDKConfig
from tests.common.common_data import CommonData


def test_account_create_basic():
    SDKConfig.PRINT_REQUEST_DATA = False
    SDKConfig.PRINT_RAW_RESPONSE = False

    autobill_sdk: AutoBillSDK = AutoBillSDK().init_sdk(request_token_dto=CommonData.get_request_token_dto())

    try:
        request_data = AccountCreateDTO(account=AccountDataDTO(name="Python SDK", emailAddress="a26@bfei.net"))
        response = autobill_sdk.account.create(request_data=request_data)
        # ResponseToObj().process(response=response)
    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


def test_account_update_info():
    SDKConfig.PRINT_REQUEST_DATA = False
    SDKConfig.PRINT_RAW_RESPONSE = False

    autobill_sdk: AutoBillSDK = AutoBillSDK().init_sdk(request_token_dto=CommonData.get_request_token_dto())

    try:
        request_data = AccountUpdateInformationDTO(account=AccountDataDTO(name="Update Done", emailAddress="a26@bfei.net", displayName="Display Name Update"))
        response = autobill_sdk.account.update_information(id="KZ558V", request_data=request_data)
        print(response)
    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


def test_account_list_basic():
    SDKConfig.PRINT_REQUEST_DATA = False
    SDKConfig.PRINT_RAW_RESPONSE = False

    autobill_sdk: AutoBillSDK = AutoBillSDK().init_sdk(request_token_dto=CommonData.get_request_token_dto())

    try:
        response = autobill_sdk.account.list()
        print(response)
        # ResponseToObj().process(response=response["accounts"][0])
    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


def test_account_details():
    SDKConfig.PRINT_REQUEST_DATA = False
    SDKConfig.PRINT_RAW_RESPONSE = False

    autobill_sdk: AutoBillSDK = AutoBillSDK().init_sdk(request_token_dto=CommonData.get_request_token_dto())

    try:
        response = autobill_sdk.account.details(id="I4I2DE")
        print(response)
        # ResponseToObj().process(response=response["accounts"][0])
    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


def test_account_delete():
    SDKConfig.PRINT_REQUEST_DATA = False
    SDKConfig.PRINT_RAW_RESPONSE = False

    autobill_sdk: AutoBillSDK = AutoBillSDK().init_sdk(request_token_dto=CommonData.get_request_token_dto())

    try:
        response = autobill_sdk.account.delete(id="KZ558V")
        print(response)
        # ResponseToObj().process(response=response["accounts"][0])
    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


def test_account_payment_methods_add():
    SDKConfig.PRINT_REQUEST_DATA = True
    SDKConfig.PRINT_RAW_RESPONSE = False

    autobill_sdk: AutoBillSDK = AutoBillSDK().init_sdk(request_token_dto=CommonData.get_request_token_dto())

    try:
        payment_method: PaymentMethodsDataDTO = PaymentMethodsDataDTO(
            processorType="OTHER",
            default="false",
            paymentProcessor="Cash",
            reference="check_processor1",
        )
        response = autobill_sdk.account.add_payment_method(account_id="KZ558V", request_data=PaymentMethodsAddDTO().method(payment_method=payment_method))
        print(response)
    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


def test_account_payment_card_methods_add():
    SDKConfig.PRINT_REQUEST_DATA = True
    SDKConfig.PRINT_RAW_RESPONSE = False

    autobill_sdk: AutoBillSDK = AutoBillSDK().init_sdk(request_token_dto=CommonData.get_request_token_dto())

    try:
        payment_method: PaymentCardMethodsDataDTO = PaymentCardMethodsDataDTO(
            processorType="DIRECT_CREDIT",
            default="false",
            paymentProcessor="eway",
            reference="eway_processor",
            cardType="Visa",
            token="2684331361852905",
            cardNumber="4111111111111111",
            expiryMonth="12",
            expiryYear="2024",
        )
        response = autobill_sdk.account.add_payment_card_method(account_id="KZ558V", request_data=PaymentCardMethodsAddDTO().method(payment_method=payment_method))
        print(response)
    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


def test_list_payment_methods():
    SDKConfig.PRINT_REQUEST_DATA = False
    SDKConfig.PRINT_RAW_RESPONSE = False

    autobill_sdk: AutoBillSDK = AutoBillSDK().init_sdk(request_token_dto=CommonData.get_request_token_dto())

    try:
        response = autobill_sdk.account.list_payment_method(account_id="KZ558V")
        print(response)
        # ResponseToObj().process(response=response["accounts"][0])
    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


def test_delete_payment_methods():
    SDKConfig.PRINT_REQUEST_DATA = False
    SDKConfig.PRINT_RAW_RESPONSE = False

    autobill_sdk: AutoBillSDK = AutoBillSDK().init_sdk(request_token_dto=CommonData.get_request_token_dto())

    try:
        response = autobill_sdk.account.delete_payment_method(account_id="KZ558V", reference="check_processor")
        print(response)
        # ResponseToObj().process(response=response["accounts"][0])
    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


def test_payment_method_details():
    SDKConfig.PRINT_REQUEST_DATA = False
    SDKConfig.PRINT_RAW_RESPONSE = False

    autobill_sdk: AutoBillSDK = AutoBillSDK().init_sdk(request_token_dto=CommonData.get_request_token_dto())

    try:
        response = autobill_sdk.account.payment_method_details(account_id="KZ558V", reference="check_processor1")
        print(response)
        # ResponseToObj().process(response=response["accounts"][0])
    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


test_payment_method_details()
