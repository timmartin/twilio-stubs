from _typeshed import Incomplete
from twilio.base import values as values
from twilio.base.instance_context import InstanceContext as InstanceContext
from twilio.base.instance_resource import InstanceResource as InstanceResource
from twilio.base.list_resource import ListResource as ListResource
from twilio.base.page import Page as Page

class DialogueList(ListResource):
    def __init__(self, version, assistant_sid) -> None: ...
    def get(self, sid): ...
    def __call__(self, sid): ...

class DialoguePage(Page):
    def __init__(self, version, response, solution) -> None: ...
    def get_instance(self, payload): ...

class DialogueContext(InstanceContext):
    def __init__(self, version, assistant_sid, sid) -> None: ...
    def fetch(self): ...

class DialogueInstance(InstanceResource):
    def __init__(self, version, payload, assistant_sid, sid: Incomplete | None = ...) -> None: ...
    @property
    def account_sid(self): ...
    @property
    def assistant_sid(self): ...
    @property
    def sid(self): ...
    @property
    def data(self): ...
    @property
    def url(self): ...
    def fetch(self): ...
