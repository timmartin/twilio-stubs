from twilio.base.version import Version as Version
from twilio.rest.pricing.v1.messaging import MessagingList as MessagingList
from twilio.rest.pricing.v1.phone_number import PhoneNumberList as PhoneNumberList
from twilio.rest.pricing.v1.voice import VoiceList as VoiceList

class V1(Version):
    version: str
    def __init__(self, domain) -> None: ...
    @property
    def messaging(self): ...
    @property
    def phone_numbers(self): ...
    @property
    def voice(self): ...
