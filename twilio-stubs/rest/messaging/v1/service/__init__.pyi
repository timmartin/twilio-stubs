from _typeshed import Incomplete
from twilio.base import deserialize as deserialize, values as values
from twilio.base.instance_context import InstanceContext as InstanceContext
from twilio.base.instance_resource import InstanceResource as InstanceResource
from twilio.base.list_resource import ListResource as ListResource
from twilio.base.page import Page as Page
from twilio.rest.messaging.v1.service.alpha_sender import AlphaSenderList as AlphaSenderList
from twilio.rest.messaging.v1.service.phone_number import PhoneNumberList as PhoneNumberList
from twilio.rest.messaging.v1.service.short_code import ShortCodeList as ShortCodeList
from twilio.rest.messaging.v1.service.us_app_to_person import UsAppToPersonList as UsAppToPersonList
from twilio.rest.messaging.v1.service.us_app_to_person_usecase import UsAppToPersonUsecaseList as UsAppToPersonUsecaseList

class ServiceList(ListResource):
    def __init__(self, version) -> None: ...
    def create(self, friendly_name, inbound_request_url=..., inbound_method=..., fallback_url=..., fallback_method=..., status_callback=..., sticky_sender=..., mms_converter=..., smart_encoding=..., scan_message_content=..., fallback_to_long_code=..., area_code_geomatch=..., validity_period=..., synchronous_validation=..., usecase=..., use_inbound_webhook_on_number=...): ...
    def stream(self, limit: Incomplete | None = ..., page_size: Incomplete | None = ...): ...
    def list(self, limit: Incomplete | None = ..., page_size: Incomplete | None = ...): ...
    def page(self, page_token=..., page_number=..., page_size=...): ...
    def get_page(self, target_url): ...
    def get(self, sid): ...
    def __call__(self, sid): ...

class ServicePage(Page):
    def __init__(self, version, response, solution) -> None: ...
    def get_instance(self, payload): ...

class ServiceContext(InstanceContext):
    def __init__(self, version, sid) -> None: ...
    def update(self, friendly_name=..., inbound_request_url=..., inbound_method=..., fallback_url=..., fallback_method=..., status_callback=..., sticky_sender=..., mms_converter=..., smart_encoding=..., scan_message_content=..., fallback_to_long_code=..., area_code_geomatch=..., validity_period=..., synchronous_validation=..., usecase=..., use_inbound_webhook_on_number=...): ...
    def fetch(self): ...
    def delete(self): ...
    @property
    def phone_numbers(self): ...
    @property
    def short_codes(self): ...
    @property
    def alpha_senders(self): ...
    @property
    def us_app_to_person(self): ...
    @property
    def us_app_to_person_usecases(self): ...

class ServiceInstance(InstanceResource):
    class ScanMessageContent:
        INHERIT: str
        ENABLE: str
        DISABLE: str
    def __init__(self, version, payload, sid: Incomplete | None = ...) -> None: ...
    @property
    def sid(self): ...
    @property
    def account_sid(self): ...
    @property
    def friendly_name(self): ...
    @property
    def date_created(self): ...
    @property
    def date_updated(self): ...
    @property
    def inbound_request_url(self): ...
    @property
    def inbound_method(self): ...
    @property
    def fallback_url(self): ...
    @property
    def fallback_method(self): ...
    @property
    def status_callback(self): ...
    @property
    def sticky_sender(self): ...
    @property
    def mms_converter(self): ...
    @property
    def smart_encoding(self): ...
    @property
    def scan_message_content(self): ...
    @property
    def fallback_to_long_code(self): ...
    @property
    def area_code_geomatch(self): ...
    @property
    def synchronous_validation(self): ...
    @property
    def validity_period(self): ...
    @property
    def url(self): ...
    @property
    def links(self): ...
    @property
    def usecase(self): ...
    @property
    def us_app_to_person_registered(self): ...
    @property
    def use_inbound_webhook_on_number(self): ...
    def update(self, friendly_name=..., inbound_request_url=..., inbound_method=..., fallback_url=..., fallback_method=..., status_callback=..., sticky_sender=..., mms_converter=..., smart_encoding=..., scan_message_content=..., fallback_to_long_code=..., area_code_geomatch=..., validity_period=..., synchronous_validation=..., usecase=..., use_inbound_webhook_on_number=...): ...
    def fetch(self): ...
    def delete(self): ...
    @property
    def phone_numbers(self): ...
    @property
    def short_codes(self): ...
    @property
    def alpha_senders(self): ...
    @property
    def us_app_to_person(self): ...
    @property
    def us_app_to_person_usecases(self): ...
