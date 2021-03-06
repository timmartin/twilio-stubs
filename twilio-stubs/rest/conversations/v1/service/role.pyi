from twilio.base import deserialize as deserialize, serialize as serialize, values as values
from twilio.base.instance_context import InstanceContext as InstanceContext
from twilio.base.instance_resource import InstanceResource as InstanceResource
from twilio.base.list_resource import ListResource as ListResource
from twilio.base.page import Page as Page
from typing import Any, Optional

class RoleList(ListResource):
    def __init__(self, version: Any, chat_service_sid: Any) -> None: ...
    def create(self, friendly_name: Any, type: Any, permission: Any): ...
    def stream(self, limit: Optional[Any] = ..., page_size: Optional[Any] = ...): ...
    def list(self, limit: Optional[Any] = ..., page_size: Optional[Any] = ...): ...
    def page(self, page_token: Any = ..., page_number: Any = ..., page_size: Any = ...): ...
    def get_page(self, target_url: Any): ...
    def get(self, sid: Any): ...
    def __call__(self, sid: Any): ...

class RolePage(Page):
    def __init__(self, version: Any, response: Any, solution: Any) -> None: ...
    def get_instance(self, payload: Any): ...

class RoleContext(InstanceContext):
    def __init__(self, version: Any, chat_service_sid: Any, sid: Any) -> None: ...
    def update(self, permission: Any): ...
    def delete(self): ...
    def fetch(self): ...

class RoleInstance(InstanceResource):
    class RoleType:
        CONVERSATION: str = ...
        SERVICE: str = ...
    def __init__(self, version: Any, payload: Any, chat_service_sid: Any, sid: Optional[Any] = ...) -> None: ...
    @property
    def sid(self): ...
    @property
    def account_sid(self): ...
    @property
    def chat_service_sid(self): ...
    @property
    def friendly_name(self): ...
    @property
    def type(self): ...
    @property
    def permissions(self): ...
    @property
    def date_created(self): ...
    @property
    def date_updated(self): ...
    @property
    def url(self): ...
    def update(self, permission: Any): ...
    def delete(self): ...
    def fetch(self): ...
