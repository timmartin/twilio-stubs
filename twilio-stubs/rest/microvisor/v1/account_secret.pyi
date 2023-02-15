from _typeshed import Incomplete
from twilio.base import deserialize as deserialize, values as values
from twilio.base.instance_context import InstanceContext as InstanceContext
from twilio.base.instance_resource import InstanceResource as InstanceResource
from twilio.base.list_resource import ListResource as ListResource
from twilio.base.page import Page as Page

class AccountSecretList(ListResource):
    def __init__(self, version) -> None: ...
    def stream(self, limit: Incomplete | None = ..., page_size: Incomplete | None = ...): ...
    def list(self, limit: Incomplete | None = ..., page_size: Incomplete | None = ...): ...
    def page(self, page_token=..., page_number=..., page_size=...): ...
    def get_page(self, target_url): ...
    def create(self, key, value): ...
    def get(self, key): ...
    def __call__(self, key): ...

class AccountSecretPage(Page):
    def __init__(self, version, response, solution) -> None: ...
    def get_instance(self, payload): ...

class AccountSecretContext(InstanceContext):
    def __init__(self, version, key) -> None: ...
    def fetch(self): ...
    def delete(self): ...

class AccountSecretInstance(InstanceResource):
    def __init__(self, version, payload, key: Incomplete | None = ...) -> None: ...
    @property
    def key(self): ...
    @property
    def date_rotated(self): ...
    @property
    def url(self): ...
    def fetch(self): ...
    def delete(self): ...
