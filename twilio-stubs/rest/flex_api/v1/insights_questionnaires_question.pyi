from _typeshed import Incomplete
from twilio.base import deserialize as deserialize, serialize as serialize, values as values
from twilio.base.instance_context import InstanceContext as InstanceContext
from twilio.base.instance_resource import InstanceResource as InstanceResource
from twilio.base.list_resource import ListResource as ListResource
from twilio.base.page import Page as Page

class InsightsQuestionnairesQuestionList(ListResource):
    def __init__(self, version) -> None: ...
    def create(self, category_id, question, description, answer_set_id, allow_na, token=...): ...
    def stream(self, category_id=..., token=..., limit: Incomplete | None = ..., page_size: Incomplete | None = ...): ...
    def list(self, category_id=..., token=..., limit: Incomplete | None = ..., page_size: Incomplete | None = ...): ...
    def page(self, category_id=..., token=..., page_token=..., page_number=..., page_size=...): ...
    def get_page(self, target_url): ...
    def get(self, question_id): ...
    def __call__(self, question_id): ...

class InsightsQuestionnairesQuestionPage(Page):
    def __init__(self, version, response, solution) -> None: ...
    def get_instance(self, payload): ...

class InsightsQuestionnairesQuestionContext(InstanceContext):
    def __init__(self, version, question_id) -> None: ...
    def update(self, allow_na, category_id=..., question=..., description=..., answer_set_id=..., token=...): ...
    def delete(self, token=...): ...

class InsightsQuestionnairesQuestionInstance(InstanceResource):
    def __init__(self, version, payload, question_id: Incomplete | None = ...) -> None: ...
    @property
    def account_sid(self): ...
    @property
    def question_id(self): ...
    @property
    def question(self): ...
    @property
    def description(self): ...
    @property
    def category(self): ...
    @property
    def answer_set_id(self): ...
    @property
    def allow_na(self): ...
    @property
    def usage(self): ...
    @property
    def url(self): ...
    def update(self, allow_na, category_id=..., question=..., description=..., answer_set_id=..., token=...): ...
    def delete(self, token=...): ...
