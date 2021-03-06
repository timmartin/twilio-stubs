from twilio.base import deserialize as deserialize, values as values
from twilio.base.instance_context import InstanceContext as InstanceContext
from twilio.base.instance_resource import InstanceResource as InstanceResource
from twilio.base.list_resource import ListResource as ListResource
from twilio.base.page import Page as Page
from typing import Any, Optional

class BucketList(ListResource):
    def __init__(self, version: Any, service_sid: Any, rate_limit_sid: Any) -> None: ...
    def create(self, max: Any, interval: Any): ...
    def stream(self, limit: Optional[Any] = ..., page_size: Optional[Any] = ...): ...
    def list(self, limit: Optional[Any] = ..., page_size: Optional[Any] = ...): ...
    def page(self, page_token: Any = ..., page_number: Any = ..., page_size: Any = ...): ...
    def get_page(self, target_url: Any): ...
    def get(self, sid: Any): ...
    def __call__(self, sid: Any): ...

class BucketPage(Page):
    def __init__(self, version: Any, response: Any, solution: Any) -> None: ...
    def get_instance(self, payload: Any): ...

class BucketContext(InstanceContext):
    def __init__(self, version: Any, service_sid: Any, rate_limit_sid: Any, sid: Any) -> None: ...
    def update(self, max: Any = ..., interval: Any = ...): ...
    def fetch(self): ...
    def delete(self): ...

class BucketInstance(InstanceResource):
    def __init__(self, version: Any, payload: Any, service_sid: Any, rate_limit_sid: Any, sid: Optional[Any] = ...) -> None: ...
    @property
    def sid(self): ...
    @property
    def rate_limit_sid(self): ...
    @property
    def service_sid(self): ...
    @property
    def account_sid(self): ...
    @property
    def max(self): ...
    @property
    def interval(self): ...
    @property
    def date_created(self): ...
    @property
    def date_updated(self): ...
    @property
    def url(self): ...
    def update(self, max: Any = ..., interval: Any = ...): ...
    def fetch(self): ...
    def delete(self): ...
