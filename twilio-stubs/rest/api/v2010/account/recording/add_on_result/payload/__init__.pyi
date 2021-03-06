from twilio.base import deserialize as deserialize, values as values
from twilio.base.instance_context import InstanceContext as InstanceContext
from twilio.base.instance_resource import InstanceResource as InstanceResource
from twilio.base.list_resource import ListResource as ListResource
from twilio.base.page import Page as Page
from typing import Any, Optional

class PayloadList(ListResource):
    def __init__(self, version: Any, account_sid: Any, reference_sid: Any, add_on_result_sid: Any) -> None: ...
    def stream(self, limit: Optional[Any] = ..., page_size: Optional[Any] = ...): ...
    def list(self, limit: Optional[Any] = ..., page_size: Optional[Any] = ...): ...
    def page(self, page_token: Any = ..., page_number: Any = ..., page_size: Any = ...): ...
    def get_page(self, target_url: Any): ...
    def get(self, sid: Any): ...
    def __call__(self, sid: Any): ...

class PayloadPage(Page):
    def __init__(self, version: Any, response: Any, solution: Any) -> None: ...
    def get_instance(self, payload: Any): ...

class PayloadContext(InstanceContext):
    def __init__(self, version: Any, account_sid: Any, reference_sid: Any, add_on_result_sid: Any, sid: Any) -> None: ...
    def fetch(self): ...
    def delete(self): ...

class PayloadInstance(InstanceResource):
    def __init__(self, version: Any, payload: Any, account_sid: Any, reference_sid: Any, add_on_result_sid: Any, sid: Optional[Any] = ...) -> None: ...
    @property
    def sid(self): ...
    @property
    def add_on_result_sid(self): ...
    @property
    def account_sid(self): ...
    @property
    def label(self): ...
    @property
    def add_on_sid(self): ...
    @property
    def add_on_configuration_sid(self): ...
    @property
    def content_type(self): ...
    @property
    def date_created(self): ...
    @property
    def date_updated(self): ...
    @property
    def reference_sid(self): ...
    @property
    def subresource_uris(self): ...
    def fetch(self): ...
    def delete(self): ...
