from _typeshed import Incomplete
from twilio.base import deserialize as deserialize, values as values
from twilio.base.instance_context import InstanceContext as InstanceContext
from twilio.base.instance_resource import InstanceResource as InstanceResource
from twilio.base.list_resource import ListResource as ListResource
from twilio.base.page import Page as Page
from twilio.rest.api.v2010.account.recording.add_on_result.payload import PayloadList as PayloadList

class AddOnResultList(ListResource):
    def __init__(self, version, account_sid, reference_sid) -> None: ...
    def stream(self, limit: Incomplete | None = ..., page_size: Incomplete | None = ...): ...
    def list(self, limit: Incomplete | None = ..., page_size: Incomplete | None = ...): ...
    def page(self, page_token=..., page_number=..., page_size=...): ...
    def get_page(self, target_url): ...
    def get(self, sid): ...
    def __call__(self, sid): ...

class AddOnResultPage(Page):
    def __init__(self, version, response, solution) -> None: ...
    def get_instance(self, payload): ...

class AddOnResultContext(InstanceContext):
    def __init__(self, version, account_sid, reference_sid, sid) -> None: ...
    def fetch(self): ...
    def delete(self): ...
    @property
    def payloads(self): ...

class AddOnResultInstance(InstanceResource):
    class Status:
        CANCELED: str
        COMPLETED: str
        DELETED: str
        FAILED: str
        IN_PROGRESS: str
        INIT: str
        PROCESSING: str
        QUEUED: str
    def __init__(self, version, payload, account_sid, reference_sid, sid: Incomplete | None = ...) -> None: ...
    @property
    def sid(self): ...
    @property
    def account_sid(self): ...
    @property
    def status(self): ...
    @property
    def add_on_sid(self): ...
    @property
    def add_on_configuration_sid(self): ...
    @property
    def date_created(self): ...
    @property
    def date_updated(self): ...
    @property
    def date_completed(self): ...
    @property
    def reference_sid(self): ...
    @property
    def subresource_uris(self): ...
    def fetch(self): ...
    def delete(self): ...
    @property
    def payloads(self): ...
