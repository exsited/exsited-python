from ab_py.common.sdk_util import SDKUtil
from ab_py.exsited.common.common_enum import SortDirection
from ab_py.exsited.item_fulfillment.dto.item_fulfillment_dto import ItemFulfillmentListResponseDTO, \
    ItemFulfillmentCreateDTO, ItemFulfillmentDetailsDTO, ItemFulfillmentInvoiceDTO, ItemFulfillmentInvoiceListDTO
from ab_py.exsited.item_fulfillment.item_fulfillment_api_url import ItemFulfillmentApiUrl
from ab_py.http.ab_rest_processor import ABRestProcessor


class ItemFulfillment(ABRestProcessor):

    def list(self, limit: int = None, offset: int = None, direction: SortDirection = None,
             order_by: str = None) -> ItemFulfillmentListResponseDTO:
        params = SDKUtil.init_pagination_params(limit=limit, offset=offset, direction=direction, order_by=order_by)
        response = self.get(url=ItemFulfillmentApiUrl.ITEM_FULFILLMENTS, params=params,
                            response_obj=ItemFulfillmentListResponseDTO())
        return response

    def create(self, id: str, request_data: ItemFulfillmentCreateDTO) -> ItemFulfillmentInvoiceDTO:
        response = self.post(url=ItemFulfillmentApiUrl.ITEM_INVOICE_FULFILLMENTS.format(inv_id=id),
                             request_obj=request_data, response_obj=ItemFulfillmentInvoiceDTO())
        return response

    def details(self, id: str) -> ItemFulfillmentDetailsDTO:
        response = self.get(url=ItemFulfillmentApiUrl.ITEM_FULFILLMENTS + f"/{id}",
                            response_obj=ItemFulfillmentDetailsDTO())
        return response

    def invoice_fulfillments(self, id: str, limit: int = None, offset: int = None, direction: SortDirection = None,
                             order_by: str = None) -> ItemFulfillmentInvoiceListDTO:
        params = SDKUtil.init_pagination_params(limit=limit, offset=offset, direction=direction, order_by=order_by)
        response = self.get(url=ItemFulfillmentApiUrl.INVOICE_ITEM_FULFILLMENTS_URL.format(inv_id=id), params=params,
                            response_obj=ItemFulfillmentInvoiceListDTO())
        return response

    def invoice_fulfillment_by_uuid(self, id: str, uuid: str) -> ItemFulfillmentInvoiceDTO:
        response = self.get(url=ItemFulfillmentApiUrl.INVOICE_ITEM_FULFILLMENT_DETAILS_URL.format(inv_id=id,
                                                                                                  uuid=uuid),
                            response_obj=ItemFulfillmentInvoiceDTO())
        return response


