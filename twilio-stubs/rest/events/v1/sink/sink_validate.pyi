from twilio.base import values as values
from twilio.base.instance_resource import InstanceResource as InstanceResource
from twilio.base.list_resource import ListResource as ListResource
from twilio.base.page import Page as Page

class SinkValidateList(ListResource):
    def __init__(self, version, sid) -> None: ...
    def create(self, test_id): ...

class SinkValidatePage(Page):
    def __init__(self, version, response, solution) -> None: ...
    def get_instance(self, payload): ...

class SinkValidateInstance(InstanceResource):
    def __init__(self, version, payload, sid) -> None: ...
    @property
    def result(self): ...
