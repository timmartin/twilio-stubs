from twilio.base import values as values
from twilio.base.instance_context import InstanceContext as InstanceContext
from twilio.base.instance_resource import InstanceResource as InstanceResource
from twilio.base.list_resource import ListResource as ListResource
from twilio.base.page import Page as Page
from typing import Any

class CpsList(ListResource):
    def __init__(self, version: Any) -> None: ...
    def get(self): ...
    def __call__(self): ...

class CpsPage(Page):
    def __init__(self, version: Any, response: Any, solution: Any) -> None: ...
    def get_instance(self, payload: Any): ...

class CpsContext(InstanceContext):
    def __init__(self, version: Any) -> None: ...
    def fetch(self, x_xcnam_sensitive_phone_number: Any = ...): ...

class CpsInstance(InstanceResource):
    def __init__(self, version: Any, payload: Any) -> None: ...
    @property
    def cps_url(self): ...
    @property
    def phone_number(self): ...
    @property
    def url(self): ...
    def fetch(self, x_xcnam_sensitive_phone_number: Any = ...): ...
