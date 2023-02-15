from _typeshed import Incomplete
from twilio.base import deserialize as deserialize, values as values
from twilio.base.instance_context import InstanceContext as InstanceContext
from twilio.base.instance_resource import InstanceResource as InstanceResource
from twilio.base.list_resource import ListResource as ListResource
from twilio.base.page import Page as Page

class MessagingConfigurationList(ListResource):
    def __init__(self, version, service_sid) -> None: ...
    def create(self, country, messaging_service_sid): ...
    def stream(self, limit: Incomplete | None = ..., page_size: Incomplete | None = ...): ...
    def list(self, limit: Incomplete | None = ..., page_size: Incomplete | None = ...): ...
    def page(self, page_token=..., page_number=..., page_size=...): ...
    def get_page(self, target_url): ...
    def get(self, country): ...
    def __call__(self, country): ...

class MessagingConfigurationPage(Page):
    def __init__(self, version, response, solution) -> None: ...
    def get_instance(self, payload): ...

class MessagingConfigurationContext(InstanceContext):
    def __init__(self, version, service_sid, country) -> None: ...
    def update(self, messaging_service_sid): ...
    def fetch(self): ...
    def delete(self): ...

class MessagingConfigurationInstance(InstanceResource):
    def __init__(self, version, payload, service_sid, country: Incomplete | None = ...) -> None: ...
    @property
    def account_sid(self): ...
    @property
    def service_sid(self): ...
    @property
    def country(self): ...
    @property
    def messaging_service_sid(self): ...
    @property
    def date_created(self): ...
    @property
    def date_updated(self): ...
    @property
    def url(self): ...
    def update(self, messaging_service_sid): ...
    def fetch(self): ...
    def delete(self): ...
