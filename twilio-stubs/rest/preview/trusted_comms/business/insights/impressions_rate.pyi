from twilio.base import deserialize as deserialize, serialize as serialize, values as values
from twilio.base.instance_context import InstanceContext as InstanceContext
from twilio.base.instance_resource import InstanceResource as InstanceResource
from twilio.base.list_resource import ListResource as ListResource
from twilio.base.page import Page as Page
from typing import Any

class ImpressionsRateList(ListResource):
    def __init__(self, version: Any, business_sid: Any) -> None: ...
    def get(self): ...
    def __call__(self): ...

class ImpressionsRatePage(Page):
    def __init__(self, version: Any, response: Any, solution: Any) -> None: ...
    def get_instance(self, payload: Any): ...

class ImpressionsRateContext(InstanceContext):
    def __init__(self, version: Any, business_sid: Any) -> None: ...
    def fetch(self, brand_sid: Any = ..., branded_channel_sid: Any = ..., phone_number_sid: Any = ..., country: Any = ..., start: Any = ..., end: Any = ..., interval: Any = ...): ...

class ImpressionsRateInstance(InstanceResource):
    class Intervals:
        MINUTE: str = ...
        HOUR: str = ...
        DAY: str = ...
        WEEK: str = ...
        MONTH: str = ...
    def __init__(self, version: Any, payload: Any, business_sid: Any) -> None: ...
    @property
    def account_sid(self): ...
    @property
    def business_sid(self): ...
    @property
    def end(self): ...
    @property
    def interval(self): ...
    @property
    def reports(self): ...
    @property
    def start(self): ...
    @property
    def url(self): ...
    def fetch(self, brand_sid: Any = ..., branded_channel_sid: Any = ..., phone_number_sid: Any = ..., country: Any = ..., start: Any = ..., end: Any = ..., interval: Any = ...): ...
