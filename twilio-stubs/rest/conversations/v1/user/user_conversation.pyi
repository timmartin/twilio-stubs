from _typeshed import Incomplete
from twilio.base import deserialize as deserialize, serialize as serialize, values as values
from twilio.base.instance_context import InstanceContext as InstanceContext
from twilio.base.instance_resource import InstanceResource as InstanceResource
from twilio.base.list_resource import ListResource as ListResource
from twilio.base.page import Page as Page

class UserConversationList(ListResource):
    def __init__(self, version, user_sid) -> None: ...
    def stream(self, limit: Incomplete | None = ..., page_size: Incomplete | None = ...): ...
    def list(self, limit: Incomplete | None = ..., page_size: Incomplete | None = ...): ...
    def page(self, page_token=..., page_number=..., page_size=...): ...
    def get_page(self, target_url): ...
    def get(self, conversation_sid): ...
    def __call__(self, conversation_sid): ...

class UserConversationPage(Page):
    def __init__(self, version, response, solution) -> None: ...
    def get_instance(self, payload): ...

class UserConversationContext(InstanceContext):
    def __init__(self, version, user_sid, conversation_sid) -> None: ...
    def update(self, notification_level=..., last_read_timestamp=..., last_read_message_index=...): ...
    def delete(self): ...
    def fetch(self): ...

class UserConversationInstance(InstanceResource):
    class NotificationLevel:
        DEFAULT: str
        MUTED: str
    class State:
        INACTIVE: str
        ACTIVE: str
        CLOSED: str
    def __init__(self, version, payload, user_sid, conversation_sid: Incomplete | None = ...) -> None: ...
    @property
    def account_sid(self): ...
    @property
    def chat_service_sid(self): ...
    @property
    def conversation_sid(self): ...
    @property
    def unread_messages_count(self): ...
    @property
    def last_read_message_index(self): ...
    @property
    def participant_sid(self): ...
    @property
    def user_sid(self): ...
    @property
    def friendly_name(self): ...
    @property
    def conversation_state(self): ...
    @property
    def timers(self): ...
    @property
    def attributes(self): ...
    @property
    def date_created(self): ...
    @property
    def date_updated(self): ...
    @property
    def created_by(self): ...
    @property
    def notification_level(self): ...
    @property
    def unique_name(self): ...
    @property
    def url(self): ...
    @property
    def links(self): ...
    def update(self, notification_level=..., last_read_timestamp=..., last_read_message_index=...): ...
    def delete(self): ...
    def fetch(self): ...