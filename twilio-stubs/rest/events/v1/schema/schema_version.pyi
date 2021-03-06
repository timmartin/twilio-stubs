from twilio.base import deserialize as deserialize, values as values
from twilio.base.instance_context import InstanceContext as InstanceContext
from twilio.base.instance_resource import InstanceResource as InstanceResource
from twilio.base.list_resource import ListResource as ListResource
from twilio.base.page import Page as Page
from typing import Any, Optional

class VersionList(ListResource):
    def __init__(self, version: Any, id: Any) -> None: ...
    def stream(self, limit: Optional[Any] = ..., page_size: Optional[Any] = ...): ...
    def list(self, limit: Optional[Any] = ..., page_size: Optional[Any] = ...): ...
    def page(self, page_token: Any = ..., page_number: Any = ..., page_size: Any = ...): ...
    def get_page(self, target_url: Any): ...
    def get(self, schema_version: Any): ...
    def __call__(self, schema_version: Any): ...

class VersionPage(Page):
    def __init__(self, version: Any, response: Any, solution: Any) -> None: ...
    def get_instance(self, payload: Any): ...

class VersionContext(InstanceContext):
    def __init__(self, version: Any, id: Any, schema_version: Any) -> None: ...
    def fetch(self): ...

class VersionInstance(InstanceResource):
    def __init__(self, version: Any, payload: Any, id: Any, schema_version: Optional[Any] = ...) -> None: ...
    @property
    def id(self): ...
    @property
    def schema_version(self): ...
    @property
    def date_created(self): ...
    @property
    def url(self): ...
    @property
    def raw(self): ...
    def fetch(self): ...
