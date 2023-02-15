from _typeshed import Incomplete
from twilio.base import deserialize as deserialize, serialize as serialize, values as values
from twilio.base.instance_context import InstanceContext as InstanceContext
from twilio.base.instance_resource import InstanceResource as InstanceResource
from twilio.base.list_resource import ListResource as ListResource
from twilio.base.page import Page as Page

class PaymentList(ListResource):
    def __init__(self, version, account_sid, call_sid) -> None: ...
    def create(self, idempotency_key, status_callback, bank_account_type=..., charge_amount=..., currency=..., description=..., input=..., min_postal_code_length=..., parameter=..., payment_connector=..., payment_method=..., postal_code=..., security_code=..., timeout=..., token_type=..., valid_card_types=...): ...
    def get(self, sid): ...
    def __call__(self, sid): ...

class PaymentPage(Page):
    def __init__(self, version, response, solution) -> None: ...
    def get_instance(self, payload): ...

class PaymentContext(InstanceContext):
    def __init__(self, version, account_sid, call_sid, sid) -> None: ...
    def update(self, idempotency_key, status_callback, capture=..., status=...): ...

class PaymentInstance(InstanceResource):
    class PaymentMethod:
        CREDIT_CARD: str
        ACH_DEBIT: str
    class BankAccountType:
        CONSUMER_CHECKING: str
        CONSUMER_SAVINGS: str
        COMMERCIAL_CHECKING: str
    class TokenType:
        ONE_TIME: str
        REUSABLE: str
    class Capture:
        PAYMENT_CARD_NUMBER: str
        EXPIRATION_DATE: str
        SECURITY_CODE: str
        POSTAL_CODE: str
        BANK_ROUTING_NUMBER: str
        BANK_ACCOUNT_NUMBER: str
    class Status:
        COMPLETE: str
        CANCEL: str
    def __init__(self, version, payload, account_sid, call_sid, sid: Incomplete | None = ...) -> None: ...
    @property
    def account_sid(self): ...
    @property
    def call_sid(self): ...
    @property
    def sid(self): ...
    @property
    def date_created(self): ...
    @property
    def date_updated(self): ...
    @property
    def uri(self): ...
    def update(self, idempotency_key, status_callback, capture=..., status=...): ...
