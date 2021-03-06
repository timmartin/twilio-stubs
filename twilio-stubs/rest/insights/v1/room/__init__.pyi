from twilio.base import deserialize as deserialize, serialize as serialize, values as values
from twilio.base.instance_context import InstanceContext as InstanceContext
from twilio.base.instance_resource import InstanceResource as InstanceResource
from twilio.base.list_resource import ListResource as ListResource
from twilio.base.page import Page as Page
from twilio.rest.insights.v1.room.participant import ParticipantList as ParticipantList
from typing import Any, Optional

class RoomList(ListResource):
    def __init__(self, version: Any) -> None: ...
    def stream(self, room_type: Any = ..., codec: Any = ..., room_name: Any = ..., created_after: Any = ..., created_before: Any = ..., limit: Optional[Any] = ..., page_size: Optional[Any] = ...): ...
    def list(self, room_type: Any = ..., codec: Any = ..., room_name: Any = ..., created_after: Any = ..., created_before: Any = ..., limit: Optional[Any] = ..., page_size: Optional[Any] = ...): ...
    def page(self, room_type: Any = ..., codec: Any = ..., room_name: Any = ..., created_after: Any = ..., created_before: Any = ..., page_token: Any = ..., page_number: Any = ..., page_size: Any = ...): ...
    def get_page(self, target_url: Any): ...
    def get(self, room_sid: Any): ...
    def __call__(self, room_sid: Any): ...

class RoomPage(Page):
    def __init__(self, version: Any, response: Any, solution: Any) -> None: ...
    def get_instance(self, payload: Any): ...

class RoomContext(InstanceContext):
    def __init__(self, version: Any, room_sid: Any) -> None: ...
    def fetch(self): ...
    @property
    def participants(self): ...

class RoomInstance(InstanceResource):
    class RoomType:
        GO: str = ...
        PEER_TO_PEER: str = ...
        GROUP: str = ...
        GROUP_SMALL: str = ...
    class RoomStatus:
        IN_PROGRESS: str = ...
        COMPLETED: str = ...
    class CreatedMethod:
        SDK: str = ...
        AD_HOC: str = ...
        API: str = ...
    class EndReason:
        ROOM_ENDED_VIA_API: str = ...
        TIMEOUT: str = ...
    class Codec:
        VP8: str = ...
        H264: str = ...
        VP9: str = ...
    class TwilioRealm:
        US1: str = ...
        US2: str = ...
        AU1: str = ...
        BR1: str = ...
        IE1: str = ...
        JP1: str = ...
        SG1: str = ...
        IN1: str = ...
        DE1: str = ...
        GLL: str = ...
        OUTSIDE: str = ...
        STAGE_US1: str = ...
        STAGE_US2: str = ...
        STAGE_AU1: str = ...
        STAGE_BR1: str = ...
        STAGE_IE1: str = ...
        STAGE_JP1: str = ...
        STAGE_SG1: str = ...
        STAGE_IN1: str = ...
        STAGE_DE1: str = ...
        DEV_US1: str = ...
        DEV_US2: str = ...
    class ProcessingState:
        COMPLETE: str = ...
        IN_PROGRESS: str = ...
    class EdgeLocation:
        ASHBURN: str = ...
        DUBLIN: str = ...
        FRANKFURT: str = ...
        SINGAPORE: str = ...
        SYDNEY: str = ...
        SAO_PAULO: str = ...
        ROAMING: str = ...
        UMATILLA: str = ...
        TOKYO: str = ...
    def __init__(self, version: Any, payload: Any, room_sid: Optional[Any] = ...) -> None: ...
    @property
    def account_sid(self): ...
    @property
    def room_sid(self): ...
    @property
    def room_name(self): ...
    @property
    def create_time(self): ...
    @property
    def end_time(self): ...
    @property
    def room_type(self): ...
    @property
    def room_status(self): ...
    @property
    def status_callback(self): ...
    @property
    def status_callback_method(self): ...
    @property
    def created_method(self): ...
    @property
    def end_reason(self): ...
    @property
    def max_participants(self): ...
    @property
    def unique_participants(self): ...
    @property
    def unique_participant_identities(self): ...
    @property
    def concurrent_participants(self): ...
    @property
    def max_concurrent_participants(self): ...
    @property
    def codecs(self): ...
    @property
    def media_region(self): ...
    @property
    def duration_sec(self): ...
    @property
    def total_participant_duration_sec(self): ...
    @property
    def total_recording_duration_sec(self): ...
    @property
    def processing_state(self): ...
    @property
    def recording_enabled(self): ...
    @property
    def edge_location(self): ...
    @property
    def url(self): ...
    @property
    def links(self): ...
    def fetch(self): ...
    @property
    def participants(self): ...
