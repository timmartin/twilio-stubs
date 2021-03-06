from twilio.base import deserialize as deserialize, values as values
from twilio.base.instance_context import InstanceContext as InstanceContext
from twilio.base.instance_resource import InstanceResource as InstanceResource
from twilio.base.list_resource import ListResource as ListResource
from twilio.base.page import Page as Page
from typing import Any, Optional

class CommandList(ListResource):
    def __init__(self, version: Any) -> None: ...
    def stream(self, device: Any = ..., sim: Any = ..., status: Any = ..., direction: Any = ..., limit: Optional[Any] = ..., page_size: Optional[Any] = ...): ...
    def list(self, device: Any = ..., sim: Any = ..., status: Any = ..., direction: Any = ..., limit: Optional[Any] = ..., page_size: Optional[Any] = ...): ...
    def page(self, device: Any = ..., sim: Any = ..., status: Any = ..., direction: Any = ..., page_token: Any = ..., page_number: Any = ..., page_size: Any = ...): ...
    def get_page(self, target_url: Any): ...
    def create(self, command: Any, device: Any = ..., sim: Any = ..., callback_method: Any = ..., callback_url: Any = ..., command_mode: Any = ..., include_sid: Any = ...): ...
    def get(self, sid: Any): ...
    def __call__(self, sid: Any): ...

class CommandPage(Page):
    def __init__(self, version: Any, response: Any, solution: Any) -> None: ...
    def get_instance(self, payload: Any): ...

class CommandContext(InstanceContext):
    def __init__(self, version: Any, sid: Any) -> None: ...
    def fetch(self): ...

class CommandInstance(InstanceResource):
    def __init__(self, version: Any, payload: Any, sid: Optional[Any] = ...) -> None: ...
    @property
    def sid(self): ...
    @property
    def account_sid(self): ...
    @property
    def device_sid(self): ...
    @property
    def sim_sid(self): ...
    @property
    def command(self): ...
    @property
    def command_mode(self): ...
    @property
    def status(self): ...
    @property
    def direction(self): ...
    @property
    def date_created(self): ...
    @property
    def date_updated(self): ...
    @property
    def url(self): ...
    def fetch(self): ...
