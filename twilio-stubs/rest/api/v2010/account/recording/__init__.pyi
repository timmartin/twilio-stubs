from _typeshed import Incomplete
from twilio.base import deserialize as deserialize, serialize as serialize, values as values
from twilio.base.instance_context import InstanceContext as InstanceContext
from twilio.base.instance_resource import InstanceResource as InstanceResource
from twilio.base.list_resource import ListResource as ListResource
from twilio.base.page import Page as Page
from twilio.rest.api.v2010.account.recording.add_on_result import AddOnResultList as AddOnResultList
from twilio.rest.api.v2010.account.recording.transcription import TranscriptionList as TranscriptionList

class RecordingList(ListResource):
    def __init__(self, version, account_sid) -> None: ...
    def stream(self, date_created_before=..., date_created=..., date_created_after=..., call_sid=..., conference_sid=..., include_soft_deleted=..., limit: Incomplete | None = ..., page_size: Incomplete | None = ...): ...
    def list(self, date_created_before=..., date_created=..., date_created_after=..., call_sid=..., conference_sid=..., include_soft_deleted=..., limit: Incomplete | None = ..., page_size: Incomplete | None = ...): ...
    def page(self, date_created_before=..., date_created=..., date_created_after=..., call_sid=..., conference_sid=..., include_soft_deleted=..., page_token=..., page_number=..., page_size=...): ...
    def get_page(self, target_url): ...
    def get(self, sid): ...
    def __call__(self, sid): ...

class RecordingPage(Page):
    def __init__(self, version, response, solution) -> None: ...
    def get_instance(self, payload): ...

class RecordingContext(InstanceContext):
    def __init__(self, version, account_sid, sid) -> None: ...
    def fetch(self, include_soft_deleted=...): ...
    def delete(self): ...
    @property
    def transcriptions(self): ...
    @property
    def add_on_results(self): ...

class RecordingInstance(InstanceResource):
    class Status:
        IN_PROGRESS: str
        PAUSED: str
        STOPPED: str
        PROCESSING: str
        COMPLETED: str
        ABSENT: str
        DELETED: str
    class Source:
        DIALVERB: str
        CONFERENCE: str
        OUTBOUNDAPI: str
        TRUNKING: str
        RECORDVERB: str
        STARTCALLRECORDINGAPI: str
        STARTCONFERENCERECORDINGAPI: str
    def __init__(self, version, payload, account_sid, sid: Incomplete | None = ...) -> None: ...
    @property
    def account_sid(self): ...
    @property
    def api_version(self): ...
    @property
    def call_sid(self): ...
    @property
    def conference_sid(self): ...
    @property
    def date_created(self): ...
    @property
    def date_updated(self): ...
    @property
    def start_time(self): ...
    @property
    def duration(self): ...
    @property
    def sid(self): ...
    @property
    def price(self): ...
    @property
    def price_unit(self): ...
    @property
    def status(self): ...
    @property
    def channels(self): ...
    @property
    def source(self): ...
    @property
    def error_code(self): ...
    @property
    def uri(self): ...
    @property
    def encryption_details(self): ...
    @property
    def subresource_uris(self): ...
    @property
    def media_url(self): ...
    def fetch(self, include_soft_deleted=...): ...
    def delete(self): ...
    @property
    def transcriptions(self): ...
    @property
    def add_on_results(self): ...
