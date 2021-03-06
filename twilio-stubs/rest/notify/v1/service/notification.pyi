from twilio.base import deserialize as deserialize, serialize as serialize, values as values
from twilio.base.instance_resource import InstanceResource as InstanceResource
from twilio.base.list_resource import ListResource as ListResource
from twilio.base.page import Page as Page
from typing import Any

class NotificationList(ListResource):
    def __init__(self, version: Any, service_sid: Any) -> None: ...
    def create(self, body: Any = ..., priority: Any = ..., ttl: Any = ..., title: Any = ..., sound: Any = ..., action: Any = ..., data: Any = ..., apn: Any = ..., gcm: Any = ..., sms: Any = ..., facebook_messenger: Any = ..., fcm: Any = ..., segment: Any = ..., alexa: Any = ..., to_binding: Any = ..., delivery_callback_url: Any = ..., identity: Any = ..., tag: Any = ...): ...

class NotificationPage(Page):
    def __init__(self, version: Any, response: Any, solution: Any) -> None: ...
    def get_instance(self, payload: Any): ...

class NotificationInstance(InstanceResource):
    class Priority:
        HIGH: str = ...
        LOW: str = ...
    def __init__(self, version: Any, payload: Any, service_sid: Any) -> None: ...
    @property
    def sid(self): ...
    @property
    def account_sid(self): ...
    @property
    def service_sid(self): ...
    @property
    def date_created(self): ...
    @property
    def identities(self): ...
    @property
    def tags(self): ...
    @property
    def segments(self): ...
    @property
    def priority(self): ...
    @property
    def ttl(self): ...
    @property
    def title(self): ...
    @property
    def body(self): ...
    @property
    def sound(self): ...
    @property
    def action(self): ...
    @property
    def data(self): ...
    @property
    def apn(self): ...
    @property
    def gcm(self): ...
    @property
    def fcm(self): ...
    @property
    def sms(self): ...
    @property
    def facebook_messenger(self): ...
    @property
    def alexa(self): ...
