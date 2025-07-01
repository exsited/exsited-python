from exsited.http.file_token_manager import FileTokenManager

from exsited.exsited.exsited_sdk import ExsitedSDK
from exsited.common.ab_exception import ABException
from exsited.common.sdk_conf import SDKConfig
from exsited.exsited.setting.dto.setting_dto import VariationCreateRequestDTO, VariationCreateDataDTO, OptionDTO
from tests.common.common_data import CommonData

def test_get_settings_payment_processor():
    SDKConfig.PRINT_REQUEST_DATA = False
    SDKConfig.PRINT_RAW_RESPONSE = False

    token_file_path = "shared_token.json"
    file_token_mgr = FileTokenManager(token_file_path)

    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(
        request_token_dto=CommonData.get_request_token_dto(),
        file_token_mgr=file_token_mgr
    )

    try:
        response = exsited_sdk.setting.get_settings_payment_processor()
        print(response)
    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)

def test_get_settings_pricing_levels():
    SDKConfig.PRINT_REQUEST_DATA = False
    SDKConfig.PRINT_RAW_RESPONSE = False

    token_file_path = "shared_token.json"
    file_token_mgr = FileTokenManager(token_file_path)

    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(
        request_token_dto=CommonData.get_request_token_dto(),
        file_token_mgr=file_token_mgr
    )

    try:
        response = exsited_sdk.setting.get_settings_pricing_levels()
        print(response)
    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)

def test_get_settings_item_group():
    SDKConfig.PRINT_REQUEST_DATA = False
    SDKConfig.PRINT_RAW_RESPONSE = False

    token_file_path = "shared_token.json"
    file_token_mgr = FileTokenManager(token_file_path)

    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(
        request_token_dto=CommonData.get_request_token_dto(),
        file_token_mgr=file_token_mgr
    )

    try:
        response = exsited_sdk.setting.get_settings_item_group()
        print(response)
    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)

def test_get_settings_currencies():
    SDKConfig.PRINT_REQUEST_DATA = False
    SDKConfig.PRINT_RAW_RESPONSE = False

    token_file_path = "shared_token.json"
    file_token_mgr = FileTokenManager(token_file_path)

    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(
        request_token_dto=CommonData.get_request_token_dto(),
        file_token_mgr=file_token_mgr
    )

    try:
        response = exsited_sdk.setting.get_settings_currencies()
        print(response)
    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)

def test_get_settings_taxes():
    SDKConfig.PRINT_REQUEST_DATA = False
    SDKConfig.PRINT_RAW_RESPONSE = False

    token_file_path = "shared_token.json"
    file_token_mgr = FileTokenManager(token_file_path)

    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(
        request_token_dto=CommonData.get_request_token_dto(),
        file_token_mgr=file_token_mgr
    )

    try:
        response = exsited_sdk.setting.get_settings_taxes()
        print(response)
    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)

def test_get_settings_discount_profiles():
    SDKConfig.PRINT_REQUEST_DATA = False
    SDKConfig.PRINT_RAW_RESPONSE = False

    token_file_path = "shared_token.json"
    file_token_mgr = FileTokenManager(token_file_path)

    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(
        request_token_dto=CommonData.get_request_token_dto(),
        file_token_mgr=file_token_mgr
    )

    try:
        response = exsited_sdk.setting.get_settings_discount_profiles()
        print(response)
    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)

def test_get_settings_warehouses():
    SDKConfig.PRINT_REQUEST_DATA = False
    SDKConfig.PRINT_RAW_RESPONSE = False

    token_file_path = "shared_token.json"
    file_token_mgr = FileTokenManager(token_file_path)

    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(
        request_token_dto=CommonData.get_request_token_dto(),
        file_token_mgr=file_token_mgr
    )

    try:
        response = exsited_sdk.setting.get_settings_warehouses()
        print(response)

    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)

def test_get_settings_shipping_profiles():
    SDKConfig.PRINT_REQUEST_DATA = False
    SDKConfig.PRINT_RAW_RESPONSE = False

    token_file_path = "shared_token.json"
    file_token_mgr = FileTokenManager(token_file_path)

    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(
        request_token_dto=CommonData.get_request_token_dto(),
        file_token_mgr=file_token_mgr
    )

    try:
        response = exsited_sdk.setting.get_settings_shipping_profiles()
        print(response)

    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)

def test_get_settings_components():
    SDKConfig.PRINT_REQUEST_DATA = False
    SDKConfig.PRINT_RAW_RESPONSE = False

    token_file_path = "shared_token.json"
    file_token_mgr = FileTokenManager(token_file_path)

    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(
        request_token_dto=CommonData.get_request_token_dto(),
        file_token_mgr=file_token_mgr
    )

    try:
        response = exsited_sdk.setting.get_settings_components()
        print(response)

    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)

def test_get_settings_variations():
    SDKConfig.PRINT_REQUEST_DATA = False
    SDKConfig.PRINT_RAW_RESPONSE = False

    token_file_path = "shared_token.json"
    file_token_mgr = FileTokenManager(token_file_path)

    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(
        request_token_dto=CommonData.get_request_token_dto(),
        file_token_mgr=file_token_mgr
    )

    try:
        response = exsited_sdk.setting.get_settings_variations()
        print(response)

    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)

def test_settings_variations_update():
    SDKConfig.PRINT_REQUEST_DATA = False
    SDKConfig.PRINT_RAW_RESPONSE = False

    token_file_path = "shared_token.json"
    file_token_mgr = FileTokenManager(token_file_path)

    exsited_sdk: ExsitedSDK = ExsitedSDK().init_sdk(
        request_token_dto=CommonData.get_request_token_dto(),
        file_token_mgr=file_token_mgr
    )

    try:
        request_data = VariationCreateRequestDTO(
            variations=VariationCreateDataDTO(
                name="",
                displayName="",
                description="",
                options=[OptionDTO(name="", order=0)]
            ))

        response = exsited_sdk.setting.variation_update(uuid="", request_data=request_data)
        print(response)

    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)
