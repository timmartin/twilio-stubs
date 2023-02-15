from _typeshed import Incomplete
from twilio.base import deserialize as deserialize, values as values
from twilio.base.instance_context import InstanceContext as InstanceContext
from twilio.base.instance_resource import InstanceResource as InstanceResource
from twilio.base.list_resource import ListResource as ListResource
from twilio.base.page import Page as Page
from twilio.rest.sync.v1.service.document import DocumentList as DocumentList
from twilio.rest.sync.v1.service.sync_list import SyncListList as SyncListList
from twilio.rest.sync.v1.service.sync_map import SyncMapList as SyncMapList
from twilio.rest.sync.v1.service.sync_stream import SyncStreamList as SyncStreamList

class ServiceList(ListResource):
    def __init__(self, version) -> None: ...
    def create(self, friendly_name=..., webhook_url=..., reachability_webhooks_enabled=..., acl_enabled=..., reachability_debouncing_enabled=..., reachability_debouncing_window=..., webhooks_from_rest_enabled=...): ...
    def stream(self, limit: Incomplete | None = ..., page_size: Incomplete | None = ...): ...
    def list(self, limit: Incomplete | None = ..., page_size: Incomplete | None = ...): ...
    def page(self, page_token=..., page_number=..., page_size=...): ...
    def get_page(self, target_url): ...
    def get(self, sid): ...
    def __call__(self, sid): ...

class ServicePage(Page):
    def __init__(self, version, response, solution) -> None: ...
    def get_instance(self, payload): ...

class ServiceContext(InstanceContext):
    def __init__(self, version, sid) -> None: ...
    def fetch(self): ...
    def delete(self): ...
    def update(self, webhook_url=..., friendly_name=..., reachability_webhooks_enabled=..., acl_enabled=..., reachability_debouncing_enabled=..., reachability_debouncing_window=..., webhooks_from_rest_enabled=...): ...
    @property
    def documents(self): ...
    @property
    def sync_lists(self): ...
    @property
    def sync_maps(self): ...
    @property
    def sync_streams(self): ...

class ServiceInstance(InstanceResource):
    def __init__(self, version, payload, sid: Incomplete | None = ...) -> None: ...
    @property
    def sid(self): ...
    @property
    def unique_name(self): ...
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
    def webhooks_from_rest_enabled(self): ...
    @property
    def reachability_webhooks_enabled(self): ...
    @property
    def acl_enabled(self): ...
    @property
    def reachability_debouncing_enabled(self): ...
    @property
    def reachability_debouncing_window(self): ...
    @property
    def links(self): ...
    def fetch(self): ...
    def delete(self): ...
    def update(self, webhook_url=..., friendly_name=..., reachability_webhooks_enabled=..., acl_enabled=..., reachability_debouncing_enabled=..., reachability_debouncing_window=..., webhooks_from_rest_enabled=...): ...
    @property
    def documents(self): ...
    @property
    def sync_lists(self): ...
    @property
    def sync_maps(self): ...
    @property
    def sync_streams(self): ...
