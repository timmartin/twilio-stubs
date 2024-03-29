from _typeshed import Incomplete
from twilio.base import deserialize as deserialize, serialize as serialize, values as values
from twilio.base.instance_context import InstanceContext as InstanceContext
from twilio.base.instance_resource import InstanceResource as InstanceResource
from twilio.base.list_resource import ListResource as ListResource
from twilio.base.page import Page as Page

class NotificationList(ListResource):
    def __init__(self, version, account_sid, call_sid) -> None: ...
    def stream(self, log=..., message_date_before=..., message_date=..., message_date_after=..., limit: Incomplete | None = ..., page_size: Incomplete | None = ...): ...
    def list(self, log=..., message_date_before=..., message_date=..., message_date_after=..., limit: Incomplete | None = ..., page_size: Incomplete | None = ...): ...
    def page(self, log=..., message_date_before=..., message_date=..., message_date_after=..., page_token=..., page_number=..., page_size=...): ...
    def get_page(self, target_url): ...
    def get(self, sid): ...
    def __call__(self, sid): ...

class NotificationPage(Page):
    def __init__(self, version, response, solution) -> None: ...
    def get_instance(self, payload): ...

class NotificationContext(InstanceContext):
    def __init__(self, version, account_sid, call_sid, sid) -> None: ...
    def fetch(self): ...

class NotificationInstance(InstanceResource):
    def __init__(self, version, payload, account_sid, call_sid, sid: Incomplete | None = ...) -> None: ...
    @property
    def account_sid(self): ...
    @property
    def api_version(self): ...
    @property
    def call_sid(self): ...
    @property
    def date_created(self): ...
    @property
    def date_updated(self): ...
    @property
    def error_code(self): ...
    @property
    def log(self): ...
    @property
    def message_date(self): ...
    @property
    def message_text(self): ...
    @property
    def more_info(self): ...
    @property
    def request_method(self): ...
    @property
    def request_url(self): ...
    @property
    def request_variables(self): ...
    @property
    def response_body(self): ...
    @property
    def response_headers(self): ...
    @property
    def sid(self): ...
    @property
    def uri(self): ...
    def fetch(self): ...
