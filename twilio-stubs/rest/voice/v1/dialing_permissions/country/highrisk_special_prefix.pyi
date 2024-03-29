from _typeshed import Incomplete
from twilio.base import values as values
from twilio.base.instance_resource import InstanceResource as InstanceResource
from twilio.base.list_resource import ListResource as ListResource
from twilio.base.page import Page as Page

class HighriskSpecialPrefixList(ListResource):
    def __init__(self, version, iso_code) -> None: ...
    def stream(self, limit: Incomplete | None = ..., page_size: Incomplete | None = ...): ...
    def list(self, limit: Incomplete | None = ..., page_size: Incomplete | None = ...): ...
    def page(self, page_token=..., page_number=..., page_size=...): ...
    def get_page(self, target_url): ...

class HighriskSpecialPrefixPage(Page):
    def __init__(self, version, response, solution) -> None: ...
    def get_instance(self, payload): ...

class HighriskSpecialPrefixInstance(InstanceResource):
    def __init__(self, version, payload, iso_code) -> None: ...
    @property
    def prefix(self): ...
