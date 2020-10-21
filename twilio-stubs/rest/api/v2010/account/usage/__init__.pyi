from twilio.base.instance_resource import InstanceResource as InstanceResource
from twilio.base.list_resource import ListResource as ListResource
from twilio.base.page import Page as Page
from twilio.rest.api.v2010.account.usage.record import RecordList as RecordList
from twilio.rest.api.v2010.account.usage.trigger import TriggerList as TriggerList
from typing import Any

class UsageList(ListResource):
    def __init__(self, version: Any, account_sid: Any) -> None: ...
    @property
    def records(self): ...
    @property
    def triggers(self): ...

class UsagePage(Page):
    def __init__(self, version: Any, response: Any, solution: Any) -> None: ...
    def get_instance(self, payload: Any): ...

class UsageInstance(InstanceResource):
    def __init__(self, version: Any, payload: Any, account_sid: Any) -> None: ...
