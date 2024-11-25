from exsited.common.sdk_util import SDKUtil
from exsited.exsited.common.common_enum import SortDirection
from exsited.exsited.item.dto.item_dto import ItemListResponseDTO, ItemResponseDTO, ItemSaleResponseDTO, \
    ItemPurchaseResponseDTO, ItemInventoryResponseDTO, ItemDataDTO, ItemActionDTO
from exsited.exsited.item.item_api_url import ItemApiUrl
from exsited.http.ab_rest_processor import ABRestProcessor


class Item(ABRestProcessor):

    def list(self, limit: int = None, offset: int = None, direction: SortDirection = None,
             order_by: str = None) -> ItemListResponseDTO:
        params = SDKUtil.init_pagination_params(limit=limit, offset=offset, direction=direction, order_by=order_by)
        response = self.get(url=ItemApiUrl.ITEMS, params=params, response_obj=ItemListResponseDTO())
        return response

    def standard(self, id: str) -> ItemResponseDTO:
        response = self.get(url=ItemApiUrl.ITEMS_STANDARD.format(id=id), response_obj=ItemResponseDTO())
        return response

    def information(self, id: str) -> ItemResponseDTO:
        response = self.get(url=ItemApiUrl.ITEMS_INFORMATION.format(id=id), response_obj=ItemResponseDTO())
        return response

    def sale(self, id: str) -> ItemSaleResponseDTO:
        response = self.get(url=ItemApiUrl.ITEMS_SALE.format(id=id), response_obj=ItemSaleResponseDTO())
        return response

    def purchase(self, id: str) -> ItemPurchaseResponseDTO:
        response = self.get(url=ItemApiUrl.ITEMS_PURCHASE.format(id=id), response_obj=ItemPurchaseResponseDTO())
        return response

    def inventory(self, id: str) -> ItemInventoryResponseDTO:
        response = self.get(url=ItemApiUrl.ITEMS_INVENTORY.format(id=id), response_obj=ItemInventoryResponseDTO())
        return response

    def create(self, request_data: ItemActionDTO) -> ItemResponseDTO:
        response = self.post(url=ItemApiUrl.ITEMS, request_obj=request_data, response_obj=ItemResponseDTO())
        return response

    def reactivate(self, id: str):
        response = self.post(url=ItemApiUrl.ITEMS_REACTIVATE.format(id=id), response_obj=dict())
        return response

    def deactivate(self, id: str):
        response = self.post(url=ItemApiUrl.ITEMS_DEACTIVATE.format(id=id), response_obj=dict())
        return response

    def delete(self, id: str):
        response = self.delete_request(url=ItemApiUrl.ITEMS_STANDARD.format(id=id), response_obj=dict())
        return response
