from twilio.base import values as values
from twilio.base.instance_context import InstanceContext as InstanceContext
from twilio.base.instance_resource import InstanceResource as InstanceResource
from twilio.base.list_resource import ListResource as ListResource
from twilio.base.page import Page as Page

class ApprovalFetchList(ListResource):
    def __init__(self, version, sid) -> None: ...
    def get(self): ...
    def __call__(self): ...

class ApprovalFetchPage(Page):
    def __init__(self, version, response, solution) -> None: ...
    def get_instance(self, payload): ...

class ApprovalFetchContext(InstanceContext):
    def __init__(self, version, sid) -> None: ...
    def fetch(self): ...

class ApprovalFetchInstance(InstanceResource):
    def __init__(self, version, payload, sid) -> None: ...
    @property
    def sid(self): ...
    @property
    def account_sid(self): ...
    @property
    def whatsapp(self): ...
    @property
    def url(self): ...
    def fetch(self): ...
