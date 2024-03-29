from _typeshed import Incomplete
from twilio.base import values as values
from twilio.base.instance_context import InstanceContext as InstanceContext
from twilio.base.instance_resource import InstanceResource as InstanceResource
from twilio.base.list_resource import ListResource as ListResource
from twilio.base.page import Page as Page
from twilio.rest.insights.v1.call.annotation import AnnotationList as AnnotationList
from twilio.rest.insights.v1.call.event import EventList as EventList
from twilio.rest.insights.v1.call.metric import MetricList as MetricList
from twilio.rest.insights.v1.call.summary import CallSummaryList as CallSummaryList

class CallList(ListResource):
    def __init__(self, version) -> None: ...
    def get(self, sid): ...
    def __call__(self, sid): ...

class CallPage(Page):
    def __init__(self, version, response, solution) -> None: ...
    def get_instance(self, payload): ...

class CallContext(InstanceContext):
    def __init__(self, version, sid) -> None: ...
    def fetch(self): ...
    @property
    def events(self): ...
    @property
    def metrics(self): ...
    @property
    def summary(self): ...
    @property
    def annotation(self): ...

class CallInstance(InstanceResource):
    def __init__(self, version, payload, sid: Incomplete | None = ...) -> None: ...
    @property
    def sid(self): ...
    @property
    def url(self): ...
    @property
    def links(self): ...
    def fetch(self): ...
    @property
    def events(self): ...
    @property
    def metrics(self): ...
    @property
    def summary(self): ...
    @property
    def annotation(self): ...
