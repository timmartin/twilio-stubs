from _typeshed import Incomplete
from twilio.base import deserialize as deserialize, values as values
from twilio.base.instance_context import InstanceContext as InstanceContext
from twilio.base.instance_resource import InstanceResource as InstanceResource
from twilio.base.list_resource import ListResource as ListResource
from twilio.base.page import Page as Page

class CustomerProfilesChannelEndpointAssignmentList(ListResource):
    def __init__(self, version, customer_profile_sid) -> None: ...
    def create(self, channel_endpoint_type, channel_endpoint_sid): ...
    def stream(self, channel_endpoint_sid=..., channel_endpoint_sids=..., limit: Incomplete | None = ..., page_size: Incomplete | None = ...): ...
    def list(self, channel_endpoint_sid=..., channel_endpoint_sids=..., limit: Incomplete | None = ..., page_size: Incomplete | None = ...): ...
    def page(self, channel_endpoint_sid=..., channel_endpoint_sids=..., page_token=..., page_number=..., page_size=...): ...
    def get_page(self, target_url): ...
    def get(self, sid): ...
    def __call__(self, sid): ...

class CustomerProfilesChannelEndpointAssignmentPage(Page):
    def __init__(self, version, response, solution) -> None: ...
    def get_instance(self, payload): ...

class CustomerProfilesChannelEndpointAssignmentContext(InstanceContext):
    def __init__(self, version, customer_profile_sid, sid) -> None: ...
    def fetch(self): ...
    def delete(self): ...

class CustomerProfilesChannelEndpointAssignmentInstance(InstanceResource):
    def __init__(self, version, payload, customer_profile_sid, sid: Incomplete | None = ...) -> None: ...
    @property
    def sid(self): ...
    @property
    def customer_profile_sid(self): ...
    @property
    def account_sid(self): ...
    @property
    def channel_endpoint_type(self): ...
    @property
    def channel_endpoint_sid(self): ...
    @property
    def date_created(self): ...
    @property
    def url(self): ...
    def fetch(self): ...
    def delete(self): ...
