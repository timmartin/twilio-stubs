from twilio.base import values as values
from twilio.base.instance_context import InstanceContext as InstanceContext
from twilio.base.instance_resource import InstanceResource as InstanceResource
from twilio.base.list_resource import ListResource as ListResource
from twilio.base.page import Page as Page
from typing import Any, Optional

class RegulationList(ListResource):
    def __init__(self, version: Any) -> None: ...
    def stream(self, end_user_type: Any = ..., iso_country: Any = ..., number_type: Any = ..., limit: Optional[Any] = ..., page_size: Optional[Any] = ...): ...
    def list(self, end_user_type: Any = ..., iso_country: Any = ..., number_type: Any = ..., limit: Optional[Any] = ..., page_size: Optional[Any] = ...): ...
    def page(self, end_user_type: Any = ..., iso_country: Any = ..., number_type: Any = ..., page_token: Any = ..., page_number: Any = ..., page_size: Any = ...): ...
    def get_page(self, target_url: Any): ...
    def get(self, sid: Any): ...
    def __call__(self, sid: Any): ...

class RegulationPage(Page):
    def __init__(self, version: Any, response: Any, solution: Any) -> None: ...
    def get_instance(self, payload: Any): ...

class RegulationContext(InstanceContext):
    def __init__(self, version: Any, sid: Any) -> None: ...
    def fetch(self): ...

class RegulationInstance(InstanceResource):
    class EndUserType:
        INDIVIDUAL: str = ...
        BUSINESS: str = ...
    def __init__(self, version: Any, payload: Any, sid: Optional[Any] = ...) -> None: ...
    @property
    def sid(self): ...
    @property
    def friendly_name(self): ...
    @property
    def iso_country(self): ...
    @property
    def number_type(self): ...
    @property
    def end_user_type(self): ...
    @property
    def requirements(self): ...
    @property
    def url(self): ...
    def fetch(self): ...
