from exsited.http.file_token_manager import FileTokenManager

from exsited.exsited.exsited_sdk import ExsitedSDK
from exsited.common.ab_exception import ABException
from exsited.common.sdk_conf import SDKConfig
from exsited.exsited.order.dto.order_nested_dto import OrderLineDTO
from exsited.exsited.return_merchandise_authorisations.dto.return_merchandise_authorisations_dto import \
    ReturnMerchandiseAuthorisationDetailsDTO, ReturnMerchandiseAuthorisationDTO, ReturnItemDTO, \
    CreateReturnMerchandiseAuthorisationDTO, RmaReturnDataDTO, CreateReceiveReturnMerchandiseAuthorisationsDTO, \
    ReceiveReturnMerchandiseAuthorisationsListDTO, ReceiveReturnDTO, ReturnMerchandiseAuthorisationCreationDTO
from tests.common.common_data import CommonData
from exsited.exsited.invoice.dto.invoice_dto import InvoiceCreateDTO, InvoiceDataDTO


def test_return_merchandise_authorisations_list():
    SDKConfig.PRINT_REQUEST_DATA = False
    SDKConfig.PRINT_RAW_RESPONSE = False

    token_file_path = "shared_token.json"
    file_token_mgr = FileTokenManager(token_file_path)

    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(
        request_token_dto=CommonData.get_request_token_dto(),
        file_token_mgr=file_token_mgr
    )

    try:
        response = exsited_sdk.return_merchandise_authorisations.list()
        print(response)

    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


def test_return_merchandise_authorisations_receive_list():
    SDKConfig.PRINT_REQUEST_DATA = False
    SDKConfig.PRINT_RAW_RESPONSE = False

    token_file_path = "shared_token.json"
    file_token_mgr = FileTokenManager(token_file_path)

    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(
        request_token_dto=CommonData.get_request_token_dto(),
        file_token_mgr=file_token_mgr
    )

    try:
        response = exsited_sdk.return_merchandise_authorisations.receive_list(id='', rma_id='')
        print(response)

    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


def test_return_merchandise_authorisations_details():
    SDKConfig.PRINT_REQUEST_DATA = False
    SDKConfig.PRINT_RAW_RESPONSE = False

    token_file_path = "shared_token.json"
    file_token_mgr = FileTokenManager(token_file_path)

    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(
        request_token_dto=CommonData.get_request_token_dto(),
        file_token_mgr=file_token_mgr
    )

    try:
        response = exsited_sdk.return_merchandise_authorisations.details(id="")
        print(response)

    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


def test_return_merchandise_authorisations_create():
    SDKConfig.PRINT_REQUEST_DATA = False
    SDKConfig.PRINT_RAW_RESPONSE = False

    token_file_path = "shared_token.json"
    file_token_mgr = FileTokenManager(token_file_path)

    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(
        request_token_dto=CommonData.get_request_token_dto(),
        file_token_mgr=file_token_mgr
    )

    try:
        request_data = CreateReturnMerchandiseAuthorisationDTO(
            returnMerchandiseAuthorisations=ReturnMerchandiseAuthorisationCreationDTO(
                date='', note='', returns=[RmaReturnDataDTO(
                    itemUuid='', uuid='', rmaQuantity='')]))

        response = exsited_sdk.return_merchandise_authorisations.invoice_rma_create(id='', request_data=request_data)
        print(response)

    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


def test_receive_return_merchandise_authorisations_create():
    SDKConfig.PRINT_REQUEST_DATA = False
    SDKConfig.PRINT_RAW_RESPONSE = False

    token_file_path = "shared_token.json"
    file_token_mgr = FileTokenManager(token_file_path)

    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(
        request_token_dto=CommonData.get_request_token_dto(),
        file_token_mgr=file_token_mgr
    )

    try:
        request_data = CreateReceiveReturnMerchandiseAuthorisationsDTO(
            receiveReturnMerchandiseAuthorisations=ReceiveReturnMerchandiseAuthorisationsListDTO(
                receiveReturns=[ReceiveReturnDTO(
                    uuid='', rmaReceiveQuantity='')]))

        response = exsited_sdk.return_merchandise_authorisations.invoice_receive_rma_create(id='', rma_id='', request_data=request_data)
        print(response)

    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)

def test_return_merchandise_authorisations_receive_details():
    SDKConfig.PRINT_REQUEST_DATA = False
    SDKConfig.PRINT_RAW_RESPONSE = False

    token_file_path = "shared_token.json"
    file_token_mgr = FileTokenManager(token_file_path)

    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(
        request_token_dto=CommonData.get_request_token_dto(),
        file_token_mgr=file_token_mgr
    )

    try:
        response = exsited_sdk.return_merchandise_authorisations.receive_details(id='', rma_id='', rec_id='')
        print(response)

    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)

def test_invoice_return_merchandise_authorisations_list():
    SDKConfig.PRINT_REQUEST_DATA = False
    SDKConfig.PRINT_RAW_RESPONSE = False

    token_file_path = "shared_token.json"
    file_token_mgr = FileTokenManager(token_file_path)

    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(
        request_token_dto=CommonData.get_request_token_dto(),
        file_token_mgr=file_token_mgr
    )

    try:
        response = exsited_sdk.return_merchandise_authorisations.invoice_list(id="")
        print(response)

    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


def test_invoice_return_merchandise_authorisations_details():
    SDKConfig.PRINT_REQUEST_DATA = False
    SDKConfig.PRINT_RAW_RESPONSE = False

    token_file_path = "shared_token.json"
    file_token_mgr = FileTokenManager(token_file_path)

    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(
        request_token_dto=CommonData.get_request_token_dto(),
        file_token_mgr=file_token_mgr
    )

    try:
        response = exsited_sdk.return_merchandise_authorisations.invoice_rma_details(id="", rma_id='')
        print(response)

    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)