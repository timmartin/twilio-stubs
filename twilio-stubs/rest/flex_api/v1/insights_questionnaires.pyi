from _typeshed import Incomplete
from twilio.base import serialize as serialize, values as values
from twilio.base.instance_context import InstanceContext as InstanceContext
from twilio.base.instance_resource import InstanceResource as InstanceResource
from twilio.base.list_resource import ListResource as ListResource
from twilio.base.page import Page as Page

class InsightsQuestionnairesList(ListResource):
    def __init__(self, version) -> None: ...
    def create(self, name, description=..., active=..., question_ids=..., token=...): ...
    def stream(self, include_inactive=..., token=..., limit: Incomplete | None = ..., page_size: Incomplete | None = ...): ...
    def list(self, include_inactive=..., token=..., limit: Incomplete | None = ..., page_size: Incomplete | None = ...): ...
    def page(self, include_inactive=..., token=..., page_token=..., page_number=..., page_size=...): ...
    def get_page(self, target_url): ...
    def get(self, id): ...
    def __call__(self, id): ...

class InsightsQuestionnairesPage(Page):
    def __init__(self, version, response, solution) -> None: ...
    def get_instance(self, payload): ...

class InsightsQuestionnairesContext(InstanceContext):
    def __init__(self, version, id) -> None: ...
    def update(self, active, name=..., description=..., question_ids=..., token=...): ...
    def delete(self, token=...): ...
    def fetch(self, token=...): ...

class InsightsQuestionnairesInstance(InstanceResource):
    def __init__(self, version, payload, id: Incomplete | None = ...) -> None: ...
    @property
    def account_sid(self): ...
    @property
    def id(self): ...
    @property
    def name(self): ...
    @property
    def description(self): ...
    @property
    def active(self): ...
    @property
    def questions(self): ...
    @property
    def url(self): ...
    def update(self, active, name=..., description=..., question_ids=..., token=...): ...
    def delete(self, token=...): ...
    def fetch(self, token=...): ...
