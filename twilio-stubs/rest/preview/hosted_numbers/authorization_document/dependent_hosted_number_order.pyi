from _typeshed import Incomplete
from twilio.base import deserialize as deserialize, values as values
from twilio.base.instance_resource import InstanceResource as InstanceResource
from twilio.base.list_resource import ListResource as ListResource
from twilio.base.page import Page as Page

class DependentHostedNumberOrderList(ListResource):
    def __init__(self, version, signing_document_sid) -> None: ...
    def stream(self, status=..., phone_number=..., incoming_phone_number_sid=..., friendly_name=..., unique_name=..., limit: Incomplete | None = ..., page_size: Incomplete | None = ...): ...
    def list(self, status=..., phone_number=..., incoming_phone_number_sid=..., friendly_name=..., unique_name=..., limit: Incomplete | None = ..., page_size: Incomplete | None = ...): ...
    def page(self, status=..., phone_number=..., incoming_phone_number_sid=..., friendly_name=..., unique_name=..., page_token=..., page_number=..., page_size=...): ...
    def get_page(self, target_url): ...

class DependentHostedNumberOrderPage(Page):
    def __init__(self, version, response, solution) -> None: ...
    def get_instance(self, payload): ...

class DependentHostedNumberOrderInstance(InstanceResource):
    class Status:
        RECEIVED: str
        PENDING_VERIFICATION: str
        VERIFIED: str
        PENDING_LOA: str
        CARRIER_PROCESSING: str
        TESTING: str
        COMPLETED: str
        FAILED: str
        ACTION_REQUIRED: str
    class VerificationType:
        PHONE_CALL: str
        PHONE_BILL: str
    def __init__(self, version, payload, signing_document_sid) -> None: ...
    @property
    def sid(self): ...
    @property
    def account_sid(self): ...
    @property
    def incoming_phone_number_sid(self): ...
    @property
    def address_sid(self): ...
    @property
    def signing_document_sid(self): ...
    @property
    def phone_number(self): ...
    @property
    def capabilities(self): ...
    @property
    def friendly_name(self): ...
    @property
    def unique_name(self): ...
    @property
    def status(self): ...
    @property
    def failure_reason(self): ...
    @property
    def date_created(self): ...
    @property
    def date_updated(self): ...
    @property
    def verification_attempts(self): ...
    @property
    def email(self): ...
    @property
    def cc_emails(self): ...
    @property
    def verification_type(self): ...
    @property
    def verification_document_sid(self): ...
    @property
    def extension(self): ...
    @property
    def call_delay(self): ...
    @property
    def verification_code(self): ...
    @property
    def verification_call_sids(self): ...
