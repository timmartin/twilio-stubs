from _typeshed import Incomplete
from twilio.base import deserialize as deserialize, values as values
from twilio.base.instance_resource import InstanceResource as InstanceResource
from twilio.base.list_resource import ListResource as ListResource
from twilio.base.page import Page as Page

class SettingsUpdateList(ListResource):
    def __init__(self, version) -> None: ...
    def stream(self, sim=..., status=..., limit: Incomplete | None = ..., page_size: Incomplete | None = ...): ...
    def list(self, sim=..., status=..., limit: Incomplete | None = ..., page_size: Incomplete | None = ...): ...
    def page(self, sim=..., status=..., page_token=..., page_number=..., page_size=...): ...
    def get_page(self, target_url): ...

class SettingsUpdatePage(Page):
    def __init__(self, version, response, solution) -> None: ...
    def get_instance(self, payload): ...

class SettingsUpdateInstance(InstanceResource):
    class Status:
        SCHEDULED: str
        IN_PROGRESS: str
        SUCCESSFUL: str
        FAILED: str
    def __init__(self, version, payload) -> None: ...
    @property
    def sid(self): ...
    @property
    def iccid(self): ...
    @property
    def sim_sid(self): ...
    @property
    def status(self): ...
    @property
    def packages(self): ...
    @property
    def date_completed(self): ...
    @property
    def date_created(self): ...
    @property
    def date_updated(self): ...