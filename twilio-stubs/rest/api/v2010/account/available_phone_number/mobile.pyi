from _typeshed import Incomplete
from twilio.base import deserialize as deserialize, values as values
from twilio.base.instance_resource import InstanceResource as InstanceResource
from twilio.base.list_resource import ListResource as ListResource
from twilio.base.page import Page as Page

class MobileList(ListResource):
    def __init__(self, version, account_sid, country_code) -> None: ...
    def stream(self, area_code=..., contains=..., sms_enabled=..., mms_enabled=..., voice_enabled=..., exclude_all_address_required=..., exclude_local_address_required=..., exclude_foreign_address_required=..., beta=..., near_number=..., near_lat_long=..., distance=..., in_postal_code=..., in_region=..., in_rate_center=..., in_lata=..., in_locality=..., fax_enabled=..., limit: Incomplete | None = ..., page_size: Incomplete | None = ...): ...
    def list(self, area_code=..., contains=..., sms_enabled=..., mms_enabled=..., voice_enabled=..., exclude_all_address_required=..., exclude_local_address_required=..., exclude_foreign_address_required=..., beta=..., near_number=..., near_lat_long=..., distance=..., in_postal_code=..., in_region=..., in_rate_center=..., in_lata=..., in_locality=..., fax_enabled=..., limit: Incomplete | None = ..., page_size: Incomplete | None = ...): ...
    def page(self, area_code=..., contains=..., sms_enabled=..., mms_enabled=..., voice_enabled=..., exclude_all_address_required=..., exclude_local_address_required=..., exclude_foreign_address_required=..., beta=..., near_number=..., near_lat_long=..., distance=..., in_postal_code=..., in_region=..., in_rate_center=..., in_lata=..., in_locality=..., fax_enabled=..., page_token=..., page_number=..., page_size=...): ...
    def get_page(self, target_url): ...

class MobilePage(Page):
    def __init__(self, version, response, solution) -> None: ...
    def get_instance(self, payload): ...

class MobileInstance(InstanceResource):
    def __init__(self, version, payload, account_sid, country_code) -> None: ...
    @property
    def friendly_name(self): ...
    @property
    def phone_number(self): ...
    @property
    def lata(self): ...
    @property
    def locality(self): ...
    @property
    def rate_center(self): ...
    @property
    def latitude(self): ...
    @property
    def longitude(self): ...
    @property
    def region(self): ...
    @property
    def postal_code(self): ...
    @property
    def iso_country(self): ...
    @property
    def address_requirements(self): ...
    @property
    def beta(self): ...
    @property
    def capabilities(self): ...
