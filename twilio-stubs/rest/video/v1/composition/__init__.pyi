from _typeshed import Incomplete
from twilio.base import deserialize as deserialize, serialize as serialize, values as values
from twilio.base.instance_context import InstanceContext as InstanceContext
from twilio.base.instance_resource import InstanceResource as InstanceResource
from twilio.base.list_resource import ListResource as ListResource
from twilio.base.page import Page as Page

class CompositionList(ListResource):
    def __init__(self, version) -> None: ...
    def stream(self, status=..., date_created_after=..., date_created_before=..., room_sid=..., limit: Incomplete | None = ..., page_size: Incomplete | None = ...): ...
    def list(self, status=..., date_created_after=..., date_created_before=..., room_sid=..., limit: Incomplete | None = ..., page_size: Incomplete | None = ...): ...
    def page(self, status=..., date_created_after=..., date_created_before=..., room_sid=..., page_token=..., page_number=..., page_size=...): ...
    def get_page(self, target_url): ...
    def create(self, room_sid, video_layout=..., audio_sources=..., audio_sources_excluded=..., resolution=..., format=..., status_callback=..., status_callback_method=..., trim=...): ...
    def get(self, sid): ...
    def __call__(self, sid): ...

class CompositionPage(Page):
    def __init__(self, version, response, solution) -> None: ...
    def get_instance(self, payload): ...

class CompositionContext(InstanceContext):
    def __init__(self, version, sid) -> None: ...
    def fetch(self): ...
    def delete(self): ...

class CompositionInstance(InstanceResource):
    class Status:
        ENQUEUED: str
        PROCESSING: str
        COMPLETED: str
        DELETED: str
        FAILED: str
    class Format:
        MP4: str
        WEBM: str
    def __init__(self, version, payload, sid: Incomplete | None = ...) -> None: ...
    @property
    def account_sid(self): ...
    @property
    def status(self): ...
    @property
    def date_created(self): ...
    @property
    def date_completed(self): ...
    @property
    def date_deleted(self): ...
    @property
    def sid(self): ...
    @property
    def room_sid(self): ...
    @property
    def audio_sources(self): ...
    @property
    def audio_sources_excluded(self): ...
    @property
    def video_layout(self): ...
    @property
    def resolution(self): ...
    @property
    def trim(self): ...
    @property
    def format(self): ...
    @property
    def bitrate(self): ...
    @property
    def size(self): ...
    @property
    def duration(self): ...
    @property
    def media_external_location(self): ...
    @property
    def status_callback(self): ...
    @property
    def status_callback_method(self): ...
    @property
    def url(self): ...
    @property
    def links(self): ...
    def fetch(self): ...
    def delete(self): ...
