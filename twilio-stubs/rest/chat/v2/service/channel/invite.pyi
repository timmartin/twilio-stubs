from _typeshed import Incomplete
from twilio.base import deserialize as deserialize, serialize as serialize, values as values
from twilio.base.instance_context import InstanceContext as InstanceContext
from twilio.base.instance_resource import InstanceResource as InstanceResource
from twilio.base.list_resource import ListResource as ListResource
from twilio.base.page import Page as Page

class InviteList(ListResource):
    def __init__(self, version, service_sid, channel_sid) -> None: ...
    def create(self, identity, role_sid=...): ...
    def stream(self, identity=..., limit: Incomplete | None = ..., page_size: Incomplete | None = ...): ...
    def list(self, identity=..., limit: Incomplete | None = ..., page_size: Incomplete | None = ...): ...
    def page(self, identity=..., page_token=..., page_number=..., page_size=...): ...
    def get_page(self, target_url): ...
    def get(self, sid): ...
    def __call__(self, sid): ...

class InvitePage(Page):
    def __init__(self, version, response, solution) -> None: ...
    def get_instance(self, payload): ...

class InviteContext(InstanceContext):
    def __init__(self, version, service_sid, channel_sid, sid) -> None: ...
    def fetch(self): ...
    def delete(self): ...

class InviteInstance(InstanceResource):
    def __init__(self, version, payload, service_sid, channel_sid, sid: Incomplete | None = ...) -> None: ...
    @property
    def sid(self): ...
    @property
    def account_sid(self): ...
    @property
    def channel_sid(self): ...
    @property
    def service_sid(self): ...
    @property
    def identity(self): ...
    @property
    def date_created(self): ...
    @property
    def date_updated(self): ...
    @property
    def role_sid(self): ...
    @property
    def created_by(self): ...
    @property
    def url(self): ...
    def fetch(self): ...
    def delete(self): ...
