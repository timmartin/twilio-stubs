from twilio.base import serialize as serialize, values as values
from twilio.base.instance_resource import InstanceResource as InstanceResource
from twilio.base.list_resource import ListResource as ListResource
from twilio.base.page import Page as Page

class StreamMessageList(ListResource):
    def __init__(self, version, service_sid, stream_sid) -> None: ...
    def create(self, data): ...

class StreamMessagePage(Page):
    def __init__(self, version, response, solution) -> None: ...
    def get_instance(self, payload): ...

class StreamMessageInstance(InstanceResource):
    def __init__(self, version, payload, service_sid, stream_sid) -> None: ...
    @property
    def sid(self): ...
    @property
    def data(self): ...
