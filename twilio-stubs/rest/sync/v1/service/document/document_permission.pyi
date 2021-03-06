from twilio.base import values as values
from twilio.base.instance_context import InstanceContext as InstanceContext
from twilio.base.instance_resource import InstanceResource as InstanceResource
from twilio.base.list_resource import ListResource as ListResource
from twilio.base.page import Page as Page
from typing import Any, Optional

class DocumentPermissionList(ListResource):
    def __init__(self, version: Any, service_sid: Any, document_sid: Any) -> None: ...
    def stream(self, limit: Optional[Any] = ..., page_size: Optional[Any] = ...): ...
    def list(self, limit: Optional[Any] = ..., page_size: Optional[Any] = ...): ...
    def page(self, page_token: Any = ..., page_number: Any = ..., page_size: Any = ...): ...
    def get_page(self, target_url: Any): ...
    def get(self, identity: Any): ...
    def __call__(self, identity: Any): ...

class DocumentPermissionPage(Page):
    def __init__(self, version: Any, response: Any, solution: Any) -> None: ...
    def get_instance(self, payload: Any): ...

class DocumentPermissionContext(InstanceContext):
    def __init__(self, version: Any, service_sid: Any, document_sid: Any, identity: Any) -> None: ...
    def fetch(self): ...
    def delete(self): ...
    def update(self, read: Any, write: Any, manage: Any): ...

class DocumentPermissionInstance(InstanceResource):
    def __init__(self, version: Any, payload: Any, service_sid: Any, document_sid: Any, identity: Optional[Any] = ...) -> None: ...
    @property
    def account_sid(self): ...
    @property
    def service_sid(self): ...
    @property
    def document_sid(self): ...
    @property
    def identity(self): ...
    @property
    def read(self): ...
    @property
    def write(self): ...
    @property
    def manage(self): ...
    @property
    def url(self): ...
    def fetch(self): ...
    def delete(self): ...
    def update(self, read: Any, write: Any, manage: Any): ...
