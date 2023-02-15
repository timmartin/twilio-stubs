from twilio.base.version import Version as Version
from twilio.rest.messaging.v1.brand_registration import BrandRegistrationList as BrandRegistrationList
from twilio.rest.messaging.v1.deactivation import DeactivationsList as DeactivationsList
from twilio.rest.messaging.v1.domain_cert import DomainCertsList as DomainCertsList
from twilio.rest.messaging.v1.domain_config import DomainConfigList as DomainConfigList
from twilio.rest.messaging.v1.external_campaign import ExternalCampaignList as ExternalCampaignList
from twilio.rest.messaging.v1.service import ServiceList as ServiceList
from twilio.rest.messaging.v1.tollfree_verification import TollfreeVerificationList as TollfreeVerificationList
from twilio.rest.messaging.v1.usecase import UsecaseList as UsecaseList

class V1(Version):
    version: str
    def __init__(self, domain) -> None: ...
    @property
    def brand_registrations(self): ...
    @property
    def deactivations(self): ...
    @property
    def domain_certs(self): ...
    @property
    def domain_config(self): ...
    @property
    def external_campaign(self): ...
    @property
    def services(self): ...
    @property
    def tollfree_verifications(self): ...
    @property
    def usecases(self): ...
