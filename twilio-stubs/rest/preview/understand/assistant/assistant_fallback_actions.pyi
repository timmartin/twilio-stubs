from twilio.base import serialize as serialize, values as values
from twilio.base.instance_context import InstanceContext as InstanceContext
from twilio.base.instance_resource import InstanceResource as InstanceResource
from twilio.base.list_resource import ListResource as ListResource
from twilio.base.page import Page as Page

class AssistantFallbackActionsList(ListResource):
    def __init__(self, version, assistant_sid) -> None: ...
    def get(self): ...
    def __call__(self): ...

class AssistantFallbackActionsPage(Page):
    def __init__(self, version, response, solution) -> None: ...
    def get_instance(self, payload): ...

class AssistantFallbackActionsContext(InstanceContext):
    def __init__(self, version, assistant_sid) -> None: ...
    def fetch(self): ...
    def update(self, fallback_actions=...): ...

class AssistantFallbackActionsInstance(InstanceResource):
    def __init__(self, version, payload, assistant_sid) -> None: ...
    @property
    def account_sid(self): ...
    @property
    def assistant_sid(self): ...
    @property
    def url(self): ...
    @property
    def data(self): ...
    def fetch(self): ...
    def update(self, fallback_actions=...): ...
