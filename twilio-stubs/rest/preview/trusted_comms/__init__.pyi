from twilio.base.version import Version as Version
from twilio.rest.preview.trusted_comms.branded_call import BrandedCallList as BrandedCallList
from twilio.rest.preview.trusted_comms.branded_channel import BrandedChannelList as BrandedChannelList
from twilio.rest.preview.trusted_comms.brands_information import BrandsInformationList as BrandsInformationList
from twilio.rest.preview.trusted_comms.business import BusinessList as BusinessList
from twilio.rest.preview.trusted_comms.cps import CpsList as CpsList
from twilio.rest.preview.trusted_comms.current_call import CurrentCallList as CurrentCallList
from twilio.rest.preview.trusted_comms.phone_call import PhoneCallList as PhoneCallList
from typing import Any

class TrustedComms(Version):
    version: str = ...
    def __init__(self, domain: Any) -> None: ...
    @property
    def branded_calls(self): ...
    @property
    def branded_channels(self): ...
    @property
    def brands_information(self): ...
    @property
    def businesses(self): ...
    @property
    def cps(self): ...
    @property
    def current_calls(self): ...
    @property
    def phone_calls(self): ...
