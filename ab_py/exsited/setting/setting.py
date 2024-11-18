from ab_py.common.sdk_util import SDKUtil
from ab_py.exsited.common.common_enum import SortDirection
from ab_py.exsited.setting.dto.setting_dto import SettingPaymentProcessorListDTO
from ab_py.http.ab_rest_processor import ABRestProcessor
from ab_py.exsited.setting.setting_api_url import SettingApiUrl


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
