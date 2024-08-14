from ab_py.exsited.account.dto.account_dto import AccountDataDTO, AccountCreateDTO, AccountUpdateInformationDTO, \
    PaymentMethodsAddDTO, PaymentCardMethodsAddDTO, AccountCancelDataDTO, AccountReactivateDataDTO, \
    AccountContactUpdateDTO, AccountCancelDTO
from ab_py.exsited.account.dto.account_nested_dto import PaymentMethodsDataDTO, PaymentCardMethodsDataDTO, ContactDTO, \
    EmailDTO, PhoneDTO, AccountContactUpdate
from ab_py.exsited.account.dto.account_nested_dto import PaymentMethodsDataDTO, PaymentCardMethodsDataDTO, \
    PaymentCardDirectDebitDataDTO, AdditionalFieldsDTO
from ab_py.exsited.exsited_sdk import ExsitedSDK
from ab_py.common.ab_exception import ABException
from ab_py.common.sdk_conf import SDKConfig
from tests.common.common_data import CommonData


def test_account_create_basic():
    SDKConfig.PRINT_REQUEST_DATA = False
    SDKConfig.PRINT_RAW_RESPONSE = False

    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(request_token_dto=CommonData.get_request_token_dto())

    try:
        request_data = AccountCreateDTO(account=AccountDataDTO(name="MeharajTest07", emailAddress="meharajtest@yopmail.com"))
        response = exsited_sdk.account.create(request_data=request_data)
        # ResponseToObj().process(response=response)
    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


def test_account_list_basic():
    SDKConfig.PRINT_REQUEST_DATA = False
    SDKConfig.PRINT_RAW_RESPONSE = False

    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(request_token_dto=CommonData.get_request_token_dto())

    try:
        response = exsited_sdk.account.list()
        print(response)
        # ResponseToObj().process(response=response["accounts"][0])
    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


def test_account_details():
    SDKConfig.PRINT_REQUEST_DATA = False
    SDKConfig.PRINT_RAW_RESPONSE = False

    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(request_token_dto=CommonData.get_request_token_dto())

    try:
        response = exsited_sdk.account.details(id="TB9H-0000000172")
        print(response)
        # ResponseToObj().process(response=response["accounts"][0])
    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


def test_account_details_information():
    SDKConfig.PRINT_REQUEST_DATA = False
    SDKConfig.PRINT_RAW_RESPONSE = False

    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(request_token_dto=CommonData.get_request_token_dto())

    try:
        response = exsited_sdk.account.details_information(id="TB9H-0000000172")
        print(response)
        # ResponseToObj().process(response=response["accounts"][0])
    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


def test_account_cancel():
    SDKConfig.PRINT_REQUEST_DATA = False
    SDKConfig.PRINT_RAW_RESPONSE = False

    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(request_token_dto=CommonData.get_request_token_dto())

    try:
        request_data = AccountCancelDataDTO(effectiveDate="2024-08-07")
        response = exsited_sdk.account.cancel(id="JJEX-0000000173", request_data=request_data)
        print(response)
    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


def test_account_reactivate():
    SDKConfig.PRINT_REQUEST_DATA = False
    SDKConfig.PRINT_RAW_RESPONSE = False

    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(request_token_dto=CommonData.get_request_token_dto())

    try:
        request_data = AccountReactivateDataDTO(effectiveDate="2024-08-07")
        response = exsited_sdk.account.reactivate(id="JJEX-0000000173", request_data=request_data)
        print(response)
    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


def test_account_update_info():
    SDKConfig.PRINT_REQUEST_DATA = False
    SDKConfig.PRINT_RAW_RESPONSE = False

    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(request_token_dto=CommonData.get_request_token_dto())

    try:
        request_data = AccountUpdateInformationDTO(account=AccountDataDTO(name="Name Update Done 05", emailAddress="testupdate05@yopmail.com", displayName="NameUpdateDisplay05", description="test update"))
        response = exsited_sdk.account.update_information(id="JJEX-0000000173", request_data=request_data)
        print(response)
    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


def test_account_delete():
    SDKConfig.PRINT_REQUEST_DATA = False
    SDKConfig.PRINT_RAW_RESPONSE = False

    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(request_token_dto=CommonData.get_request_token_dto())

    try:
        response = exsited_sdk.account.delete(id="8LX6-0000000158")
        print(response)
        # ResponseToObj().process(response=response["accounts"][0])
    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


def test_account_contacts():
    SDKConfig.PRINT_REQUEST_DATA = False
    SDKConfig.PRINT_RAW_RESPONSE = False

    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(request_token_dto=CommonData.get_request_token_dto())

    try:
        response = exsited_sdk.account.get_contacts(id="TB9H-0000000172")
        print(response)
    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


def test_account_contacts_type():
    SDKConfig.PRINT_REQUEST_DATA = False
    SDKConfig.PRINT_RAW_RESPONSE = False

    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(request_token_dto=CommonData.get_request_token_dto())

    try:
        response = exsited_sdk.account.get_contact_type(id="TB9H-0000000172", contact_type="CONTACT_1")
        print(response)
    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


def test_account_contact_update():
    SDKConfig.PRINT_REQUEST_DATA = False
    SDKConfig.PRINT_RAW_RESPONSE = False

    exsited_sdk = ExsitedSDK().init_sdk(request_token_dto=CommonData.get_request_token_dto())

    try:
        contact_dto = ContactDTO(firstName="JohnXXX", lastName="DoeXXX", email=EmailDTO(address="johnXXX@yopmail.com"), phone=PhoneDTO(number="1234567890"))
        request_data = AccountContactUpdateDTO(account=AccountContactUpdate(contact=contact_dto))
        print("Request Data:", request_data)

        response = exsited_sdk.account.update_contact(id="TB9H-0000000172", contact_type="CONTACT_1", request_data=request_data)
        print("Response Data:", response)
    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


def test_account_contact_delete():
    SDKConfig.PRINT_REQUEST_DATA = False
    SDKConfig.PRINT_RAW_RESPONSE = False

    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(request_token_dto=CommonData.get_request_token_dto())

    try:
        response = exsited_sdk.account.contact_delete(id="27XE-0000000179", contact_type="CONTACT_1")
        print(response)
        # ResponseToObj().process(response=response["accounts"][0])
    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


def test_account_payment_methods_add():
    SDKConfig.PRINT_REQUEST_DATA = True
    SDKConfig.PRINT_RAW_RESPONSE = False

    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(request_token_dto=CommonData.get_request_token_dto())

    try:
        payment_method: PaymentMethodsDataDTO = PaymentMethodsDataDTO(
            processorType="OTHER",
            default="false",
            paymentProcessor="Cash",
            reference="check_processor1",
        )
        response = exsited_sdk.account.add_payment_method(account_id="1264-0000000103", request_data=PaymentMethodsAddDTO().method(payment_method=payment_method))
        print(response)
    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


def test_account_payment_card_methods_add():
    SDKConfig.PRINT_REQUEST_DATA = True
    SDKConfig.PRINT_RAW_RESPONSE = False

    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(request_token_dto=CommonData.get_request_token_dto())

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
        response = exsited_sdk.account.add_payment_card_method(account_id="1264-0000000103", request_data=PaymentCardMethodsAddDTO().method(payment_method=payment_method))
        print(response)
    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


def test_account_payment_card_direct_debit_methods_add():
    SDKConfig.PRINT_REQUEST_DATA = True
    SDKConfig.PRINT_RAW_RESPONSE = False

    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(request_token_dto=CommonData.get_request_token_dto())

    try:
        payment_method: PaymentCardDirectDebitDataDTO = PaymentCardDirectDebitDataDTO(
            processorType="DIRECT_DEBIT",
            default="true",
            paymentProcessor="Stripe Direct Debit",
            accountNumber="000123456",
            routingNumber="000000",
            accountName="Sami",
            reference="samidirectdebit",
            additionalFields=AdditionalFieldsDTO(hostIp="118.127.108.3"),
        )
        response = exsited_sdk.account.add_payment_card_method(account_id="1264-0000000103", request_data=PaymentCardMethodsAddDTO().method(payment_method=payment_method))
        print(response)
    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


def test_list_payment_methods():
    SDKConfig.PRINT_REQUEST_DATA = False
    SDKConfig.PRINT_RAW_RESPONSE = False

    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(request_token_dto=CommonData.get_request_token_dto())

    try:
        response = exsited_sdk.account.list_payment_method(account_id="KZ558V")
        print(response)
        # ResponseToObj().process(response=response["accounts"][0])
    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


def test_delete_payment_methods():
    SDKConfig.PRINT_REQUEST_DATA = False
    SDKConfig.PRINT_RAW_RESPONSE = False

    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(request_token_dto=CommonData.get_request_token_dto())

    try:
        response = exsited_sdk.account.delete_payment_method(account_id="KZ558V", reference="check_processor")
        print(response)
        # ResponseToObj().process(response=response["accounts"][0])
    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


def test_payment_method_details():
    SDKConfig.PRINT_REQUEST_DATA = False
    SDKConfig.PRINT_RAW_RESPONSE = False

    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(request_token_dto=CommonData.get_request_token_dto())

    try:
        response = exsited_sdk.account.payment_method_details(account_id="KZ558V", reference="check_processor1")
        print(response)
        # ResponseToObj().process(response=response["accounts"][0])
    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


#test_payment_method_details()
#test_account_create_basic()
##test_account_details()
#test_account_delete()
#test_account_update_info()
#test_account_contacts()
#test_account_contacts_type()
#test_account_contact_update()
#test_account_reactivate()
test_account_contact_delete()
