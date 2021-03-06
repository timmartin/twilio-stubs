from twilio.base import deserialize as deserialize, serialize as serialize, values as values
from twilio.base.instance_context import InstanceContext as InstanceContext
from twilio.base.instance_resource import InstanceResource as InstanceResource
from twilio.base.list_resource import ListResource as ListResource
from twilio.base.page import Page as Page
from twilio.rest.api.v2010.account.conference.participant import ParticipantList as ParticipantList
from twilio.rest.api.v2010.account.conference.recording import RecordingList as RecordingList
from typing import Any, Optional

class ConferenceList(ListResource):
    def __init__(self, version: Any, account_sid: Any) -> None: ...
    def stream(self, date_created_before: Any = ..., date_created: Any = ..., date_created_after: Any = ..., date_updated_before: Any = ..., date_updated: Any = ..., date_updated_after: Any = ..., friendly_name: Any = ..., status: Any = ..., limit: Optional[Any] = ..., page_size: Optional[Any] = ...): ...
    def list(self, date_created_before: Any = ..., date_created: Any = ..., date_created_after: Any = ..., date_updated_before: Any = ..., date_updated: Any = ..., date_updated_after: Any = ..., friendly_name: Any = ..., status: Any = ..., limit: Optional[Any] = ..., page_size: Optional[Any] = ...): ...
    def page(self, date_created_before: Any = ..., date_created: Any = ..., date_created_after: Any = ..., date_updated_before: Any = ..., date_updated: Any = ..., date_updated_after: Any = ..., friendly_name: Any = ..., status: Any = ..., page_token: Any = ..., page_number: Any = ..., page_size: Any = ...): ...
    def get_page(self, target_url: Any): ...
    def get(self, sid: Any): ...
    def __call__(self, sid: Any): ...

class ConferencePage(Page):
    def __init__(self, version: Any, response: Any, solution: Any) -> None: ...
    def get_instance(self, payload: Any): ...

class ConferenceContext(InstanceContext):
    def __init__(self, version: Any, account_sid: Any, sid: Any) -> None: ...
    def fetch(self): ...
    def update(self, status: Any = ..., announce_url: Any = ..., announce_method: Any = ...): ...
    @property
    def participants(self): ...
    @property
    def recordings(self): ...

class ConferenceInstance(InstanceResource):
    class Status:
        INIT: str = ...
        IN_PROGRESS: str = ...
        COMPLETED: str = ...
    class UpdateStatus:
        COMPLETED: str = ...
    class ReasonConferenceEnded:
        CONFERENCE_ENDED_VIA_API: str = ...
        PARTICIPANT_WITH_END_CONFERENCE_ON_EXIT_LEFT: str = ...
        PARTICIPANT_WITH_END_CONFERENCE_ON_EXIT_KICKED: str = ...
        LAST_PARTICIPANT_KICKED: str = ...
        LAST_PARTICIPANT_LEFT: str = ...
    def __init__(self, version: Any, payload: Any, account_sid: Any, sid: Optional[Any] = ...) -> None: ...
    @property
    def account_sid(self): ...
    @property
    def date_created(self): ...
    @property
    def date_updated(self): ...
    @property
    def api_version(self): ...
    @property
    def friendly_name(self): ...
    @property
    def region(self): ...
    @property
    def sid(self): ...
    @property
    def status(self): ...
    @property
    def uri(self): ...
    @property
    def subresource_uris(self): ...
    @property
    def reason_conference_ended(self): ...
    @property
    def call_sid_ending_conference(self): ...
    def fetch(self): ...
    def update(self, status: Any = ..., announce_url: Any = ..., announce_method: Any = ...): ...
    @property
    def participants(self): ...
    @property
    def recordings(self): ...
