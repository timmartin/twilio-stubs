from _typeshed import Incomplete
from twilio.base import deserialize as deserialize, values as values
from twilio.base.instance_resource import InstanceResource as InstanceResource
from twilio.base.list_resource import ListResource as ListResource
from twilio.base.page import Page as Page

class ParticipantConversationList(ListResource):
    def __init__(self, version, chat_service_sid) -> None: ...
    def stream(self, identity=..., address=..., limit: Incomplete | None = ..., page_size: Incomplete | None = ...): ...
    def list(self, identity=..., address=..., limit: Incomplete | None = ..., page_size: Incomplete | None = ...): ...
    def page(self, identity=..., address=..., page_token=..., page_number=..., page_size=...): ...
    def get_page(self, target_url): ...

class ParticipantConversationPage(Page):
    def __init__(self, version, response, solution) -> None: ...
    def get_instance(self, payload): ...

class ParticipantConversationInstance(InstanceResource):
    class State:
        INACTIVE: str
        ACTIVE: str
        CLOSED: str
    def __init__(self, version, payload, chat_service_sid) -> None: ...
    @property
    def account_sid(self): ...
    @property
    def chat_service_sid(self): ...
    @property
    def participant_sid(self): ...
    @property
    def participant_user_sid(self): ...
    @property
    def participant_identity(self): ...
    @property
    def participant_messaging_binding(self): ...
    @property
    def conversation_sid(self): ...
    @property
    def conversation_unique_name(self): ...
    @property
    def conversation_friendly_name(self): ...
    @property
    def conversation_attributes(self): ...
    @property
    def conversation_date_created(self): ...
    @property
    def conversation_date_updated(self): ...
    @property
    def conversation_created_by(self): ...
    @property
    def conversation_state(self): ...
    @property
    def conversation_timers(self): ...
    @property
    def links(self): ...
