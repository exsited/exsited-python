class PurchaseInvoiceApiUrl:
    PURCHASE_INVOICE = "/api/v3/purchase-invoices"
    PURCHASE_INVOICE_DETAILS = "/api/v3/purchase-invoices/{id}"
    PURCHASE_INVOICE_LINE_DETAILS = "/api/v3/purchase-invoices/{id}/lines/{uuid}"
    PURCHASE_INVOICE_ACCOUNT_DETAILS = "/api/v3/accounts/{id}/purchase-invoices"
    PURCHASE_INVOICE_CREATE = "/api/v3/purchase-invoices/"
    PURCHASE_INVOICE_CANCEL = "/api/v3/purchase-invoices/{id}/cancel"
    PURCHASE_INVOICE_REACTIVE = "/api/v3/purchase-invoices/{id}/reactive"
    PURCHASE_INVOICE_DELETE = "/api/v3/purchase-invoices/{id}"
    PURCHASE_INVOICE_AMEND = "/api/v3/purchase-invoices/{purchase_invoice_id}/amend"
    PURCHASE_INVOICE_INFORMATION = "/api/v3/purchase-invoices/{purchase_invoice_id}/information"
    PURCHASE_INVOICE_FROM_PURCHASE_ORDER = "/api/v3/purchase-orders/{purchase_order_id}/purchase-invoices"
