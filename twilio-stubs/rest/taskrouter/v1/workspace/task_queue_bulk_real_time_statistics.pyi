from twilio.base import deserialize as deserialize, values as values
from twilio.base.instance_resource import InstanceResource as InstanceResource
from twilio.base.list_resource import ListResource as ListResource
from twilio.base.page import Page as Page

class TaskQueueBulkRealTimeStatisticsList(ListResource):
    def __init__(self, version, workspace_sid) -> None: ...
    def create(self): ...

class TaskQueueBulkRealTimeStatisticsPage(Page):
    def __init__(self, version, response, solution) -> None: ...
    def get_instance(self, payload): ...

class TaskQueueBulkRealTimeStatisticsInstance(InstanceResource):
    def __init__(self, version, payload, workspace_sid) -> None: ...
    @property
    def account_sid(self): ...
    @property
    def workspace_sid(self): ...
    @property
    def task_queue_data(self): ...
    @property
    def task_queue_response_count(self): ...
    @property
    def url(self): ...
