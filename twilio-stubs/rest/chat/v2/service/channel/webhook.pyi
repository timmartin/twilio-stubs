from twilio.base import deserialize as deserialize, serialize as serialize, values as values
from twilio.base.instance_context import InstanceContext as InstanceContext
from twilio.base.instance_resource import InstanceResource as InstanceResource
from twilio.base.list_resource import ListResource as ListResource
from twilio.base.page import Page as Page
from typing import Any, Optional

class WebhookList(ListResource):
    def __init__(self, version: Any, service_sid: Any, channel_sid: Any) -> None: ...
    def stream(self, limit: Optional[Any] = ..., page_size: Optional[Any] = ...): ...
    def list(self, limit: Optional[Any] = ..., page_size: Optional[Any] = ...): ...
    def page(self, page_token: Any = ..., page_number: Any = ..., page_size: Any = ...): ...
    def get_page(self, target_url: Any): ...
    def create(self, type: Any, configuration_url: Any = ..., configuration_method: Any = ..., configuration_filters: Any = ..., configuration_triggers: Any = ..., configuration_flow_sid: Any = ..., configuration_retry_count: Any = ...): ...
    def get(self, sid: Any): ...
    def __call__(self, sid: Any): ...

class WebhookPage(Page):
    def __init__(self, version: Any, response: Any, solution: Any) -> None: ...
    def get_instance(self, payload: Any): ...

class WebhookContext(InstanceContext):
    def __init__(self, version: Any, service_sid: Any, channel_sid: Any, sid: Any) -> None: ...
    def fetch(self): ...
    def update(self, configuration_url: Any = ..., configuration_method: Any = ..., configuration_filters: Any = ..., configuration_triggers: Any = ..., configuration_flow_sid: Any = ..., configuration_retry_count: Any = ...): ...
    def delete(self): ...

class WebhookInstance(InstanceResource):
    class Type:
        WEBHOOK: str = ...
        TRIGGER: str = ...
        STUDIO: str = ...
    class Method:
        GET: str = ...
        POST: str = ...
    def __init__(self, version: Any, payload: Any, service_sid: Any, channel_sid: Any, sid: Optional[Any] = ...) -> None: ...
    @property
    def sid(self): ...
    @property
    def account_sid(self): ...
    @property
    def service_sid(self): ...
    @property
    def channel_sid(self): ...
    @property
    def type(self): ...
    @property
    def url(self): ...
    @property
    def configuration(self): ...
    @property
    def date_created(self): ...
    @property
    def date_updated(self): ...
    def fetch(self): ...
    def update(self, configuration_url: Any = ..., configuration_method: Any = ..., configuration_filters: Any = ..., configuration_triggers: Any = ..., configuration_flow_sid: Any = ..., configuration_retry_count: Any = ...): ...
    def delete(self): ...
