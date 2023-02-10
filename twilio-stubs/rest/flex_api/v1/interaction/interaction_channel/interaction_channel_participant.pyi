from typing import Optional, Any

from twilio.base import serialize as serialize, values as values
from twilio.base.instance_context import InstanceContext as InstanceContext
from twilio.base.instance_resource import InstanceResource as InstanceResource
from twilio.base.list_resource import ListResource as ListResource
from twilio.base.page import Page as Page

class InteractionChannelParticipantList(ListResource):
    def __init__(self, version, interaction_sid, channel_sid) -> None: ...
    def create(self, type, media_properties): ...
    def stream(self, limit: Optional[Any] | None = ..., page_size: Optional[Any] | None = ...): ...
    def list(self, limit: Optional[Any] | None = ..., page_size: Optional[Any] | None = ...): ...
    def page(self, page_token=..., page_number=..., page_size=...): ...
    def get_page(self, target_url): ...
    def get(self, sid): ...
    def __call__(self, sid): ...

class InteractionChannelParticipantPage(Page):
    def __init__(self, version, response, solution) -> None: ...
    def get_instance(self, payload): ...

class InteractionChannelParticipantContext(InstanceContext):
    def __init__(self, version, interaction_sid, channel_sid, sid) -> None: ...
    def update(self, status): ...

class InteractionChannelParticipantInstance(InstanceResource):
    class Status:
        CLOSED: str
        WRAPUP: str
    class Type:
        SUPERVISOR: str
        CUSTOMER: str
        EXTERNAL: str
        AGENT: str
        UNKNOWN: str
    def __init__(self, version, payload, interaction_sid, channel_sid, sid: Any | None = ...) -> None: ...
    @property
    def sid(self): ...
    @property
    def type(self): ...
    @property
    def interaction_sid(self): ...
    @property
    def channel_sid(self): ...
    @property
    def url(self): ...
    def update(self, status): ...
