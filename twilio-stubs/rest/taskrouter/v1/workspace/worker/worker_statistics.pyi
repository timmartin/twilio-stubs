from twilio.base import serialize as serialize, values as values
from twilio.base.instance_context import InstanceContext as InstanceContext
from twilio.base.instance_resource import InstanceResource as InstanceResource
from twilio.base.list_resource import ListResource as ListResource
from twilio.base.page import Page as Page

class WorkerStatisticsList(ListResource):
    def __init__(self, version, workspace_sid, worker_sid) -> None: ...
    def get(self): ...
    def __call__(self): ...

class WorkerStatisticsPage(Page):
    def __init__(self, version, response, solution) -> None: ...
    def get_instance(self, payload): ...

class WorkerStatisticsContext(InstanceContext):
    def __init__(self, version, workspace_sid, worker_sid) -> None: ...
    def fetch(self, minutes=..., start_date=..., end_date=..., task_channel=...): ...

class WorkerStatisticsInstance(InstanceResource):
    def __init__(self, version, payload, workspace_sid, worker_sid) -> None: ...
    @property
    def account_sid(self): ...
    @property
    def cumulative(self): ...
    @property
    def worker_sid(self): ...
    @property
    def workspace_sid(self): ...
    @property
    def url(self): ...
    def fetch(self, minutes=..., start_date=..., end_date=..., task_channel=...): ...
