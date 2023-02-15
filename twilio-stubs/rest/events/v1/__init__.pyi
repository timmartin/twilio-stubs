from twilio.base.version import Version as Version
from twilio.rest.events.v1.event_type import EventTypeList as EventTypeList
from twilio.rest.events.v1.schema import SchemaList as SchemaList
from twilio.rest.events.v1.sink import SinkList as SinkList
from twilio.rest.events.v1.subscription import SubscriptionList as SubscriptionList

class V1(Version):
    version: str
    def __init__(self, domain) -> None: ...
    @property
    def event_types(self): ...
    @property
    def schemas(self): ...
    @property
    def sinks(self): ...
    @property
    def subscriptions(self): ...
