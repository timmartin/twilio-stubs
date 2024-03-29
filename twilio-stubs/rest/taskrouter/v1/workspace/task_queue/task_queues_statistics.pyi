from _typeshed import Incomplete
from twilio.base import serialize as serialize, values as values
from twilio.base.instance_resource import InstanceResource as InstanceResource
from twilio.base.list_resource import ListResource as ListResource
from twilio.base.page import Page as Page

class TaskQueuesStatisticsList(ListResource):
    def __init__(self, version, workspace_sid) -> None: ...
    def stream(self, end_date=..., friendly_name=..., minutes=..., start_date=..., task_channel=..., split_by_wait_time=..., limit: Incomplete | None = ..., page_size: Incomplete | None = ...): ...
    def list(self, end_date=..., friendly_name=..., minutes=..., start_date=..., task_channel=..., split_by_wait_time=..., limit: Incomplete | None = ..., page_size: Incomplete | None = ...): ...
    def page(self, end_date=..., friendly_name=..., minutes=..., start_date=..., task_channel=..., split_by_wait_time=..., page_token=..., page_number=..., page_size=...): ...
    def get_page(self, target_url): ...

class TaskQueuesStatisticsPage(Page):
    def __init__(self, version, response, solution) -> None: ...
    def get_instance(self, payload): ...

class TaskQueuesStatisticsInstance(InstanceResource):
    def __init__(self, version, payload, workspace_sid) -> None: ...
    @property
    def account_sid(self): ...
    @property
    def cumulative(self): ...
    @property
    def realtime(self): ...
    @property
    def task_queue_sid(self): ...
    @property
    def workspace_sid(self): ...
