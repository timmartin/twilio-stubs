from _typeshed import Incomplete
from twilio.base import deserialize as deserialize, serialize as serialize, values as values
from twilio.base.instance_context import InstanceContext as InstanceContext
from twilio.base.instance_resource import InstanceResource as InstanceResource
from twilio.base.list_resource import ListResource as ListResource
from twilio.base.page import Page as Page
from twilio.rest.taskrouter.v1.workspace.task.reservation import ReservationList as ReservationList

class TaskList(ListResource):
    def __init__(self, version, workspace_sid) -> None: ...
    def stream(self, priority=..., assignment_status=..., workflow_sid=..., workflow_name=..., task_queue_sid=..., task_queue_name=..., evaluate_task_attributes=..., ordering=..., has_addons=..., limit: Incomplete | None = ..., page_size: Incomplete | None = ...): ...
    def list(self, priority=..., assignment_status=..., workflow_sid=..., workflow_name=..., task_queue_sid=..., task_queue_name=..., evaluate_task_attributes=..., ordering=..., has_addons=..., limit: Incomplete | None = ..., page_size: Incomplete | None = ...): ...
    def page(self, priority=..., assignment_status=..., workflow_sid=..., workflow_name=..., task_queue_sid=..., task_queue_name=..., evaluate_task_attributes=..., ordering=..., has_addons=..., page_token=..., page_number=..., page_size=...): ...
    def get_page(self, target_url): ...
    def create(self, timeout=..., priority=..., task_channel=..., workflow_sid=..., attributes=...): ...
    def get(self, sid): ...
    def __call__(self, sid): ...

class TaskPage(Page):
    def __init__(self, version, response, solution) -> None: ...
    def get_instance(self, payload): ...

class TaskContext(InstanceContext):
    def __init__(self, version, workspace_sid, sid) -> None: ...
    def fetch(self): ...
    def update(self, attributes=..., assignment_status=..., reason=..., priority=..., task_channel=..., if_match=...): ...
    def delete(self, if_match=...): ...
    @property
    def reservations(self): ...

class TaskInstance(InstanceResource):
    class Status:
        PENDING: str
        RESERVED: str
        ASSIGNED: str
        CANCELED: str
        COMPLETED: str
        WRAPPING: str
    def __init__(self, version, payload, workspace_sid, sid: Incomplete | None = ...) -> None: ...
    @property
    def account_sid(self): ...
    @property
    def age(self): ...
    @property
    def assignment_status(self): ...
    @property
    def attributes(self): ...
    @property
    def addons(self): ...
    @property
    def date_created(self): ...
    @property
    def date_updated(self): ...
    @property
    def task_queue_entered_date(self): ...
    @property
    def priority(self): ...
    @property
    def reason(self): ...
    @property
    def sid(self): ...
    @property
    def task_queue_sid(self): ...
    @property
    def task_queue_friendly_name(self): ...
    @property
    def task_channel_sid(self): ...
    @property
    def task_channel_unique_name(self): ...
    @property
    def timeout(self): ...
    @property
    def workflow_sid(self): ...
    @property
    def workflow_friendly_name(self): ...
    @property
    def workspace_sid(self): ...
    @property
    def url(self): ...
    @property
    def links(self): ...
    def fetch(self): ...
    def update(self, attributes=..., assignment_status=..., reason=..., priority=..., task_channel=..., if_match=...): ...
    def delete(self, if_match=...): ...
    @property
    def reservations(self): ...
