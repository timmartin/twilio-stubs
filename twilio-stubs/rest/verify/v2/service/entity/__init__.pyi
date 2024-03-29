from _typeshed import Incomplete
from twilio.base import deserialize as deserialize, values as values
from twilio.base.instance_context import InstanceContext as InstanceContext
from twilio.base.instance_resource import InstanceResource as InstanceResource
from twilio.base.list_resource import ListResource as ListResource
from twilio.base.page import Page as Page
from twilio.rest.verify.v2.service.entity.challenge import ChallengeList as ChallengeList
from twilio.rest.verify.v2.service.entity.factor import FactorList as FactorList
from twilio.rest.verify.v2.service.entity.new_factor import NewFactorList as NewFactorList

class EntityList(ListResource):
    def __init__(self, version, service_sid) -> None: ...
    def create(self, identity): ...
    def stream(self, limit: Incomplete | None = ..., page_size: Incomplete | None = ...): ...
    def list(self, limit: Incomplete | None = ..., page_size: Incomplete | None = ...): ...
    def page(self, page_token=..., page_number=..., page_size=...): ...
    def get_page(self, target_url): ...
    def get(self, identity): ...
    def __call__(self, identity): ...

class EntityPage(Page):
    def __init__(self, version, response, solution) -> None: ...
    def get_instance(self, payload): ...

class EntityContext(InstanceContext):
    def __init__(self, version, service_sid, identity) -> None: ...
    def delete(self): ...
    def fetch(self): ...
    @property
    def factors(self): ...
    @property
    def new_factors(self): ...
    @property
    def challenges(self): ...

class EntityInstance(InstanceResource):
    def __init__(self, version, payload, service_sid, identity: Incomplete | None = ...) -> None: ...
    @property
    def sid(self): ...
    @property
    def identity(self): ...
    @property
    def account_sid(self): ...
    @property
    def service_sid(self): ...
    @property
    def date_created(self): ...
    @property
    def date_updated(self): ...
    @property
    def url(self): ...
    @property
    def links(self): ...
    def delete(self): ...
    def fetch(self): ...
    @property
    def factors(self): ...
    @property
    def new_factors(self): ...
    @property
    def challenges(self): ...
