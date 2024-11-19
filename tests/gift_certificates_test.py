from exsited.common.ab_exception import ABException
from exsited.common.sdk_conf import SDKConfig
from exsited.exsited.exsited_sdk import ExsitedSDK
from exsited.exsited.gift_certificates.dto.gift_certificates_dto import GiftCertificateDetailsDTO, GiftCertificateDTO
from tests.common.common_data import CommonData


def test_gift_certificates_list():
    SDKConfig.PRINT_REQUEST_DATA = True
    SDKConfig.PRINT_RAW_RESPONSE = False
    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(request_token_dto=CommonData.get_request_token_dto())
    try:

        response = exsited_sdk.gift_certificates.list()
        print(response)
    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


def test_gift_certificate_details():
    SDKConfig.PRINT_REQUEST_DATA = True
    SDKConfig.PRINT_RAW_RESPONSE = False
    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(request_token_dto=CommonData.get_request_token_dto())
    try:

        response = exsited_sdk.gift_certificates.details(id="")
        print(response)
    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


def test_gift_certificate_allocations_list():
    SDKConfig.PRINT_REQUEST_DATA = True
    SDKConfig.PRINT_RAW_RESPONSE = False
    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(request_token_dto=CommonData.get_request_token_dto())
    try:

        response = exsited_sdk.gift_certificates.allocation_list(id="")
        print(response)
    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


def test_gift_certificate_transactions_list():
    SDKConfig.PRINT_REQUEST_DATA = True
    SDKConfig.PRINT_RAW_RESPONSE = False
    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(request_token_dto=CommonData.get_request_token_dto())
    try:
        response = exsited_sdk.gift_certificates.transaction_list(id="")
        print(response)
    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


def test_gift_certificate_create():
    SDKConfig.PRINT_REQUEST_DATA = True
    SDKConfig.PRINT_RAW_RESPONSE = False
    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(request_token_dto=CommonData.get_request_token_dto())
    try:

        request_obj = GiftCertificateDetailsDTO(giftCertificate=GiftCertificateDTO(
            status="",
            accountingCode="",
            amount="",
            currency="",
            expiryDate=""
        ))
        response = exsited_sdk.gift_certificates.create(request_data=request_obj)
        print(response)
    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


def test_gift_disable():
    SDKConfig.PRINT_REQUEST_DATA = True
    SDKConfig.PRINT_RAW_RESPONSE = False
    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(request_token_dto=CommonData.get_request_token_dto())
    try:
        response = exsited_sdk.gift_certificates.disable(id="")
        print(response)
    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


def test_gift_enable():
    SDKConfig.PRINT_REQUEST_DATA = True
    SDKConfig.PRINT_RAW_RESPONSE = False
    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(request_token_dto=CommonData.get_request_token_dto())
    try:
        response = exsited_sdk.gift_certificates.enable(id="")
        print(response)
    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


def test_gift_certificate_allocate():
    SDKConfig.PRINT_REQUEST_DATA = True
    SDKConfig.PRINT_RAW_RESPONSE = False
    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(request_token_dto=CommonData.get_request_token_dto())
    try:
        request_obj = GiftCertificateDetailsDTO(giftCertificate=GiftCertificateDTO(account=""))
        response = exsited_sdk.gift_certificates.allocate(id="",
                                                          request_data=request_obj)
        print(response)
    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


def test_gift_certificate_deallocate():
    SDKConfig.PRINT_REQUEST_DATA = True
    SDKConfig.PRINT_RAW_RESPONSE = False
    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(request_token_dto=CommonData.get_request_token_dto())
    try:
        request_obj = GiftCertificateDetailsDTO(giftCertificate=GiftCertificateDTO(account=""))
        response = exsited_sdk.gift_certificates.deallocate(id="",
                                                            request_data=request_obj)
        print(response)
    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


def test_gift_certificate_amend():
    SDKConfig.PRINT_REQUEST_DATA = True
    SDKConfig.PRINT_RAW_RESPONSE = False
    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(request_token_dto=CommonData.get_request_token_dto())
    try:
        request_obj = GiftCertificateDetailsDTO(giftCertificate=GiftCertificateDTO(
            accountingCode="",
            amount="",
        ))
        response = exsited_sdk.gift_certificates.amend(id="",
                                                       request_data=request_obj)
        print(response)
    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


def test_gift_certificate_update():
    SDKConfig.PRINT_REQUEST_DATA = True
    SDKConfig.PRINT_RAW_RESPONSE = False
    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(request_token_dto=CommonData.get_request_token_dto())
    try:
        request_obj = GiftCertificateDetailsDTO(giftCertificate=GiftCertificateDTO(
            expiryDate=""
        ))
        response = exsited_sdk.gift_certificates.update(id="",
                                                        request_data=request_obj)
        print(response)
    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


def test_gift_certificate_delete():
    SDKConfig.PRINT_REQUEST_DATA = True
    SDKConfig.PRINT_RAW_RESPONSE = False
    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(request_token_dto=CommonData.get_request_token_dto())
    try:
        response = exsited_sdk.gift_certificates.delete(id="")
        print(response)
    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


# test_gift_certificates_list()
# test_gift_certificate_details()
# test_gift_certificate_allocations_list()
# test_gift_certificate_transactions_list()
# test_gift_certificate_create()
# test_gift_disable()
# test_gift_enable()
# test_gift_certificate_allocate()
# test_gift_certificate_deallocate()
# test_gift_certificate_amend()
# test_gift_certificate_update()
test_gift_certificate_delete()
