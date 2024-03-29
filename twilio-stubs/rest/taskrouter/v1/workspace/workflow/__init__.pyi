from _typeshed import Incomplete
from twilio.base import deserialize as deserialize, values as values
from twilio.base.instance_context import InstanceContext as InstanceContext
from twilio.base.instance_resource import InstanceResource as InstanceResource
from twilio.base.list_resource import ListResource as ListResource
from twilio.base.page import Page as Page
from twilio.rest.taskrouter.v1.workspace.workflow.workflow_cumulative_statistics import WorkflowCumulativeStatisticsList as WorkflowCumulativeStatisticsList
from twilio.rest.taskrouter.v1.workspace.workflow.workflow_real_time_statistics import WorkflowRealTimeStatisticsList as WorkflowRealTimeStatisticsList
from twilio.rest.taskrouter.v1.workspace.workflow.workflow_statistics import WorkflowStatisticsList as WorkflowStatisticsList

class WorkflowList(ListResource):
    def __init__(self, version, workspace_sid) -> None: ...
    def stream(self, friendly_name=..., limit: Incomplete | None = ..., page_size: Incomplete | None = ...): ...
    def list(self, friendly_name=..., limit: Incomplete | None = ..., page_size: Incomplete | None = ...): ...
    def page(self, friendly_name=..., page_token=..., page_number=..., page_size=...): ...
    def get_page(self, target_url): ...
    def create(self, friendly_name, configuration, assignment_callback_url=..., fallback_assignment_callback_url=..., task_reservation_timeout=...): ...
    def get(self, sid): ...
    def __call__(self, sid): ...

class WorkflowPage(Page):
    def __init__(self, version, response, solution) -> None: ...
    def get_instance(self, payload): ...

class WorkflowContext(InstanceContext):
    def __init__(self, version, workspace_sid, sid) -> None: ...
    def fetch(self): ...
    def update(self, friendly_name=..., assignment_callback_url=..., fallback_assignment_callback_url=..., configuration=..., task_reservation_timeout=..., re_evaluate_tasks=...): ...
    def delete(self): ...
    @property
    def statistics(self): ...
    @property
    def real_time_statistics(self): ...
    @property
    def cumulative_statistics(self): ...

class WorkflowInstance(InstanceResource):
    def __init__(self, version, payload, workspace_sid, sid: Incomplete | None = ...) -> None: ...
    @property
    def account_sid(self): ...
    @property
    def assignment_callback_url(self): ...
    @property
    def configuration(self): ...
    @property
    def date_created(self): ...
    @property
    def date_updated(self): ...
    @property
    def document_content_type(self): ...
    @property
    def fallback_assignment_callback_url(self): ...
    @property
    def friendly_name(self): ...
    @property
    def sid(self): ...
    @property
    def task_reservation_timeout(self): ...
    @property
    def workspace_sid(self): ...
    @property
    def url(self): ...
    @property
    def links(self): ...
    def fetch(self): ...
    def update(self, friendly_name=..., assignment_callback_url=..., fallback_assignment_callback_url=..., configuration=..., task_reservation_timeout=..., re_evaluate_tasks=...): ...
    def delete(self): ...
    @property
    def statistics(self): ...
    @property
    def real_time_statistics(self): ...
    @property
    def cumulative_statistics(self): ...
