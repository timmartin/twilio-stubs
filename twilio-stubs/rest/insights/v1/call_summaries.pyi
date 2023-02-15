from _typeshed import Incomplete
from twilio.base import deserialize as deserialize, values as values
from twilio.base.instance_resource import InstanceResource as InstanceResource
from twilio.base.list_resource import ListResource as ListResource
from twilio.base.page import Page as Page

class CallSummariesList(ListResource):
    def __init__(self, version) -> None: ...
    def stream(self, from_=..., to=..., from_carrier=..., to_carrier=..., from_country_code=..., to_country_code=..., branded=..., verified_caller=..., has_tag=..., start_time=..., end_time=..., call_type=..., call_state=..., direction=..., processing_state=..., sort_by=..., subaccount=..., abnormal_session=..., limit: Incomplete | None = ..., page_size: Incomplete | None = ...): ...
    def list(self, from_=..., to=..., from_carrier=..., to_carrier=..., from_country_code=..., to_country_code=..., branded=..., verified_caller=..., has_tag=..., start_time=..., end_time=..., call_type=..., call_state=..., direction=..., processing_state=..., sort_by=..., subaccount=..., abnormal_session=..., limit: Incomplete | None = ..., page_size: Incomplete | None = ...): ...
    def page(self, from_=..., to=..., from_carrier=..., to_carrier=..., from_country_code=..., to_country_code=..., branded=..., verified_caller=..., has_tag=..., start_time=..., end_time=..., call_type=..., call_state=..., direction=..., processing_state=..., sort_by=..., subaccount=..., abnormal_session=..., page_token=..., page_number=..., page_size=...): ...
    def get_page(self, target_url): ...

class CallSummariesPage(Page):
    def __init__(self, version, response, solution) -> None: ...
    def get_instance(self, payload): ...

class CallSummariesInstance(InstanceResource):
    class AnsweredBy:
        UNKNOWN: str
        MACHINE_START: str
        MACHINE_END_BEEP: str
        MACHINE_END_SILENCE: str
        MACHINE_END_OTHER: str
        HUMAN: str
        FAX: str
    class CallType:
        CARRIER: str
        SIP: str
        TRUNKING: str
        CLIENT: str
    class CallState:
        RINGING: str
        COMPLETED: str
        BUSY: str
        FAIL: str
        NOANSWER: str
        CANCELED: str
        ANSWERED: str
        UNDIALED: str
    class ProcessingState:
        COMPLETE: str
        PARTIAL: str
    class CallDirection:
        OUTBOUND_API: str
        OUTBOUND_DIAL: str
        INBOUND: str
        TRUNKING_ORIGINATING: str
        TRUNKING_TERMINATING: str
    class SortBy:
        START_TIME: str
        END_TIME: str
    class ProcessingStateRequest:
        COMPLETED: str
        STARTED: str
        PARTIAL: str
        ALL: str
    def __init__(self, version, payload) -> None: ...
    @property
    def account_sid(self): ...
    @property
    def call_sid(self): ...
    @property
    def answered_by(self): ...
    @property
    def call_type(self): ...
    @property
    def call_state(self): ...
    @property
    def processing_state(self): ...
    @property
    def created_time(self): ...
    @property
    def start_time(self): ...
    @property
    def end_time(self): ...
    @property
    def duration(self): ...
    @property
    def connect_duration(self): ...
    @property
    def from_(self): ...
    @property
    def to(self): ...
    @property
    def carrier_edge(self): ...
    @property
    def client_edge(self): ...
    @property
    def sdk_edge(self): ...
    @property
    def sip_edge(self): ...
    @property
    def tags(self): ...
    @property
    def url(self): ...
    @property
    def attributes(self): ...
    @property
    def properties(self): ...
    @property
    def trust(self): ...
