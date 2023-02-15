from _typeshed import Incomplete
from twilio.base import deserialize as deserialize
from twilio.base.instance_context import InstanceContext as InstanceContext
from twilio.base.instance_resource import InstanceResource as InstanceResource
from twilio.base.list_resource import ListResource as ListResource
from twilio.base.page import Page as Page

class ArchivedCallList(ListResource):
    def __init__(self, version) -> None: ...
    def get(self, date, sid): ...
    def __call__(self, date, sid): ...

class ArchivedCallPage(Page):
    def __init__(self, version, response, solution) -> None: ...
    def get_instance(self, payload): ...

class ArchivedCallContext(InstanceContext):
    def __init__(self, version, date, sid) -> None: ...
    def delete(self): ...

class ArchivedCallInstance(InstanceResource):
    def __init__(self, version, payload, date: Incomplete | None = ..., sid: Incomplete | None = ...) -> None: ...
    @property
    def date(self): ...
    @property
    def sid(self): ...
    @property
    def url(self): ...
    def delete(self): ...