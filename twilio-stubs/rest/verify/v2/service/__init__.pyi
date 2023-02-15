from _typeshed import Incomplete
from twilio.base import deserialize as deserialize, values as values
from twilio.base.instance_context import InstanceContext as InstanceContext
from twilio.base.instance_resource import InstanceResource as InstanceResource
from twilio.base.list_resource import ListResource as ListResource
from twilio.base.page import Page as Page
from twilio.rest.verify.v2.service.access_token import AccessTokenList as AccessTokenList
from twilio.rest.verify.v2.service.entity import EntityList as EntityList
from twilio.rest.verify.v2.service.messaging_configuration import MessagingConfigurationList as MessagingConfigurationList
from twilio.rest.verify.v2.service.rate_limit import RateLimitList as RateLimitList
from twilio.rest.verify.v2.service.verification import VerificationList as VerificationList
from twilio.rest.verify.v2.service.verification_check import VerificationCheckList as VerificationCheckList
from twilio.rest.verify.v2.service.webhook import WebhookList as WebhookList

class ServiceList(ListResource):
    def __init__(self, version) -> None: ...
    def create(self, friendly_name, code_length=..., lookup_enabled=..., skip_sms_to_landlines=..., dtmf_input_required=..., tts_name=..., psd2_enabled=..., do_not_share_warning_enabled=..., custom_code_enabled=..., push_include_date=..., push_apn_credential_sid=..., push_fcm_credential_sid=..., totp_issuer=..., totp_time_step=..., totp_code_length=..., totp_skew=..., default_template_sid=...): ...
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
    def fetch(self): ...
    def delete(self): ...
    def update(self, friendly_name=..., code_length=..., lookup_enabled=..., skip_sms_to_landlines=..., dtmf_input_required=..., tts_name=..., psd2_enabled=..., do_not_share_warning_enabled=..., custom_code_enabled=..., push_include_date=..., push_apn_credential_sid=..., push_fcm_credential_sid=..., totp_issuer=..., totp_time_step=..., totp_code_length=..., totp_skew=..., default_template_sid=...): ...
    @property
    def verifications(self): ...
    @property
    def verification_checks(self): ...
    @property
    def rate_limits(self): ...
    @property
    def messaging_configurations(self): ...
    @property
    def entities(self): ...
    @property
    def webhooks(self): ...
    @property
    def access_tokens(self): ...

class ServiceInstance(InstanceResource):
    def __init__(self, version, payload, sid: Incomplete | None = ...) -> None: ...
    @property
    def sid(self): ...
    @property
    def account_sid(self): ...
    @property
    def friendly_name(self): ...
    @property
    def code_length(self): ...
    @property
    def lookup_enabled(self): ...
    @property
    def psd2_enabled(self): ...
    @property
    def skip_sms_to_landlines(self): ...
    @property
    def dtmf_input_required(self): ...
    @property
    def tts_name(self): ...
    @property
    def do_not_share_warning_enabled(self): ...
    @property
    def custom_code_enabled(self): ...
    @property
    def push(self): ...
    @property
    def totp(self): ...
    @property
    def default_template_sid(self): ...
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
    def update(self, friendly_name=..., code_length=..., lookup_enabled=..., skip_sms_to_landlines=..., dtmf_input_required=..., tts_name=..., psd2_enabled=..., do_not_share_warning_enabled=..., custom_code_enabled=..., push_include_date=..., push_apn_credential_sid=..., push_fcm_credential_sid=..., totp_issuer=..., totp_time_step=..., totp_code_length=..., totp_skew=..., default_template_sid=...): ...
    @property
    def verifications(self): ...
    @property
    def verification_checks(self): ...
    @property
    def rate_limits(self): ...
    @property
    def messaging_configurations(self): ...
    @property
    def entities(self): ...
    @property
    def webhooks(self): ...
    @property
    def access_tokens(self): ...
