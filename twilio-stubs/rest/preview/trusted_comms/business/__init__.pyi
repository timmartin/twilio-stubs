from twilio.base import values as values
from twilio.base.instance_context import InstanceContext as InstanceContext
from twilio.base.instance_resource import InstanceResource as InstanceResource
from twilio.base.list_resource import ListResource as ListResource
from twilio.base.page import Page as Page
from twilio.rest.preview.trusted_comms.business.insights import InsightsList as InsightsList
from typing import Any, Optional

class BusinessList(ListResource):
    def __init__(self, version: Any) -> None: ...
    def get(self, sid: Any): ...
    def __call__(self, sid: Any): ...

class BusinessPage(Page):
    def __init__(self, version: Any, response: Any, solution: Any) -> None: ...
    def get_instance(self, payload: Any): ...

class BusinessContext(InstanceContext):
    def __init__(self, version: Any, sid: Any) -> None: ...
    def fetch(self): ...
    @property
    def insights(self): ...

class BusinessInstance(InstanceResource):
    def __init__(self, version: Any, payload: Any, sid: Optional[Any] = ...) -> None: ...
    @property
    def account_sid(self): ...
    @property
    def sid(self): ...
    @property
    def url(self): ...
    @property
    def links(self): ...
    def fetch(self): ...
    @property
    def insights(self): ...
