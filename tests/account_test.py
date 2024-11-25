from exsited.exsited.account.dto.account_dto import AccountDataDTO, AccountCreateDTO, AccountUpdateInformationDTO, \
    PaymentMethodsAddDTO, PaymentCardMethodsAddDTO, AccountCancelDataDTO, AccountReactivateDataDTO, \
    AccountContactUpdateDTO, AccountCancelDTO, AccountAddressesAddDTO, AccountAddressesAdd
from exsited.exsited.account.dto.account_nested_dto import PaymentMethodsDataDTO, PaymentCardMethodsDataDTO, ContactDTO, \
    EmailDTO, PhoneDTO, AccountContactUpdate, PaymentMethodsDTO
from exsited.exsited.account.dto.account_nested_dto import PaymentMethodsDataDTO, PaymentCardMethodsDataDTO, \
    PaymentCardDirectDebitDataDTO, AdditionalFieldsDTO
from exsited.exsited.common.dto.common_dto import AddressDTO
from exsited.exsited.exsited_sdk import ExsitedSDK
from exsited.common.ab_exception import ABException
from exsited.common.sdk_conf import SDKConfig
from tests.common.common_data import CommonData


def test_account_create_basic():
    SDKConfig.PRINT_REQUEST_DATA = False
    SDKConfig.PRINT_RAW_RESPONSE = False

    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(request_token_dto=CommonData.get_request_token_dto())

    try:
        request_data = AccountCreateDTO(
            account=AccountDataDTO(name="", emailAddress=""))
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
        response = exsited_sdk.account.details(id="")
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
        response = exsited_sdk.account.details_information(id="")
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
        request_data = AccountCancelDataDTO(effectiveDate="")
        response = exsited_sdk.account.cancel(id="", request_data=request_data)
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
        request_data = AccountReactivateDataDTO(effectiveDate="")
        response = exsited_sdk.account.reactivate(id="", request_data=request_data)
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
        request_data = AccountUpdateInformationDTO(
            account=AccountDataDTO(name="", emailAddress="",
                                   displayName="", description="test "))
        response = exsited_sdk.account.update_information(id="", request_data=request_data)
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
        response = exsited_sdk.account.delete(id="")
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
        response = exsited_sdk.account.get_contacts(id="")
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
        response = exsited_sdk.account.get_contact_type(id="", contact_type="")
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
        contact_dto = ContactDTO(firstName="", lastName="", email=EmailDTO(address=""),
                                 phone=PhoneDTO(number=""))
        request_data = AccountContactUpdateDTO(account=AccountContactUpdate(contact=contact_dto))
        print("Request Data:", request_data)

        response = exsited_sdk.account.update_contact(id="", contact_type="",
                                                      request_data=request_data)
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
        response = exsited_sdk.account.contact_delete(id="", contact_type="")
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
            processorType="",
            default="",
            paymentProcessor="",
            reference="",
        )
        response = exsited_sdk.account.add_payment_method(account_id="",
                                                          request_data=PaymentMethodsAddDTO().method(
                                                              payment_method=payment_method))
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
            processorType="",
            default="",
            paymentProcessor="",
            reference="",
            cardType="",
            token="",
            cardNumber="",
            expiryMonth="",
            expiryYear="",
        )
        response = exsited_sdk.account.add_payment_card_method(account_id="",
                                                               request_data=PaymentCardMethodsAddDTO().method(
                                                                   payment_method=payment_method))
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
            processorType="",
            default="",
            paymentProcessor="",
            accountNumber="",
            routingNumber="",
            accountName="",
            reference="",
            additionalFields=AdditionalFieldsDTO(hostIp=""),
        )
        response = exsited_sdk.account.add_payment_card_method(account_id="",
                                                               request_data=PaymentCardMethodsAddDTO().method(
                                                                   payment_method=payment_method))
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
        response = exsited_sdk.account.list_payment_method(account_id="")
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
        response = exsited_sdk.account.delete_payment_method(account_id="", reference="")
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
        response = exsited_sdk.account.payment_method_details(account_id="", reference="")
        print(response)
        # ResponseToObj().process(response=response["accounts"][0])
    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


def test_get_billing_preferences():
    SDKConfig.PRINT_REQUEST_DATA = False
    SDKConfig.PRINT_RAW_RESPONSE = False

    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(request_token_dto=CommonData.get_request_token_dto())

    try:
        response = exsited_sdk.account.billing_preference_details(account_id="")
        print(response)
    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


def test_add_addresses():
    SDKConfig.PRINT_REQUEST_DATA = False
    SDKConfig.PRINT_RAW_RESPONSE = False

    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(request_token_dto=CommonData.get_request_token_dto())

    try:
        address_one = AddressDTO(
            addressLine1="",
            addressLine2="",
            addressLine3="",
            addressLine4="",
            addressLine5="",
            post_code="",
            city="",
            state="",
            country="",
            isDefaultBilling=False,
            isDefaultShipping=False
        )
        request_obj = AccountAddressesAddDTO(
            account=AccountAddressesAdd(addresses=[address_one])
        )
        response = exsited_sdk.account.add_addresses(id="", request_data=request_obj)
        print(response)
    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


def test_update_payment_methods():
    SDKConfig.PRINT_REQUEST_DATA = False
    SDKConfig.PRINT_RAW_RESPONSE = False

    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(request_token_dto=CommonData.get_request_token_dto())

    try:
        payment_method = PaymentMethodsDataDTO(reference="")
        request_obj = PaymentMethodsAddDTO(
            account=PaymentMethodsDTO(paymentMethod=payment_method)
        )
        response = exsited_sdk.account.update_payment_method(id="", reference="",  request_data=request_obj)
        print(response)
    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


def test_account_contact_modify():
    SDKConfig.PRINT_REQUEST_DATA = False
    SDKConfig.PRINT_RAW_RESPONSE = False

    exsited_sdk = ExsitedSDK().init_sdk(request_token_dto=CommonData.get_request_token_dto())

    try:
        contact_dto = ContactDTO(firstName="")
        request_data = AccountContactUpdateDTO(account=AccountContactUpdate(contact=contact_dto))

        response = exsited_sdk.account.modify_contact(id="", contact_type="",
                                                      request_data=request_data)
        print("Response Data:", response)
    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


# test_payment_method_details()
test_account_create_basic()
# test_payment_method_details()
#test_account_create_basic()
##test_account_details()
#test_account_delete()
#test_account_update_info()
#test_account_contacts()
#test_account_contacts_type()
#test_account_contact_update()
#test_account_reactivate()
# test_account_contact_delete()
# test_account_delete()
# test_account_update_info()
# test_account_contacts()
# test_account_contacts_type()
# test_account_contact_update()
# test_account_reactivate()
# test_account_contact_delete()
# test_get_billing_preferences()
# test_add_addresses()
# test_update_payment_methods()
# test_account_contact_modify()
#test_account_delete()
#test_account_update_info()
#test_account_contacts()
#test_account_contacts_type()
#test_account_contact_update()
# test_account_reactivate()
# test_account_contact_delete()

#test_account_delete()
#test_account_update_info()
#test_account_contacts()
#test_account_contacts_type()
#test_account_contact_update()
#test_account_reactivate()
# test_account_contact_delete()
# test_account_payment_methods_add()