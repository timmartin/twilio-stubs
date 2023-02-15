from twilio.base.version import Version as Version
from twilio.rest.routes.v2.phone_number import PhoneNumberList as PhoneNumberList
from twilio.rest.routes.v2.sip_domain import SipDomainList as SipDomainList
from twilio.rest.routes.v2.trunk import TrunkList as TrunkList

class V2(Version):
    version: str
    def __init__(self, domain) -> None: ...
    @property
    def phone_numbers(self): ...
    @property
    def sip_domains(self): ...
    @property
    def trunks(self): ...
