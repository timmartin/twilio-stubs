from twilio.base import deserialize as deserialize, values as values
from twilio.base.instance_context import InstanceContext as InstanceContext
from twilio.base.instance_resource import InstanceResource as InstanceResource
from twilio.base.list_resource import ListResource as ListResource
from twilio.base.page import Page as Page
from typing import Any, Optional

class TaskChannelList(ListResource):
    def __init__(self, version: Any, workspace_sid: Any) -> None: ...
    def stream(self, limit: Optional[Any] = ..., page_size: Optional[Any] = ...): ...
    def list(self, limit: Optional[Any] = ..., page_size: Optional[Any] = ...): ...
    def page(self, page_token: Any = ..., page_number: Any = ..., page_size: Any = ...): ...
    def get_page(self, target_url: Any): ...
    def create(self, friendly_name: Any, unique_name: Any, channel_optimized_routing: Any = ...): ...
    def get(self, sid: Any): ...
    def __call__(self, sid: Any): ...

class TaskChannelPage(Page):
    def __init__(self, version: Any, response: Any, solution: Any) -> None: ...
    def get_instance(self, payload: Any): ...

class TaskChannelContext(InstanceContext):
    def __init__(self, version: Any, workspace_sid: Any, sid: Any) -> None: ...
    def fetch(self): ...
    def update(self, friendly_name: Any = ..., channel_optimized_routing: Any = ...): ...
    def delete(self): ...

class TaskChannelInstance(InstanceResource):
    def __init__(self, version: Any, payload: Any, workspace_sid: Any, sid: Optional[Any] = ...) -> None: ...
    @property
    def account_sid(self): ...
    @property
    def date_created(self): ...
    @property
    def date_updated(self): ...
    @property
    def friendly_name(self): ...
    @property
    def sid(self): ...
    @property
    def unique_name(self): ...
    @property
    def workspace_sid(self): ...
    @property
    def channel_optimized_routing(self): ...
    @property
    def url(self): ...
    @property
    def links(self): ...
    def fetch(self): ...
    def update(self, friendly_name: Any = ..., channel_optimized_routing: Any = ...): ...
    def delete(self): ...
