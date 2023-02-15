from _typeshed import Incomplete
from twilio.base import deserialize as deserialize, serialize as serialize, values as values
from twilio.base.instance_context import InstanceContext as InstanceContext
from twilio.base.instance_resource import InstanceResource as InstanceResource
from twilio.base.list_resource import ListResource as ListResource
from twilio.base.page import Page as Page

class LogList(ListResource):
    def __init__(self, version, service_sid, environment_sid) -> None: ...
    def stream(self, function_sid=..., start_date=..., end_date=..., limit: Incomplete | None = ..., page_size: Incomplete | None = ...): ...
    def list(self, function_sid=..., start_date=..., end_date=..., limit: Incomplete | None = ..., page_size: Incomplete | None = ...): ...
    def page(self, function_sid=..., start_date=..., end_date=..., page_token=..., page_number=..., page_size=...): ...
    def get_page(self, target_url): ...
    def get(self, sid): ...
    def __call__(self, sid): ...

class LogPage(Page):
    def __init__(self, version, response, solution) -> None: ...
    def get_instance(self, payload): ...

class LogContext(InstanceContext):
    def __init__(self, version, service_sid, environment_sid, sid) -> None: ...
    def fetch(self): ...

class LogInstance(InstanceResource):
    class Level:
        INFO: str
        WARN: str
        ERROR: str
    def __init__(self, version, payload, service_sid, environment_sid, sid: Incomplete | None = ...) -> None: ...
    @property
    def sid(self): ...
    @property
    def account_sid(self): ...
    @property
    def service_sid(self): ...
    @property
    def environment_sid(self): ...
    @property
    def build_sid(self): ...
    @property
    def deployment_sid(self): ...
    @property
    def function_sid(self): ...
    @property
    def request_sid(self): ...
    @property
    def level(self): ...
    @property
    def message(self): ...
    @property
    def date_created(self): ...
    @property
    def url(self): ...
    def fetch(self): ...
