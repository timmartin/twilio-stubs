from _typeshed import Incomplete
from twilio.base import deserialize as deserialize, serialize as serialize, values as values
from twilio.base.instance_context import InstanceContext as InstanceContext
from twilio.base.instance_resource import InstanceResource as InstanceResource
from twilio.base.list_resource import ListResource as ListResource
from twilio.base.page import Page as Page

class BindingList(ListResource):
    def __init__(self, version, service_sid) -> None: ...
    def stream(self, binding_type=..., identity=..., limit: Incomplete | None = ..., page_size: Incomplete | None = ...): ...
    def list(self, binding_type=..., identity=..., limit: Incomplete | None = ..., page_size: Incomplete | None = ...): ...
    def page(self, binding_type=..., identity=..., page_token=..., page_number=..., page_size=...): ...
    def get_page(self, target_url): ...
    def get(self, sid): ...
    def __call__(self, sid): ...

class BindingPage(Page):
    def __init__(self, version, response, solution) -> None: ...
    def get_instance(self, payload): ...

class BindingContext(InstanceContext):
    def __init__(self, version, service_sid, sid) -> None: ...
    def fetch(self): ...
    def delete(self): ...

class BindingInstance(InstanceResource):
    class BindingType:
        GCM: str
        APN: str
        FCM: str
    def __init__(self, version, payload, service_sid, sid: Incomplete | None = ...) -> None: ...
    @property
    def sid(self): ...
    @property
    def account_sid(self): ...
    @property
    def service_sid(self): ...
    @property
    def date_created(self): ...
    @property
    def date_updated(self): ...
    @property
    def endpoint(self): ...
    @property
    def identity(self): ...
    @property
    def credential_sid(self): ...
    @property
    def binding_type(self): ...
    @property
    def message_types(self): ...
    @property
    def url(self): ...
    @property
    def links(self): ...
    def fetch(self): ...
    def delete(self): ...
