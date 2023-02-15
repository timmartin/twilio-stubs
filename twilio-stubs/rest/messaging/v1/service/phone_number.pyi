from _typeshed import Incomplete
from twilio.base import deserialize as deserialize, values as values
from twilio.base.instance_context import InstanceContext as InstanceContext
from twilio.base.instance_resource import InstanceResource as InstanceResource
from twilio.base.list_resource import ListResource as ListResource
from twilio.base.page import Page as Page

class PhoneNumberList(ListResource):
    def __init__(self, version, service_sid) -> None: ...
    def create(self, phone_number_sid): ...
    def stream(self, limit: Incomplete | None = ..., page_size: Incomplete | None = ...): ...
    def list(self, limit: Incomplete | None = ..., page_size: Incomplete | None = ...): ...
    def page(self, page_token=..., page_number=..., page_size=...): ...
    def get_page(self, target_url): ...
    def get(self, sid): ...
    def __call__(self, sid): ...

class PhoneNumberPage(Page):
    def __init__(self, version, response, solution) -> None: ...
    def get_instance(self, payload): ...

class PhoneNumberContext(InstanceContext):
    def __init__(self, version, service_sid, sid) -> None: ...
    def delete(self): ...
    def fetch(self): ...

class PhoneNumberInstance(InstanceResource):
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
    def phone_number(self): ...
    @property
    def country_code(self): ...
    @property
    def capabilities(self): ...
    @property
    def url(self): ...
    def delete(self): ...
    def fetch(self): ...
