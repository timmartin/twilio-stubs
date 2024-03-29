from _typeshed import Incomplete
from twilio.base import deserialize as deserialize, values as values
from twilio.base.instance_context import InstanceContext as InstanceContext
from twilio.base.instance_resource import InstanceResource as InstanceResource
from twilio.base.list_resource import ListResource as ListResource
from twilio.base.page import Page as Page
from twilio.rest.trusthub.v1.customer_profiles.customer_profiles_channel_endpoint_assignment import CustomerProfilesChannelEndpointAssignmentList as CustomerProfilesChannelEndpointAssignmentList
from twilio.rest.trusthub.v1.customer_profiles.customer_profiles_entity_assignments import CustomerProfilesEntityAssignmentsList as CustomerProfilesEntityAssignmentsList
from twilio.rest.trusthub.v1.customer_profiles.customer_profiles_evaluations import CustomerProfilesEvaluationsList as CustomerProfilesEvaluationsList

class CustomerProfilesList(ListResource):
    def __init__(self, version) -> None: ...
    def create(self, friendly_name, email, policy_sid, status_callback=...): ...
    def stream(self, status=..., friendly_name=..., policy_sid=..., limit: Incomplete | None = ..., page_size: Incomplete | None = ...): ...
    def list(self, status=..., friendly_name=..., policy_sid=..., limit: Incomplete | None = ..., page_size: Incomplete | None = ...): ...
    def page(self, status=..., friendly_name=..., policy_sid=..., page_token=..., page_number=..., page_size=...): ...
    def get_page(self, target_url): ...
    def get(self, sid): ...
    def __call__(self, sid): ...

class CustomerProfilesPage(Page):
    def __init__(self, version, response, solution) -> None: ...
    def get_instance(self, payload): ...

class CustomerProfilesContext(InstanceContext):
    def __init__(self, version, sid) -> None: ...
    def fetch(self): ...
    def update(self, status=..., status_callback=..., friendly_name=..., email=...): ...
    def delete(self): ...
    @property
    def customer_profiles_entity_assignments(self): ...
    @property
    def customer_profiles_evaluations(self): ...
    @property
    def customer_profiles_channel_endpoint_assignment(self): ...

class CustomerProfilesInstance(InstanceResource):
    class Status:
        DRAFT: str
        PENDING_REVIEW: str
        IN_REVIEW: str
        TWILIO_REJECTED: str
        TWILIO_APPROVED: str
    class EndUserType:
        INDIVIDUAL: str
        BUSINESS: str
    def __init__(self, version, payload, sid: Incomplete | None = ...) -> None: ...
    @property
    def sid(self): ...
    @property
    def account_sid(self): ...
    @property
    def policy_sid(self): ...
    @property
    def friendly_name(self): ...
    @property
    def status(self): ...
    @property
    def valid_until(self): ...
    @property
    def email(self): ...
    @property
    def status_callback(self): ...
    @property
    def date_created(self): ...
    @property
    def date_updated(self): ...
    @property
    def url(self): ...
    @property
    def links(self): ...
    def fetch(self): ...
    def update(self, status=..., status_callback=..., friendly_name=..., email=...): ...
    def delete(self): ...
    @property
    def customer_profiles_entity_assignments(self): ...
    @property
    def customer_profiles_evaluations(self): ...
    @property
    def customer_profiles_channel_endpoint_assignment(self): ...
