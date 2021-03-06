from twilio.base import deserialize as deserialize, serialize as serialize, values as values
from twilio.base.instance_context import InstanceContext as InstanceContext
from twilio.base.instance_resource import InstanceResource as InstanceResource
from twilio.base.list_resource import ListResource as ListResource
from twilio.base.page import Page as Page
from typing import Any, Optional

class ParticipantList(ListResource):
    def __init__(self, version: Any, chat_service_sid: Any, conversation_sid: Any) -> None: ...
    def create(self, identity: Any = ..., messaging_binding_address: Any = ..., messaging_binding_proxy_address: Any = ..., date_created: Any = ..., date_updated: Any = ..., attributes: Any = ..., messaging_binding_projected_address: Any = ..., role_sid: Any = ..., x_twilio_webhook_enabled: Any = ...): ...
    def stream(self, limit: Optional[Any] = ..., page_size: Optional[Any] = ...): ...
    def list(self, limit: Optional[Any] = ..., page_size: Optional[Any] = ...): ...
    def page(self, page_token: Any = ..., page_number: Any = ..., page_size: Any = ...): ...
    def get_page(self, target_url: Any): ...
    def get(self, sid: Any): ...
    def __call__(self, sid: Any): ...

class ParticipantPage(Page):
    def __init__(self, version: Any, response: Any, solution: Any) -> None: ...
    def get_instance(self, payload: Any): ...

class ParticipantContext(InstanceContext):
    def __init__(self, version: Any, chat_service_sid: Any, conversation_sid: Any, sid: Any) -> None: ...
    def update(self, date_created: Any = ..., date_updated: Any = ..., identity: Any = ..., attributes: Any = ..., role_sid: Any = ..., messaging_binding_proxy_address: Any = ..., messaging_binding_projected_address: Any = ..., x_twilio_webhook_enabled: Any = ...): ...
    def delete(self, x_twilio_webhook_enabled: Any = ...): ...
    def fetch(self): ...

class ParticipantInstance(InstanceResource):
    class WebhookEnabledType:
        TRUE: str = ...
        FALSE: str = ...
    def __init__(self, version: Any, payload: Any, chat_service_sid: Any, conversation_sid: Any, sid: Optional[Any] = ...) -> None: ...
    @property
    def account_sid(self): ...
    @property
    def chat_service_sid(self): ...
    @property
    def conversation_sid(self): ...
    @property
    def sid(self): ...
    @property
    def identity(self): ...
    @property
    def attributes(self): ...
    @property
    def messaging_binding(self): ...
    @property
    def role_sid(self): ...
    @property
    def date_created(self): ...
    @property
    def date_updated(self): ...
    @property
    def url(self): ...
    def update(self, date_created: Any = ..., date_updated: Any = ..., identity: Any = ..., attributes: Any = ..., role_sid: Any = ..., messaging_binding_proxy_address: Any = ..., messaging_binding_projected_address: Any = ..., x_twilio_webhook_enabled: Any = ...): ...
    def delete(self, x_twilio_webhook_enabled: Any = ...): ...
    def fetch(self): ...
