from exsited.exsited.common.common_enum import SortDirection
from exsited.exsited.invoice.dto.invoice_dto import InvoiceDetailsDTO, InvoiceListDTO, InvoiceCreateDTO, InvoiceDataDTO, \
    InvoiceAccountDTO, InvoiceOrderDetailsDTO, InvoiceOrderListDTO
from exsited.exsited.invoice.invoice_api_url import InvoiceApiUrl
from exsited.common.sdk_util import SDKUtil
from exsited.http.ab_rest_processor import ABRestProcessor


class Invoice(ABRestProcessor):

    def create(self, id: str, request_data: InvoiceCreateDTO) -> InvoiceDetailsDTO:
        response = self.post(url=InvoiceApiUrl.INVOICE_CREATE.format(id=id), request_obj=request_data,
                             response_obj=InvoiceDetailsDTO())
        return response

    def list(self, limit: int = None, offset: int = None, direction: SortDirection = None, order_by: str = None) -> InvoiceListDTO:
        params = SDKUtil.init_pagination_params(limit=limit, offset=offset, direction=direction, order_by=order_by)
        response = self.get(url=InvoiceApiUrl.INVOICES, params=params, response_obj=InvoiceListDTO())
        return response

    def details(self, id: str):
        response = self.get(url=InvoiceApiUrl.INVOICES + f"/{id}", response_obj=InvoiceDetailsDTO())
        return response

    def information(self, id: str):
        response = self.get(url=InvoiceApiUrl.INVOICE_INFORMATION.format(id=id), response_obj=InvoiceDetailsDTO())
        return response

    def delete(self, id: str):
        response = self.delete_request(url=InvoiceApiUrl.INVOICE_DELETE.format(id=id))
        return response


    def invoice_account(self, accountId: str):
        response = self.get(url=InvoiceApiUrl.INVOICE_ACCOUNT.format(id=accountId), response_obj=InvoiceAccountDTO())
        return response

    def match_structure(self, invoice_data):
        invoice_dict = {
         'status': invoice_data.get('status'),
         'id': invoice_data.get('id'),
         'type': invoice_data.get('type'),
         'customerPurchaseOrderId': invoice_data.get('customer_purchase_order_id'),
         'billingStartDate': invoice_data.get('billing_start_date'),
         'alternateBillingStartDate': invoice_data.get('alternate_billing_start_date'),
         'billingEndDate': invoice_data.get('billing_end_date'),
         'alternateBillingEndDate': invoice_data.get('alternate_billing_end_date'),
         'issueDate': invoice_data.get('issue_date'),
         'alternateIssueDate': invoice_data.get('alternate_issue_date'),
         'dueDate': invoice_data.get('due_date'),
         'alternateDueDate': invoice_data.get('alternate_due_date'),
         'subtotal': invoice_data.get('subtotal'),
         'tax': invoice_data.get('tax'),
         'taxTotal': invoice_data.get('tax_total'),
         'total': invoice_data.get('total'),
         'paid': invoice_data.get('paid'),
         'due': invoice_data.get('due'),
         'paymentStatus': invoice_data.get('payment_status'),
         'discountAmount': invoice_data.get('discount_amount'),
         'priceTaxInclusive': invoice_data.get('price_tax_inclusive'),
         'invoiceNote': invoice_data.get('invoice_note'),
         'accountId': invoice_data.get('account_id'),
         'orderId': invoice_data.get('order_id'),
         'createdBy': invoice_data.get('created_by'),
         'createdOn': invoice_data.get('created_on'),
         'lastUpdatedBy': invoice_data.get('last_updated_by'),
         'lastUpdatedOn': invoice_data.get('last_updated_on'),
         'uuid': invoice_data.get('uuid'),
         'version': invoice_data.get('version'),
         'lines': invoice_data.get('lines'),
         'customForms': invoice_data.get('custom_form'),
         'currency': invoice_data.get('currency')
        }

        return invoice_dict

    def invoice_details_against_order_v3(self, order_id: str, limit: int = None, offset: int = None, direction: SortDirection = None, order_by: str = None) ->InvoiceOrderDetailsDTO:
        params = SDKUtil.init_pagination_params(limit=limit, offset=offset, direction=direction, order_by=order_by)
        response = self.get(url=InvoiceApiUrl.EACH_INVOICE_V3.format(id=order_id), params=params, response_obj=InvoiceOrderDetailsDTO())
        return response.order.invoices[-1]

    def invoice_list_against_order_v3(self, order_id: str, limit: int = None, offset: int = None, direction: SortDirection = None, order_by: str = None) ->InvoiceOrderListDTO:
        params = SDKUtil.init_pagination_params(limit=limit, offset=offset, direction=direction, order_by=order_by)
        response = self.get(url=InvoiceApiUrl.EACH_INVOICE_V3.format(id=order_id), params=params, response_obj=InvoiceOrderListDTO())
        return response