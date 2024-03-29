from twilio.base import values as values
from twilio.base.instance_resource import InstanceResource as InstanceResource
from twilio.base.list_resource import ListResource as ListResource
from twilio.base.page import Page as Page

class UsecaseList(ListResource):
    def __init__(self, version) -> None: ...
    def fetch(self): ...

class UsecasePage(Page):
    def __init__(self, version, response, solution) -> None: ...
    def get_instance(self, payload): ...

class UsecaseInstance(InstanceResource):
    def __init__(self, version, payload) -> None: ...
    @property
    def usecases(self): ...
