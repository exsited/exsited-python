from ab_py.autobill.common.common_enum import SortDirection
from ab_py.autobill.invoice.dto.invoice_dto import InvoiceDetailsDTO, InvoiceListDTO
from ab_py.autobill.invoice.invoice_api_url import InvoiceApiUrl
from ab_py.common.sdk_util import SDKUtil
from ab_py.http.ab_rest_processor import ABRestProcessor


class Invoice(ABRestProcessor):
    def list(self, limit: int = None, offset: int = None, direction: SortDirection = None, order_by: str = None) -> InvoiceListDTO:
        params = SDKUtil.init_pagination_params(limit=limit, offset=offset, direction=direction, order_by=order_by)
        response = self.get(url=InvoiceApiUrl.INVOICES, params=params, response_obj=InvoiceListDTO())
        return response

    def details(self, id: str):
        response = self.get(url=InvoiceApiUrl.INVOICES + f"/{id}", response_obj=InvoiceDetailsDTO())
        return response
