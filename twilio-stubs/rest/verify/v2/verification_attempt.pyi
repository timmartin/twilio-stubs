from _typeshed import Incomplete
from twilio.base import deserialize as deserialize, serialize as serialize, values as values
from twilio.base.instance_context import InstanceContext as InstanceContext
from twilio.base.instance_resource import InstanceResource as InstanceResource
from twilio.base.list_resource import ListResource as ListResource
from twilio.base.page import Page as Page

class VerificationAttemptList(ListResource):
    def __init__(self, version) -> None: ...
    def stream(self, date_created_after=..., date_created_before=..., channel_data_to=..., country=..., channel=..., verify_service_sid=..., verification_sid=..., status=..., limit: Incomplete | None = ..., page_size: Incomplete | None = ...): ...
    def list(self, date_created_after=..., date_created_before=..., channel_data_to=..., country=..., channel=..., verify_service_sid=..., verification_sid=..., status=..., limit: Incomplete | None = ..., page_size: Incomplete | None = ...): ...
    def page(self, date_created_after=..., date_created_before=..., channel_data_to=..., country=..., channel=..., verify_service_sid=..., verification_sid=..., status=..., page_token=..., page_number=..., page_size=...): ...
    def get_page(self, target_url): ...
    def get(self, sid): ...
    def __call__(self, sid): ...

class VerificationAttemptPage(Page):
    def __init__(self, version, response, solution) -> None: ...
    def get_instance(self, payload): ...

class VerificationAttemptContext(InstanceContext):
    def __init__(self, version, sid) -> None: ...
    def fetch(self): ...

class VerificationAttemptInstance(InstanceResource):
    class Channels:
        SMS: str
        CALL: str
        EMAIL: str
        WHATSAPP: str
    class CallStatus:
        QUEUED: str
        IN_PROGRESS: str
        COMPLETED: str
        BUSY: str
        FAILED: str
        NO_ANSWER: str
        RINGING: str
        CANCELED: str
    class MessageStatus:
        QUEUED: str
        SENDING: str
        SENT: str
        FAILED: str
        DELIVERED: str
        UNDELIVERED: str
        RECEIVING: str
        RECEIVED: str
        ACCEPTED: str
        SCHEDULED: str
        READ: str
        PARTIALLY_DELIVERED: str
        CANCELED: str
    class ConversionStatus:
        CONVERTED: str
        UNCONVERTED: str
    class AttemptStatus:
        CONFIRMED: str
        UNCONFIRMED: str
        EXPIRED: str
    def __init__(self, version, payload, sid: Incomplete | None = ...) -> None: ...
    @property
    def sid(self): ...
    @property
    def account_sid(self): ...
    @property
    def service_sid(self): ...
    @property
    def verification_sid(self): ...
    @property
    def date_created(self): ...
    @property
    def date_updated(self): ...
    @property
    def conversion_status(self): ...
    @property
    def channel(self): ...
    @property
    def price(self): ...
    @property
    def channel_data(self): ...
    @property
    def url(self): ...
    def fetch(self): ...
