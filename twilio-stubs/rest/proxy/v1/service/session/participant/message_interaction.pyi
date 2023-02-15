from _typeshed import Incomplete
from twilio.base import deserialize as deserialize, serialize as serialize, values as values
from twilio.base.instance_context import InstanceContext as InstanceContext
from twilio.base.instance_resource import InstanceResource as InstanceResource
from twilio.base.list_resource import ListResource as ListResource
from twilio.base.page import Page as Page

class MessageInteractionList(ListResource):
    def __init__(self, version, service_sid, session_sid, participant_sid) -> None: ...
    def create(self, body=..., media_url=...): ...
    def stream(self, limit: Incomplete | None = ..., page_size: Incomplete | None = ...): ...
    def list(self, limit: Incomplete | None = ..., page_size: Incomplete | None = ...): ...
    def page(self, page_token=..., page_number=..., page_size=...): ...
    def get_page(self, target_url): ...
    def get(self, sid): ...
    def __call__(self, sid): ...

class MessageInteractionPage(Page):
    def __init__(self, version, response, solution) -> None: ...
    def get_instance(self, payload): ...

class MessageInteractionContext(InstanceContext):
    def __init__(self, version, service_sid, session_sid, participant_sid, sid) -> None: ...
    def fetch(self): ...

class MessageInteractionInstance(InstanceResource):
    class Type:
        MESSAGE: str
        VOICE: str
        UNKNOWN: str
    class ResourceStatus:
        ACCEPTED: str
        ANSWERED: str
        BUSY: str
        CANCELED: str
        COMPLETED: str
        DELETED: str
        DELIVERED: str
        DELIVERY_UNKNOWN: str
        FAILED: str
        IN_PROGRESS: str
        INITIATED: str
        NO_ANSWER: str
        QUEUED: str
        RECEIVED: str
        RECEIVING: str
        RINGING: str
        SCHEDULED: str
        SENDING: str
        SENT: str
        UNDELIVERED: str
        UNKNOWN: str
    def __init__(self, version, payload, service_sid, session_sid, participant_sid, sid: Incomplete | None = ...) -> None: ...
    @property
    def sid(self): ...
    @property
    def session_sid(self): ...
    @property
    def service_sid(self): ...
    @property
    def account_sid(self): ...
    @property
    def data(self): ...
    @property
    def type(self): ...
    @property
    def participant_sid(self): ...
    @property
    def inbound_participant_sid(self): ...
    @property
    def inbound_resource_sid(self): ...
    @property
    def inbound_resource_status(self): ...
    @property
    def inbound_resource_type(self): ...
    @property
    def inbound_resource_url(self): ...
    @property
    def outbound_participant_sid(self): ...
    @property
    def outbound_resource_sid(self): ...
    @property
    def outbound_resource_status(self): ...
    @property
    def outbound_resource_type(self): ...
    @property
    def outbound_resource_url(self): ...
    @property
    def date_created(self): ...
    @property
    def date_updated(self): ...
    @property
    def url(self): ...
    def fetch(self): ...
