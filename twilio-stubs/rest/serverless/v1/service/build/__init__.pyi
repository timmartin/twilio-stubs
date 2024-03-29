from _typeshed import Incomplete
from twilio.base import deserialize as deserialize, serialize as serialize, values as values
from twilio.base.instance_context import InstanceContext as InstanceContext
from twilio.base.instance_resource import InstanceResource as InstanceResource
from twilio.base.list_resource import ListResource as ListResource
from twilio.base.page import Page as Page
from twilio.rest.serverless.v1.service.build.build_status import BuildStatusList as BuildStatusList

class BuildList(ListResource):
    def __init__(self, version, service_sid) -> None: ...
    def stream(self, limit: Incomplete | None = ..., page_size: Incomplete | None = ...): ...
    def list(self, limit: Incomplete | None = ..., page_size: Incomplete | None = ...): ...
    def page(self, page_token=..., page_number=..., page_size=...): ...
    def get_page(self, target_url): ...
    def create(self, asset_versions=..., function_versions=..., dependencies=..., runtime=...): ...
    def get(self, sid): ...
    def __call__(self, sid): ...

class BuildPage(Page):
    def __init__(self, version, response, solution) -> None: ...
    def get_instance(self, payload): ...

class BuildContext(InstanceContext):
    def __init__(self, version, service_sid, sid) -> None: ...
    def fetch(self): ...
    def delete(self): ...
    @property
    def build_status(self): ...

class BuildInstance(InstanceResource):
    class Status:
        BUILDING: str
        COMPLETED: str
        FAILED: str
    class Runtime:
        NODE8: str
        NODE10: str
        NODE12: str
        NODE14: str
        NODE16: str
    def __init__(self, version, payload, service_sid, sid: Incomplete | None = ...) -> None: ...
    @property
    def sid(self): ...
    @property
    def account_sid(self): ...
    @property
    def service_sid(self): ...
    @property
    def status(self): ...
    @property
    def asset_versions(self): ...
    @property
    def function_versions(self): ...
    @property
    def dependencies(self): ...
    @property
    def runtime(self): ...
    @property
    def date_created(self): ...
    @property
    def date_updated(self): ...
    @property
    def url(self): ...
    @property
    def links(self): ...
    def fetch(self): ...
    def delete(self): ...
    @property
    def build_status(self): ...
