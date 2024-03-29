from _typeshed import Incomplete
from twilio.base import deserialize as deserialize, values as values
from twilio.base.instance_context import InstanceContext as InstanceContext
from twilio.base.instance_resource import InstanceResource as InstanceResource
from twilio.base.list_resource import ListResource as ListResource
from twilio.base.page import Page as Page

class PhoneNumberList(ListResource):
    def __init__(self, version) -> None: ...
    def get(self, phone_number): ...
    def __call__(self, phone_number): ...

class PhoneNumberPage(Page):
    def __init__(self, version, response, solution) -> None: ...
    def get_instance(self, payload): ...

class PhoneNumberContext(InstanceContext):
    def __init__(self, version, phone_number) -> None: ...
    def update(self, voice_region=..., friendly_name=...): ...
    def fetch(self): ...

class PhoneNumberInstance(InstanceResource):
    def __init__(self, version, payload, phone_number: Incomplete | None = ...) -> None: ...
    @property
    def phone_number(self): ...
    @property
    def url(self): ...
    @property
    def sid(self): ...
    @property
    def account_sid(self): ...
    @property
    def friendly_name(self): ...
    @property
    def voice_region(self): ...
    @property
    def date_created(self): ...
    @property
    def date_updated(self): ...
    def update(self, voice_region=..., friendly_name=...): ...
    def fetch(self): ...
