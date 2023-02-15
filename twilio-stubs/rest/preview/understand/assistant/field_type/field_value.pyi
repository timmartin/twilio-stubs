from _typeshed import Incomplete
from twilio.base import deserialize as deserialize, values as values
from twilio.base.instance_context import InstanceContext as InstanceContext
from twilio.base.instance_resource import InstanceResource as InstanceResource
from twilio.base.list_resource import ListResource as ListResource
from twilio.base.page import Page as Page

class FieldValueList(ListResource):
    def __init__(self, version, assistant_sid, field_type_sid) -> None: ...
    def stream(self, language=..., limit: Incomplete | None = ..., page_size: Incomplete | None = ...): ...
    def list(self, language=..., limit: Incomplete | None = ..., page_size: Incomplete | None = ...): ...
    def page(self, language=..., page_token=..., page_number=..., page_size=...): ...
    def get_page(self, target_url): ...
    def create(self, language, value, synonym_of=...): ...
    def get(self, sid): ...
    def __call__(self, sid): ...

class FieldValuePage(Page):
    def __init__(self, version, response, solution) -> None: ...
    def get_instance(self, payload): ...

class FieldValueContext(InstanceContext):
    def __init__(self, version, assistant_sid, field_type_sid, sid) -> None: ...
    def fetch(self): ...
    def delete(self): ...

class FieldValueInstance(InstanceResource):
    def __init__(self, version, payload, assistant_sid, field_type_sid, sid: Incomplete | None = ...) -> None: ...
    @property
    def account_sid(self): ...
    @property
    def date_created(self): ...
    @property
    def date_updated(self): ...
    @property
    def field_type_sid(self): ...
    @property
    def language(self): ...
    @property
    def assistant_sid(self): ...
    @property
    def sid(self): ...
    @property
    def value(self): ...
    @property
    def url(self): ...
    @property
    def synonym_of(self): ...
    def fetch(self): ...
    def delete(self): ...
