from exsited.exsited.common.common_enum import SortDirection
from exsited.exsited.item_receipt.dto.item_receipt_dto import ItemReceiptListDTO, ItemReceiptDetailsDTO
from exsited.exsited.item_receipt.item_receipt_url import ItemReceiptApiUrl
from exsited.common.sdk_util import SDKUtil
from exsited.http.ab_rest_processor import ABRestProcessor

class ItemReceipt(ABRestProcessor):

    def list(self, limit: int = None, offset: int = None, direction: SortDirection = None,
             order_by: str = None) -> ItemReceiptListDTO:
        params = SDKUtil.init_pagination_params(limit=limit, offset=offset, direction=direction, order_by=order_by)
        response = self.get(url=ItemReceiptApiUrl.ITEM_RECEIPT_LIST, params=params, response_obj=ItemReceiptListDTO())
        return response

    def details(self, id: str) -> ItemReceiptDetailsDTO:
        response = self.get(url=ItemReceiptApiUrl.ITEM_RECEIPT_DETAILS.format(id=id),
                            response_obj=ItemReceiptDetailsDTO())
        return response

    def purchase_order_details(self, id: str) -> ItemReceiptDetailsDTO:
        response = self.get(url=ItemReceiptApiUrl.ITEM_RECEIPT_DETAILS.format(id=id),
                            response_obj=ItemReceiptDetailsDTO())
        return response