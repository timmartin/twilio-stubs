from twilio.base import deserialize as deserialize, serialize as serialize, values as values
from twilio.base.instance_context import InstanceContext as InstanceContext
from twilio.base.instance_resource import InstanceResource as InstanceResource
from twilio.base.list_resource import ListResource as ListResource
from twilio.base.page import Page as Page
from twilio.rest.preview.understand.assistant.assistant_fallback_actions import AssistantFallbackActionsList as AssistantFallbackActionsList
from twilio.rest.preview.understand.assistant.assistant_initiation_actions import AssistantInitiationActionsList as AssistantInitiationActionsList
from twilio.rest.preview.understand.assistant.dialogue import DialogueList as DialogueList
from twilio.rest.preview.understand.assistant.field_type import FieldTypeList as FieldTypeList
from twilio.rest.preview.understand.assistant.model_build import ModelBuildList as ModelBuildList
from twilio.rest.preview.understand.assistant.query import QueryList as QueryList
from twilio.rest.preview.understand.assistant.style_sheet import StyleSheetList as StyleSheetList
from twilio.rest.preview.understand.assistant.task import TaskList as TaskList
from typing import Any, Optional

class AssistantList(ListResource):
    def __init__(self, version: Any) -> None: ...
    def stream(self, limit: Optional[Any] = ..., page_size: Optional[Any] = ...): ...
    def list(self, limit: Optional[Any] = ..., page_size: Optional[Any] = ...): ...
    def page(self, page_token: Any = ..., page_number: Any = ..., page_size: Any = ...): ...
    def get_page(self, target_url: Any): ...
    def create(self, friendly_name: Any = ..., log_queries: Any = ..., unique_name: Any = ..., callback_url: Any = ..., callback_events: Any = ..., fallback_actions: Any = ..., initiation_actions: Any = ..., style_sheet: Any = ...): ...
    def get(self, sid: Any): ...
    def __call__(self, sid: Any): ...

class AssistantPage(Page):
    def __init__(self, version: Any, response: Any, solution: Any) -> None: ...
    def get_instance(self, payload: Any): ...

class AssistantContext(InstanceContext):
    def __init__(self, version: Any, sid: Any) -> None: ...
    def fetch(self): ...
    def update(self, friendly_name: Any = ..., log_queries: Any = ..., unique_name: Any = ..., callback_url: Any = ..., callback_events: Any = ..., fallback_actions: Any = ..., initiation_actions: Any = ..., style_sheet: Any = ...): ...
    def delete(self): ...
    @property
    def field_types(self): ...
    @property
    def tasks(self): ...
    @property
    def model_builds(self): ...
    @property
    def queries(self): ...
    @property
    def assistant_fallback_actions(self): ...
    @property
    def assistant_initiation_actions(self): ...
    @property
    def dialogues(self): ...
    @property
    def style_sheet(self): ...

class AssistantInstance(InstanceResource):
    def __init__(self, version: Any, payload: Any, sid: Optional[Any] = ...) -> None: ...
    @property
    def account_sid(self): ...
    @property
    def date_created(self): ...
    @property
    def date_updated(self): ...
    @property
    def friendly_name(self): ...
    @property
    def latest_model_build_sid(self): ...
    @property
    def links(self): ...
    @property
    def log_queries(self): ...
    @property
    def sid(self): ...
    @property
    def unique_name(self): ...
    @property
    def url(self): ...
    @property
    def callback_url(self): ...
    @property
    def callback_events(self): ...
    def fetch(self): ...
    def update(self, friendly_name: Any = ..., log_queries: Any = ..., unique_name: Any = ..., callback_url: Any = ..., callback_events: Any = ..., fallback_actions: Any = ..., initiation_actions: Any = ..., style_sheet: Any = ...): ...
    def delete(self): ...
    @property
    def field_types(self): ...
    @property
    def tasks(self): ...
    @property
    def model_builds(self): ...
    @property
    def queries(self): ...
    @property
    def assistant_fallback_actions(self): ...
    @property
    def assistant_initiation_actions(self): ...
    @property
    def dialogues(self): ...
    @property
    def style_sheet(self): ...
