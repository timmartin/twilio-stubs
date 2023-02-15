from twilio.base import values as values
from twilio.base.instance_context import InstanceContext as InstanceContext
from twilio.base.instance_resource import InstanceResource as InstanceResource
from twilio.base.list_resource import ListResource as ListResource
from twilio.base.page import Page as Page

class UserInfoList(ListResource):
    def __init__(self, version) -> None: ...
    def get(self): ...
    def __call__(self): ...

class UserInfoPage(Page):
    def __init__(self, version, response, solution) -> None: ...
    def get_instance(self, payload): ...

class UserInfoContext(InstanceContext):
    def __init__(self, version) -> None: ...
    def fetch(self): ...

class UserInfoInstance(InstanceResource):
    def __init__(self, version, payload) -> None: ...
    @property
    def user_sid(self): ...
    @property
    def first_name(self): ...
    @property
    def last_name(self): ...
    @property
    def friendly_name(self): ...
    @property
    def email(self): ...
    @property
    def url(self): ...
    def fetch(self): ...