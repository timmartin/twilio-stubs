from typing import Any

from twilio.base import serialize as serialize, values as values
from twilio.base.instance_context import InstanceContext as InstanceContext
from twilio.base.instance_resource import InstanceResource as InstanceResource
from twilio.base.list_resource import ListResource as ListResource
from twilio.base.page import Page as Page
from twilio.rest.flex_api.v1.interaction.interaction_channel import InteractionChannelList as InteractionChannelList

class InteractionList(ListResource):
    def __init__(self, version) -> None: ...
    def create(self, channel, routing): ...
    def get(self, sid): ...
    def __call__(self, sid): ...

class InteractionPage(Page):
    def __init__(self, version, response, solution) -> None: ...
    def get_instance(self, payload): ...

class InteractionContext(InstanceContext):
    def __init__(self, version, sid) -> None: ...
    def fetch(self): ...
    @property
    def channels(self): ...

class InteractionInstance(InstanceResource):
    def __init__(self, version, payload, sid: Any | None = ...) -> None: ...
    @property
    def sid(self): ...
    @property
    def channel(self): ...
    @property
    def routing(self): ...
    @property
    def url(self): ...
    @property
    def links(self): ...
    def fetch(self): ...
    @property
    def channels(self): ...