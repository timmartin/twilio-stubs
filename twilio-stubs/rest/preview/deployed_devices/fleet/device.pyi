from _typeshed import Incomplete
from twilio.base import deserialize as deserialize, values as values
from twilio.base.instance_context import InstanceContext as InstanceContext
from twilio.base.instance_resource import InstanceResource as InstanceResource
from twilio.base.list_resource import ListResource as ListResource
from twilio.base.page import Page as Page

class DeviceList(ListResource):
    def __init__(self, version, fleet_sid) -> None: ...
    def create(self, unique_name=..., friendly_name=..., identity=..., deployment_sid=..., enabled=...): ...
    def stream(self, deployment_sid=..., limit: Incomplete | None = ..., page_size: Incomplete | None = ...): ...
    def list(self, deployment_sid=..., limit: Incomplete | None = ..., page_size: Incomplete | None = ...): ...
    def page(self, deployment_sid=..., page_token=..., page_number=..., page_size=...): ...
    def get_page(self, target_url): ...
    def get(self, sid): ...
    def __call__(self, sid): ...

class DevicePage(Page):
    def __init__(self, version, response, solution) -> None: ...
    def get_instance(self, payload): ...

class DeviceContext(InstanceContext):
    def __init__(self, version, fleet_sid, sid) -> None: ...
    def fetch(self): ...
    def delete(self): ...
    def update(self, friendly_name=..., identity=..., deployment_sid=..., enabled=...): ...

class DeviceInstance(InstanceResource):
    def __init__(self, version, payload, fleet_sid, sid: Incomplete | None = ...) -> None: ...
    @property
    def sid(self): ...
    @property
    def url(self): ...
    @property
    def unique_name(self): ...
    @property
    def friendly_name(self): ...
    @property
    def fleet_sid(self): ...
    @property
    def enabled(self): ...
    @property
    def account_sid(self): ...
    @property
    def identity(self): ...
    @property
    def deployment_sid(self): ...
    @property
    def date_created(self): ...
    @property
    def date_updated(self): ...
    @property
    def date_authenticated(self): ...
    def fetch(self): ...
    def delete(self): ...
    def update(self, friendly_name=..., identity=..., deployment_sid=..., enabled=...): ...
