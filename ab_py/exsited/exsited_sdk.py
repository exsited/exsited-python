from ab_py.exsited.account.account import Account
from ab_py.exsited.auth.dto.token_dto import RequestTokenDTO
from ab_py.exsited.invoice.invoice import Invoice
from ab_py.exsited.order.order import Order
from ab_py.exsited.purchase_order.purchase_order import PurchaseOrder
from ab_py.exsited.setting.setting import Setting

from ab_py.exsited.payment.payment import Payment

class ExsitedSDK:
    _request_token_dto: RequestTokenDTO = None
    account: Account = None
    order: Order = None
    invoice: Invoice = None
    setting: Setting = None
    payment: Payment = None
    purchase_order: PurchaseOrder = None

    def __init__(self, exsited_url: str = None, grant_type: str = None, client_id: str = None, client_secret: str = None, redirect_uri: str = None):
        if grant_type and client_id and client_secret and redirect_uri:
            self._request_token_dto = RequestTokenDTO(
                grantType=grant_type,
                clientId=client_id,
                clientSecret=client_secret,
                redirectUri=redirect_uri,
                exsitedUrl=exsited_url,
            )
            self._init_endpoints()

    def _init_endpoints(self):
        self.account = Account(request_token_dto=self._request_token_dto)
        self.order = Order(request_token_dto=self._request_token_dto)
        self.invoice = Invoice(request_token_dto=self._request_token_dto)
        self.setting = Setting(request_token_dto=self._request_token_dto)
        self.payment = Payment(request_token_dto=self._request_token_dto)
        self.purchase_order = PurchaseOrder(request_token_dto=self._request_token_dto)

    def init_sdk(self, request_token_dto: RequestTokenDTO) -> 'ExsitedSDK':
        self._request_token_dto = request_token_dto
        self._init_endpoints()
        return self
