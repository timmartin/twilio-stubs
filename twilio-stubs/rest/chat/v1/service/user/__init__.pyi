from _typeshed import Incomplete
from twilio.base import deserialize as deserialize, values as values
from twilio.base.instance_context import InstanceContext as InstanceContext
from twilio.base.instance_resource import InstanceResource as InstanceResource
from twilio.base.list_resource import ListResource as ListResource
from twilio.base.page import Page as Page
from twilio.rest.chat.v1.service.user.user_channel import UserChannelList as UserChannelList

class UserList(ListResource):
    def __init__(self, version, service_sid) -> None: ...
    def create(self, identity, role_sid=..., attributes=..., friendly_name=...): ...
    def stream(self, limit: Incomplete | None = ..., page_size: Incomplete | None = ...): ...
    def list(self, limit: Incomplete | None = ..., page_size: Incomplete | None = ...): ...
    def page(self, page_token=..., page_number=..., page_size=...): ...
    def get_page(self, target_url): ...
    def get(self, sid): ...
    def __call__(self, sid): ...

class UserPage(Page):
    def __init__(self, version, response, solution) -> None: ...
    def get_instance(self, payload): ...

class UserContext(InstanceContext):
    def __init__(self, version, service_sid, sid) -> None: ...
    def fetch(self): ...
    def delete(self): ...
    def update(self, role_sid=..., attributes=..., friendly_name=...): ...
    @property
    def user_channels(self): ...

class UserInstance(InstanceResource):
    def __init__(self, version, payload, service_sid, sid: Incomplete | None = ...) -> None: ...
    @property
    def sid(self): ...
    @property
    def account_sid(self): ...
    @property
    def service_sid(self): ...
    @property
    def attributes(self): ...
    @property
    def friendly_name(self): ...
    @property
    def role_sid(self): ...
    @property
    def identity(self): ...
    @property
    def is_online(self): ...
    @property
    def is_notifiable(self): ...
    @property
    def date_created(self): ...
    @property
    def date_updated(self): ...
    @property
    def joined_channels_count(self): ...
    @property
    def links(self): ...
    @property
    def url(self): ...
    def fetch(self): ...
    def delete(self): ...
    def update(self, role_sid=..., attributes=..., friendly_name=...): ...
    @property
    def user_channels(self): ...
