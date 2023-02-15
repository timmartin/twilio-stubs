from twilio.base import deserialize as deserialize, values as values
from twilio.base.instance_context import InstanceContext as InstanceContext
from twilio.base.instance_resource import InstanceResource as InstanceResource
from twilio.base.list_resource import ListResource as ListResource
from twilio.base.page import Page as Page

class WorkersRealTimeStatisticsList(ListResource):
    def __init__(self, version, workspace_sid) -> None: ...
    def get(self): ...
    def __call__(self): ...

class WorkersRealTimeStatisticsPage(Page):
    def __init__(self, version, response, solution) -> None: ...
    def get_instance(self, payload): ...

class WorkersRealTimeStatisticsContext(InstanceContext):
    def __init__(self, version, workspace_sid) -> None: ...
    def fetch(self, task_channel=...): ...

class WorkersRealTimeStatisticsInstance(InstanceResource):
    def __init__(self, version, payload, workspace_sid) -> None: ...
    @property
    def account_sid(self): ...
    @property
    def activity_statistics(self): ...
    @property
    def total_workers(self): ...
    @property
    def workspace_sid(self): ...
    @property
    def url(self): ...
    def fetch(self, task_channel=...): ...
