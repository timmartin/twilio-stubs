from twilio.base import values as values
from twilio.base.instance_context import InstanceContext as InstanceContext
from twilio.base.instance_resource import InstanceResource as InstanceResource
from twilio.base.list_resource import ListResource as ListResource
from twilio.base.page import Page as Page
from typing import Any, Optional

class JobList(ListResource):
    def __init__(self, version: Any) -> None: ...
    def get(self, job_sid: Any): ...
    def __call__(self, job_sid: Any): ...

class JobPage(Page):
    def __init__(self, version: Any, response: Any, solution: Any) -> None: ...
    def get_instance(self, payload: Any): ...

class JobContext(InstanceContext):
    def __init__(self, version: Any, job_sid: Any) -> None: ...
    def fetch(self): ...
    def delete(self): ...

class JobInstance(InstanceResource):
    def __init__(self, version: Any, payload: Any, job_sid: Optional[Any] = ...) -> None: ...
    @property
    def resource_type(self): ...
    @property
    def friendly_name(self): ...
    @property
    def details(self): ...
    @property
    def start_day(self): ...
    @property
    def end_day(self): ...
    @property
    def job_sid(self): ...
    @property
    def webhook_url(self): ...
    @property
    def webhook_method(self): ...
    @property
    def email(self): ...
    @property
    def url(self): ...
    def fetch(self): ...
    def delete(self): ...
