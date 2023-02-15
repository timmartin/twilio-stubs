from _typeshed import Incomplete
from twilio.base import deserialize as deserialize, values as values
from twilio.base.instance_context import InstanceContext as InstanceContext
from twilio.base.instance_resource import InstanceResource as InstanceResource
from twilio.base.list_resource import ListResource as ListResource
from twilio.base.page import Page as Page

class CredentialList(ListResource):
    def __init__(self, version) -> None: ...
    def stream(self, limit: Incomplete | None = ..., page_size: Incomplete | None = ...): ...
    def list(self, limit: Incomplete | None = ..., page_size: Incomplete | None = ...): ...
    def page(self, page_token=..., page_number=..., page_size=...): ...
    def get_page(self, target_url): ...
    def create(self, type, friendly_name=..., certificate=..., private_key=..., sandbox=..., api_key=..., secret=...): ...
    def get(self, sid): ...
    def __call__(self, sid): ...

class CredentialPage(Page):
    def __init__(self, version, response, solution) -> None: ...
    def get_instance(self, payload): ...

class CredentialContext(InstanceContext):
    def __init__(self, version, sid) -> None: ...
    def fetch(self): ...
    def update(self, friendly_name=..., certificate=..., private_key=..., sandbox=..., api_key=..., secret=...): ...
    def delete(self): ...

class CredentialInstance(InstanceResource):
    class PushService:
        GCM: str
        APN: str
        FCM: str
    def __init__(self, version, payload, sid: Incomplete | None = ...) -> None: ...
    @property
    def sid(self): ...
    @property
    def account_sid(self): ...
    @property
    def friendly_name(self): ...
    @property
    def type(self): ...
    @property
    def sandbox(self): ...
    @property
    def date_created(self): ...
    @property
    def date_updated(self): ...
    @property
    def url(self): ...
    def fetch(self): ...
    def update(self, friendly_name=..., certificate=..., private_key=..., sandbox=..., api_key=..., secret=...): ...
    def delete(self): ...
