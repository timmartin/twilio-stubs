from _typeshed import Incomplete
from twilio.base import deserialize as deserialize, values as values
from twilio.base.instance_context import InstanceContext as InstanceContext
from twilio.base.instance_resource import InstanceResource as InstanceResource
from twilio.base.list_resource import ListResource as ListResource
from twilio.base.page import Page as Page
from twilio.rest.insights.v1.conference.conference_participant import ConferenceParticipantList as ConferenceParticipantList

class ConferenceList(ListResource):
    def __init__(self, version) -> None: ...
    def stream(self, conference_sid=..., friendly_name=..., status=..., created_after=..., created_before=..., mixer_region=..., tags=..., subaccount=..., detected_issues=..., end_reason=..., limit: Incomplete | None = ..., page_size: Incomplete | None = ...): ...
    def list(self, conference_sid=..., friendly_name=..., status=..., created_after=..., created_before=..., mixer_region=..., tags=..., subaccount=..., detected_issues=..., end_reason=..., limit: Incomplete | None = ..., page_size: Incomplete | None = ...): ...
    def page(self, conference_sid=..., friendly_name=..., status=..., created_after=..., created_before=..., mixer_region=..., tags=..., subaccount=..., detected_issues=..., end_reason=..., page_token=..., page_number=..., page_size=...): ...
    def get_page(self, target_url): ...
    def get(self, conference_sid): ...
    def __call__(self, conference_sid): ...

class ConferencePage(Page):
    def __init__(self, version, response, solution) -> None: ...
    def get_instance(self, payload): ...

class ConferenceContext(InstanceContext):
    def __init__(self, version, conference_sid) -> None: ...
    def fetch(self): ...
    @property
    def conference_participants(self): ...

class ConferenceInstance(InstanceResource):
    class ConferenceStatus:
        IN_PROGRESS: str
        NOT_STARTED: str
        COMPLETED: str
        SUMMARY_TIMEOUT: str
    class ConferenceEndReason:
        LAST_PARTICIPANT_LEFT: str
        CONFERENCE_ENDED_VIA_API: str
        PARTICIPANT_WITH_END_CONFERENCE_ON_EXIT_LEFT: str
        LAST_PARTICIPANT_KICKED: str
        PARTICIPANT_WITH_END_CONFERENCE_ON_EXIT_KICKED: str
    class Region:
        US1: str
        AU1: str
        BR1: str
        IE1: str
        JP1: str
        SG1: str
        DE1: str
    class Tag:
        INVALID_REQUESTED_REGION: str
        DUPLICATE_IDENTITY: str
        START_FAILURE: str
        REGION_CONFIGURATION_ISSUES: str
        QUALITY_WARNINGS: str
        PARTICIPANT_BEHAVIOR_ISSUES: str
        HIGH_PACKET_LOSS: str
        HIGH_JITTER: str
        HIGH_LATENCY: str
        LOW_MOS: str
        DETECTED_SILENCE: str
    class ProcessingState:
        COMPLETE: str
        IN_PROGRESS: str
        TIMEOUT: str
    def __init__(self, version, payload, conference_sid: Incomplete | None = ...) -> None: ...
    @property
    def conference_sid(self): ...
    @property
    def account_sid(self): ...
    @property
    def friendly_name(self): ...
    @property
    def create_time(self): ...
    @property
    def start_time(self): ...
    @property
    def end_time(self): ...
    @property
    def duration_seconds(self): ...
    @property
    def connect_duration_seconds(self): ...
    @property
    def status(self): ...
    @property
    def max_participants(self): ...
    @property
    def max_concurrent_participants(self): ...
    @property
    def unique_participants(self): ...
    @property
    def end_reason(self): ...
    @property
    def ended_by(self): ...
    @property
    def mixer_region(self): ...
    @property
    def mixer_region_requested(self): ...
    @property
    def recording_enabled(self): ...
    @property
    def detected_issues(self): ...
    @property
    def tags(self): ...
    @property
    def tag_info(self): ...
    @property
    def processing_state(self): ...
    @property
    def url(self): ...
    @property
    def links(self): ...
    def fetch(self): ...
    @property
    def conference_participants(self): ...
