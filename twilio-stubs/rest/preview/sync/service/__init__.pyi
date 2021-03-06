from twilio.base import deserialize as deserialize, values as values
from twilio.base.instance_context import InstanceContext as InstanceContext
from twilio.base.instance_resource import InstanceResource as InstanceResource
from twilio.base.list_resource import ListResource as ListResource
from twilio.base.page import Page as Page
from twilio.rest.preview.sync.service.document import DocumentList as DocumentList
from twilio.rest.preview.sync.service.sync_list import SyncListList as SyncListList
from twilio.rest.preview.sync.service.sync_map import SyncMapList as SyncMapList
from typing import Any, Optional

class ServiceList(ListResource):
    def __init__(self, version: Any) -> None: ...
    def create(self, friendly_name: Any = ..., webhook_url: Any = ..., reachability_webhooks_enabled: Any = ..., acl_enabled: Any = ...): ...
    def stream(self, limit: Optional[Any] = ..., page_size: Optional[Any] = ...): ...
    def list(self, limit: Optional[Any] = ..., page_size: Optional[Any] = ...): ...
    def page(self, page_token: Any = ..., page_number: Any = ..., page_size: Any = ...): ...
    def get_page(self, target_url: Any): ...
    def get(self, sid: Any): ...
    def __call__(self, sid: Any): ...

class ServicePage(Page):
    def __init__(self, version: Any, response: Any, solution: Any) -> None: ...
    def get_instance(self, payload: Any): ...

class ServiceContext(InstanceContext):
    def __init__(self, version: Any, sid: Any) -> None: ...
    def fetch(self): ...
    def delete(self): ...
    def update(self, webhook_url: Any = ..., friendly_name: Any = ..., reachability_webhooks_enabled: Any = ..., acl_enabled: Any = ...): ...
    @property
    def documents(self): ...
    @property
    def sync_lists(self): ...
    @property
    def sync_maps(self): ...

class ServiceInstance(InstanceResource):
    def __init__(self, version: Any, payload: Any, sid: Optional[Any] = ...) -> None: ...
    @property
    def sid(self): ...
    @property
    def account_sid(self): ...
    @property
    def friendly_name(self): ...
    @property
    def date_created(self): ...
    @property
    def date_updated(self): ...
    @property
    def url(self): ...
    @property
    def webhook_url(self): ...
    @property
    def reachability_webhooks_enabled(self): ...
    @property
    def acl_enabled(self): ...
    @property
    def links(self): ...
    def fetch(self): ...
    def delete(self): ...
    def update(self, webhook_url: Any = ..., friendly_name: Any = ..., reachability_webhooks_enabled: Any = ..., acl_enabled: Any = ...): ...
    @property
    def documents(self): ...
    @property
    def sync_lists(self): ...
    @property
    def sync_maps(self): ...
