from _typeshed import Incomplete
from twilio.base import deserialize as deserialize, values as values
from twilio.base.instance_context import InstanceContext as InstanceContext
from twilio.base.instance_resource import InstanceResource as InstanceResource
from twilio.base.list_resource import ListResource as ListResource
from twilio.base.page import Page as Page
from twilio.rest.supersim.v1.sim.billing_period import BillingPeriodList as BillingPeriodList
from twilio.rest.supersim.v1.sim.sim_ip_address import SimIpAddressList as SimIpAddressList

class SimList(ListResource):
    def __init__(self, version) -> None: ...
    def create(self, iccid, registration_code): ...
    def stream(self, status=..., fleet=..., iccid=..., limit: Incomplete | None = ..., page_size: Incomplete | None = ...): ...
    def list(self, status=..., fleet=..., iccid=..., limit: Incomplete | None = ..., page_size: Incomplete | None = ...): ...
    def page(self, status=..., fleet=..., iccid=..., page_token=..., page_number=..., page_size=...): ...
    def get_page(self, target_url): ...
    def get(self, sid): ...
    def __call__(self, sid): ...

class SimPage(Page):
    def __init__(self, version, response, solution) -> None: ...
    def get_instance(self, payload): ...

class SimContext(InstanceContext):
    def __init__(self, version, sid) -> None: ...
    def fetch(self): ...
    def update(self, unique_name=..., status=..., fleet=..., callback_url=..., callback_method=..., account_sid=...): ...
    @property
    def billing_periods(self): ...
    @property
    def sim_ip_addresses(self): ...

class SimInstance(InstanceResource):
    class Status:
        NEW: str
        READY: str
        ACTIVE: str
        INACTIVE: str
        SCHEDULED: str
    class StatusUpdate:
        READY: str
        ACTIVE: str
        INACTIVE: str
    def __init__(self, version, payload, sid: Incomplete | None = ...) -> None: ...
    @property
    def sid(self): ...
    @property
    def unique_name(self): ...
    @property
    def account_sid(self): ...
    @property
    def iccid(self): ...
    @property
    def status(self): ...
    @property
    def fleet_sid(self): ...
    @property
    def date_created(self): ...
    @property
    def date_updated(self): ...
    @property
    def url(self): ...
    @property
    def links(self): ...
    def fetch(self): ...
    def update(self, unique_name=..., status=..., fleet=..., callback_url=..., callback_method=..., account_sid=...): ...
    @property
    def billing_periods(self): ...
    @property
    def sim_ip_addresses(self): ...