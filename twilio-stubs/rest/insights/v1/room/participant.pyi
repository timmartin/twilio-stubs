from _typeshed import Incomplete
from twilio.base import deserialize as deserialize, values as values
from twilio.base.instance_context import InstanceContext as InstanceContext
from twilio.base.instance_resource import InstanceResource as InstanceResource
from twilio.base.list_resource import ListResource as ListResource
from twilio.base.page import Page as Page

class ParticipantList(ListResource):
    def __init__(self, version, room_sid) -> None: ...
    def stream(self, limit: Incomplete | None = ..., page_size: Incomplete | None = ...): ...
    def list(self, limit: Incomplete | None = ..., page_size: Incomplete | None = ...): ...
    def page(self, page_token=..., page_number=..., page_size=...): ...
    def get_page(self, target_url): ...
    def get(self, participant_sid): ...
    def __call__(self, participant_sid): ...

class ParticipantPage(Page):
    def __init__(self, version, response, solution) -> None: ...
    def get_instance(self, payload): ...

class ParticipantContext(InstanceContext):
    def __init__(self, version, room_sid, participant_sid) -> None: ...
    def fetch(self): ...

class ParticipantInstance(InstanceResource):
    class RoomStatus:
        IN_PROGRESS: str
        COMPLETED: str
    class Codec:
        VP8: str
        H264: str
        VP9: str
    class TwilioRealm:
        US1: str
        US2: str
        AU1: str
        BR1: str
        IE1: str
        JP1: str
        SG1: str
        IN1: str
        DE1: str
        GLL: str
    class EdgeLocation:
        ASHBURN: str
        DUBLIN: str
        FRANKFURT: str
        SINGAPORE: str
        SYDNEY: str
        SAO_PAULO: str
        ROAMING: str
        UMATILLA: str
        TOKYO: str
    def __init__(self, version, payload, room_sid, participant_sid: Incomplete | None = ...) -> None: ...
    @property
    def participant_sid(self): ...
    @property
    def participant_identity(self): ...
    @property
    def join_time(self): ...
    @property
    def leave_time(self): ...
    @property
    def duration_sec(self): ...
    @property
    def account_sid(self): ...
    @property
    def room_sid(self): ...
    @property
    def status(self): ...
    @property
    def codecs(self): ...
    @property
    def end_reason(self): ...
    @property
    def error_code(self): ...
    @property
    def error_code_url(self): ...
    @property
    def media_region(self): ...
    @property
    def properties(self): ...
    @property
    def edge_location(self): ...
    @property
    def publisher_info(self): ...
    @property
    def url(self): ...
    def fetch(self): ...
