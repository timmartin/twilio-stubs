from _typeshed import Incomplete
from twilio.base import deserialize as deserialize, values as values
from twilio.base.instance_resource import InstanceResource as InstanceResource
from twilio.base.list_resource import ListResource as ListResource
from twilio.base.page import Page as Page

class DependentPhoneNumberList(ListResource):
    def __init__(self, version, account_sid, address_sid) -> None: ...
    def stream(self, limit: Incomplete | None = ..., page_size: Incomplete | None = ...): ...
    def list(self, limit: Incomplete | None = ..., page_size: Incomplete | None = ...): ...
    def page(self, page_token=..., page_number=..., page_size=...): ...
    def get_page(self, target_url): ...

class DependentPhoneNumberPage(Page):
    def __init__(self, version, response, solution) -> None: ...
    def get_instance(self, payload): ...

class DependentPhoneNumberInstance(InstanceResource):
    class AddressRequirement:
        NONE: str
        ANY: str
        LOCAL: str
        FOREIGN: str
    class EmergencyStatus:
        ACTIVE: str
        INACTIVE: str
    def __init__(self, version, payload, account_sid, address_sid) -> None: ...
    @property
    def sid(self): ...
    @property
    def account_sid(self): ...
    @property
    def friendly_name(self): ...
    @property
    def phone_number(self): ...
    @property
    def voice_url(self): ...
    @property
    def voice_method(self): ...
    @property
    def voice_fallback_method(self): ...
    @property
    def voice_fallback_url(self): ...
    @property
    def voice_caller_id_lookup(self): ...
    @property
    def date_created(self): ...
    @property
    def date_updated(self): ...
    @property
    def sms_fallback_method(self): ...
    @property
    def sms_fallback_url(self): ...
    @property
    def sms_method(self): ...
    @property
    def sms_url(self): ...
    @property
    def address_requirements(self): ...
    @property
    def capabilities(self): ...
    @property
    def status_callback(self): ...
    @property
    def status_callback_method(self): ...
    @property
    def api_version(self): ...
    @property
    def sms_application_sid(self): ...
    @property
    def voice_application_sid(self): ...
    @property
    def trunk_sid(self): ...
    @property
    def emergency_status(self): ...
    @property
    def emergency_address_sid(self): ...
    @property
    def uri(self): ...
