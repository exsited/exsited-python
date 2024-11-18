from ab_py.common.ab_exception import ABException
from ab_py.common.sdk_conf import SDKConfig
from ab_py.exsited.exsited_sdk import ExsitedSDK
from ab_py.exsited.gift_certificates.dto.gift_certificates_dto import GiftCertificateDetailsDTO, GiftCertificateDTO
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

        response = exsited_sdk.gift_certificates.details(id="725e3745-d685-4371-abcd-625d458c3b89")
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

        response = exsited_sdk.gift_certificates.allocation_list(id="725e3745-d685-4371-abcd-625d458c3b89")
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
        response = exsited_sdk.gift_certificates.transaction_list(id="725e3745-d685-4371-abcd-625d458c3b89")
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
            status="ACTIVE",
            accountingCode="Gift Certificate",
            amount="100",
            currency="AUD",
            expiryDate="2031-09-24"
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
        response = exsited_sdk.gift_certificates.disable(id="7b6447f2-1e60-43d3-aec2-6c7e0d018756")
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
        response = exsited_sdk.gift_certificates.enable(id="7b6447f2-1e60-43d3-aec2-6c7e0d018756")
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
        request_obj = GiftCertificateDetailsDTO(giftCertificate=GiftCertificateDTO(account="WAU656"))
        response = exsited_sdk.gift_certificates.allocate(id="7b6447f2-1e60-43d3-aec2-6c7e0d018756",
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
        request_obj = GiftCertificateDetailsDTO(giftCertificate=GiftCertificateDTO(account="WAU656"))
        response = exsited_sdk.gift_certificates.deallocate(id="7b6447f2-1e60-43d3-aec2-6c7e0d018756",
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
            accountingCode="Gift Certificate",
            amount="100",
        ))
        response = exsited_sdk.gift_certificates.amend(id="7b6447f2-1e60-43d3-aec2-6c7e0d018756",
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
            expiryDate="2029-08-05"
        ))
        response = exsited_sdk.gift_certificates.update(id="7b6447f2-1e60-43d3-aec2-6c7e0d018756",
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
        response = exsited_sdk.gift_certificates.delete(id="a84b911c-9a9c-4cb5-9d55-e7712550710a")
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
