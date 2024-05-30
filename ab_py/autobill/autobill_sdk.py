from ab_py.autobill.account.account import Account
from ab_py.autobill.auth.dto.token_dto import RequestTokenDTO
from ab_py.autobill.invoice.invoice import Invoice
from ab_py.autobill.order.order import Order


class AutoBillSDK:
    _request_token_dto: RequestTokenDTO = None
    account: Account = None
    order: Order = None
    invoice: Invoice = None

    def __init__(self, autobill_url: str = None, grant_type: str = None, client_id: str = None, client_secret: str = None, redirect_uri: str = None):
        if grant_type and client_id and client_secret and redirect_uri:
            self._request_token_dto = RequestTokenDTO(
                grantType=grant_type,
                clientId=client_id,
                clientSecret=client_secret,
                redirectUri=redirect_uri,
                autoBillUrl=autobill_url,
            )
            self._init_endpoints()

    def _init_endpoints(self):
        self.account = Account(request_token_dto=self._request_token_dto)
        self.order = Order(request_token_dto=self._request_token_dto)
        self.invoice = Invoice(request_token_dto=self._request_token_dto)

    def init_sdk(self, request_token_dto: RequestTokenDTO) -> 'AutobillSDK':
        self._request_token_dto = request_token_dto
        self._init_endpoints()
        return self
