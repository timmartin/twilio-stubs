from twilio.base import deserialize as deserialize, values as values
from twilio.base.instance_context import InstanceContext as InstanceContext
from twilio.base.instance_resource import InstanceResource as InstanceResource
from twilio.base.list_resource import ListResource as ListResource
from twilio.base.page import Page as Page
from typing import Any, Optional

class ModelBuildList(ListResource):
    def __init__(self, version: Any, assistant_sid: Any) -> None: ...
    def stream(self, limit: Optional[Any] = ..., page_size: Optional[Any] = ...): ...
    def list(self, limit: Optional[Any] = ..., page_size: Optional[Any] = ...): ...
    def page(self, page_token: Any = ..., page_number: Any = ..., page_size: Any = ...): ...
    def get_page(self, target_url: Any): ...
    def create(self, status_callback: Any = ..., unique_name: Any = ...): ...
    def get(self, sid: Any): ...
    def __call__(self, sid: Any): ...

class ModelBuildPage(Page):
    def __init__(self, version: Any, response: Any, solution: Any) -> None: ...
    def get_instance(self, payload: Any): ...

class ModelBuildContext(InstanceContext):
    def __init__(self, version: Any, assistant_sid: Any, sid: Any) -> None: ...
    def fetch(self): ...
    def update(self, unique_name: Any = ...): ...
    def delete(self): ...

class ModelBuildInstance(InstanceResource):
    class Status:
        ENQUEUED: str = ...
        BUILDING: str = ...
        COMPLETED: str = ...
        FAILED: str = ...
        CANCELED: str = ...
    def __init__(self, version: Any, payload: Any, assistant_sid: Any, sid: Optional[Any] = ...) -> None: ...
    @property
    def account_sid(self): ...
    @property
    def date_created(self): ...
    @property
    def date_updated(self): ...
    @property
    def assistant_sid(self): ...
    @property
    def sid(self): ...
    @property
    def status(self): ...
    @property
    def unique_name(self): ...
    @property
    def url(self): ...
    @property
    def build_duration(self): ...
    @property
    def error_code(self): ...
    def fetch(self): ...
    def update(self, unique_name: Any = ...): ...
    def delete(self): ...
