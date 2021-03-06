from twilio.base import deserialize as deserialize, values as values
from twilio.base.instance_context import InstanceContext as InstanceContext
from twilio.base.instance_resource import InstanceResource as InstanceResource
from twilio.base.list_resource import ListResource as ListResource
from twilio.base.page import Page as Page
from twilio.rest.api.v2010.account.incoming_phone_number.assigned_add_on.assigned_add_on_extension import AssignedAddOnExtensionList as AssignedAddOnExtensionList
from typing import Any, Optional

class AssignedAddOnList(ListResource):
    def __init__(self, version: Any, account_sid: Any, resource_sid: Any) -> None: ...
    def stream(self, limit: Optional[Any] = ..., page_size: Optional[Any] = ...): ...
    def list(self, limit: Optional[Any] = ..., page_size: Optional[Any] = ...): ...
    def page(self, page_token: Any = ..., page_number: Any = ..., page_size: Any = ...): ...
    def get_page(self, target_url: Any): ...
    def create(self, installed_add_on_sid: Any): ...
    def get(self, sid: Any): ...
    def __call__(self, sid: Any): ...

class AssignedAddOnPage(Page):
    def __init__(self, version: Any, response: Any, solution: Any) -> None: ...
    def get_instance(self, payload: Any): ...

class AssignedAddOnContext(InstanceContext):
    def __init__(self, version: Any, account_sid: Any, resource_sid: Any, sid: Any) -> None: ...
    def fetch(self): ...
    def delete(self): ...
    @property
    def extensions(self): ...

class AssignedAddOnInstance(InstanceResource):
    def __init__(self, version: Any, payload: Any, account_sid: Any, resource_sid: Any, sid: Optional[Any] = ...) -> None: ...
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
