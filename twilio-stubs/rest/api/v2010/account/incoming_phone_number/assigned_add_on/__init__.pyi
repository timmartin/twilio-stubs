from _typeshed import Incomplete
from twilio.base import deserialize as deserialize, values as values
from twilio.base.instance_context import InstanceContext as InstanceContext
from twilio.base.instance_resource import InstanceResource as InstanceResource
from twilio.base.list_resource import ListResource as ListResource
from twilio.base.page import Page as Page
from twilio.rest.api.v2010.account.incoming_phone_number.assigned_add_on.assigned_add_on_extension import AssignedAddOnExtensionList as AssignedAddOnExtensionList

class AssignedAddOnList(ListResource):
    def __init__(self, version, account_sid, resource_sid) -> None: ...
    def stream(self, limit: Incomplete | None = ..., page_size: Incomplete | None = ...): ...
    def list(self, limit: Incomplete | None = ..., page_size: Incomplete | None = ...): ...
    def page(self, page_token=..., page_number=..., page_size=...): ...
    def get_page(self, target_url): ...
    def create(self, installed_add_on_sid): ...
    def get(self, sid): ...
    def __call__(self, sid): ...

class AssignedAddOnPage(Page):
    def __init__(self, version, response, solution) -> None: ...
    def get_instance(self, payload): ...

class AssignedAddOnContext(InstanceContext):
    def __init__(self, version, account_sid, resource_sid, sid) -> None: ...
    def fetch(self): ...
    def delete(self): ...
    @property
    def extensions(self): ...

class AssignedAddOnInstance(InstanceResource):
    def __init__(self, version, payload, account_sid, resource_sid, sid: Incomplete | None = ...) -> None: ...
    @property
    def sid(self): ...
    @property
    def account_sid(self): ...
    @property
    def resource_sid(self): ...
    @property
    def friendly_name(self): ...
    @property
    def description(self): ...
    @property
    def configuration(self): ...
    @property
    def unique_name(self): ...
    @property
    def date_created(self): ...
    @property
    def date_updated(self): ...
    @property
    def uri(self): ...
    @property
    def subresource_uris(self): ...
    def fetch(self): ...
    def delete(self): ...
    @property
    def extensions(self): ...
