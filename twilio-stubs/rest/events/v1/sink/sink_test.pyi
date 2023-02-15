from twilio.base import values as values
from twilio.base.instance_resource import InstanceResource as InstanceResource
from twilio.base.list_resource import ListResource as ListResource
from twilio.base.page import Page as Page

class SinkTestList(ListResource):
    def __init__(self, version, sid) -> None: ...
    def create(self): ...

class SinkTestPage(Page):
    def __init__(self, version, response, solution) -> None: ...
    def get_instance(self, payload): ...

class SinkTestInstance(InstanceResource):
    def __init__(self, version, payload, sid) -> None: ...
    @property
    def result(self): ...
