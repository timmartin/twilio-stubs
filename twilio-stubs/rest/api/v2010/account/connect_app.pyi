from twilio.base import serialize as serialize, values as values
from twilio.base.instance_context import InstanceContext as InstanceContext
from twilio.base.instance_resource import InstanceResource as InstanceResource
from twilio.base.list_resource import ListResource as ListResource
from twilio.base.page import Page as Page
from typing import Any, Optional

class ConnectAppList(ListResource):
    def __init__(self, version: Any, account_sid: Any) -> None: ...
    def stream(self, limit: Optional[Any] = ..., page_size: Optional[Any] = ...): ...
    def list(self, limit: Optional[Any] = ..., page_size: Optional[Any] = ...): ...
    def page(self, page_token: Any = ..., page_number: Any = ..., page_size: Any = ...): ...
    def get_page(self, target_url: Any): ...
    def get(self, sid: Any): ...
    def __call__(self, sid: Any): ...

class ConnectAppPage(Page):
    def __init__(self, version: Any, response: Any, solution: Any) -> None: ...
    def get_instance(self, payload: Any): ...

class ConnectAppContext(InstanceContext):
    def __init__(self, version: Any, account_sid: Any, sid: Any) -> None: ...
    def fetch(self): ...
    def update(self, authorize_redirect_url: Any = ..., company_name: Any = ..., deauthorize_callback_method: Any = ..., deauthorize_callback_url: Any = ..., description: Any = ..., friendly_name: Any = ..., homepage_url: Any = ..., permissions: Any = ...): ...
    def delete(self): ...

class ConnectAppInstance(InstanceResource):
    class Permission:
        GET_ALL: str = ...
        POST_ALL: str = ...
    def __init__(self, version: Any, payload: Any, account_sid: Any, sid: Optional[Any] = ...) -> None: ...
    @property
    def account_sid(self): ...
    @property
    def authorize_redirect_url(self): ...
    @property
    def company_name(self): ...
    @property
    def deauthorize_callback_method(self): ...
    @property
    def deauthorize_callback_url(self): ...
    @property
    def description(self): ...
    @property
    def friendly_name(self): ...
    @property
    def homepage_url(self): ...
    @property
    def permissions(self): ...
    @property
    def sid(self): ...
    @property
    def uri(self): ...
    def fetch(self): ...
    def update(self, authorize_redirect_url: Any = ..., company_name: Any = ..., deauthorize_callback_method: Any = ..., deauthorize_callback_url: Any = ..., description: Any = ..., friendly_name: Any = ..., homepage_url: Any = ..., permissions: Any = ...): ...
    def delete(self): ...
