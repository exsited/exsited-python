from exsited.common.sdk_util import SDKUtil
from exsited.exsited.common.common_enum import SortDirection
from exsited.exsited.setting.dto.setting_dto import SettingPaymentProcessorListDTO
from exsited.http.ab_rest_processor import ABRestProcessor
from exsited.exsited.setting.setting_api_url import SettingApiUrl


class Setting(ABRestProcessor):
    def get_settings(self, limit: int = None, offset: int = None, direction: SortDirection = None,
             order_by: str = None):
        params = SDKUtil.init_pagination_params(limit=limit, offset=offset, direction=direction, order_by=order_by)
        response = self.get(url=SettingApiUrl.SETTINGS, params=params, response_obj={})
        return response

    def get_settings_payment_processor(self, limit: int = None, offset: int = None, direction: SortDirection = None,
             order_by: str = None) -> SettingPaymentProcessorListDTO:
        params = SDKUtil.init_pagination_params(limit=limit, offset=offset, direction=direction, order_by=order_by)
        response = self.get(url=SettingApiUrl.SETTINGS_PAYMENT_PROCESSOR, params=params, response_obj=SettingPaymentProcessorListDTO())
        return response
