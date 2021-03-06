from twilio.base import deserialize as deserialize, serialize as serialize, values as values
from twilio.base.instance_context import InstanceContext as InstanceContext
from twilio.base.instance_resource import InstanceResource as InstanceResource
from twilio.base.list_resource import ListResource as ListResource
from twilio.base.page import Page as Page
from twilio.rest.fax.v1.fax.fax_media import FaxMediaList as FaxMediaList
from typing import Any, Optional

class FaxList(ListResource):
    def __init__(self, version: Any) -> None: ...
    def stream(self, from_: Any = ..., to: Any = ..., date_created_on_or_before: Any = ..., date_created_after: Any = ..., limit: Optional[Any] = ..., page_size: Optional[Any] = ...): ...
    def list(self, from_: Any = ..., to: Any = ..., date_created_on_or_before: Any = ..., date_created_after: Any = ..., limit: Optional[Any] = ..., page_size: Optional[Any] = ...): ...
    def page(self, from_: Any = ..., to: Any = ..., date_created_on_or_before: Any = ..., date_created_after: Any = ..., page_token: Any = ..., page_number: Any = ..., page_size: Any = ...): ...
    def get_page(self, target_url: Any): ...
    def create(self, to: Any, media_url: Any, quality: Any = ..., status_callback: Any = ..., from_: Any = ..., sip_auth_username: Any = ..., sip_auth_password: Any = ..., store_media: Any = ..., ttl: Any = ...): ...
    def get(self, sid: Any): ...
    def __call__(self, sid: Any): ...

class FaxPage(Page):
    def __init__(self, version: Any, response: Any, solution: Any) -> None: ...
    def get_instance(self, payload: Any): ...

class FaxContext(InstanceContext):
    def __init__(self, version: Any, sid: Any) -> None: ...
    def fetch(self): ...
    def update(self, status: Any = ...): ...
    def delete(self): ...
    @property
    def media(self): ...

class FaxInstance(InstanceResource):
    class Direction:
        INBOUND: str = ...
        OUTBOUND: str = ...
    class Quality:
        STANDARD: str = ...
        FINE: str = ...
        SUPERFINE: str = ...
    class Status:
        QUEUED: str = ...
        PROCESSING: str = ...
        SENDING: str = ...
        DELIVERED: str = ...
        RECEIVING: str = ...
        RECEIVED: str = ...
        NO_ANSWER: str = ...
        BUSY: str = ...
        FAILED: str = ...
        CANCELED: str = ...
    class UpdateStatus:
        CANCELED: str = ...
    def __init__(self, version: Any, payload: Any, sid: Optional[Any] = ...) -> None: ...
    @property
    def sid(self): ...
    @property
    def account_sid(self): ...
    @property
    def from_(self): ...
    @property
    def to(self): ...
    @property
    def quality(self): ...
    @property
    def media_sid(self): ...
    @property
    def media_url(self): ...
    @property
    def num_pages(self): ...
    @property
    def duration(self): ...
    @property
    def status(self): ...
    @property
    def direction(self): ...
    @property
    def api_version(self): ...
    @property
    def price(self): ...
    @property
    def price_unit(self): ...
    @property
    def date_created(self): ...
    @property
    def date_updated(self): ...
    @property
    def links(self): ...
    @property
    def url(self): ...
    def fetch(self): ...
    def update(self, status: Any = ...): ...
    def delete(self): ...
    @property
    def media(self): ...
