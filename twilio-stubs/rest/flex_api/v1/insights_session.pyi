from twilio.base import values as values
from twilio.base.instance_context import InstanceContext as InstanceContext
from twilio.base.instance_resource import InstanceResource as InstanceResource
from twilio.base.list_resource import ListResource as ListResource
from twilio.base.page import Page as Page

class InsightsSessionList(ListResource):
    def __init__(self, version) -> None: ...
    def get(self): ...
    def __call__(self): ...

class InsightsSessionPage(Page):
    def __init__(self, version, response, solution) -> None: ...
    def get_instance(self, payload): ...

class InsightsSessionContext(InstanceContext):
    def __init__(self, version) -> None: ...
    def create(self, authorization=...): ...

class InsightsSessionInstance(InstanceResource):
    def __init__(self, version, payload) -> None: ...
    @property
    def workspace_id(self): ...
    @property
    def session_expiry(self): ...
    @property
    def session_id(self): ...
    @property
    def base_url(self): ...
    @property
    def url(self): ...
    def create(self, authorization=...): ...
