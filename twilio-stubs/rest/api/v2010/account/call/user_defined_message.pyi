from twilio.base import deserialize as deserialize, values as values
from twilio.base.instance_resource import InstanceResource as InstanceResource
from twilio.base.list_resource import ListResource as ListResource
from twilio.base.page import Page as Page

class UserDefinedMessageList(ListResource):
    def __init__(self, version, account_sid, call_sid) -> None: ...
    def create(self, content, idempotency_key=...): ...

class UserDefinedMessagePage(Page):
    def __init__(self, version, response, solution) -> None: ...
    def get_instance(self, payload): ...

class UserDefinedMessageInstance(InstanceResource):
    def __init__(self, version, payload, account_sid, call_sid) -> None: ...
    @property
    def account_sid(self): ...
    @property
    def call_sid(self): ...
    @property
    def sid(self): ...
    @property
    def date_created(self): ...
