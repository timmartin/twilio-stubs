from twilio.base.version import Version as Version
from twilio.rest.pricing.v2.country import CountryList as CountryList
from twilio.rest.pricing.v2.number import NumberList as NumberList
from twilio.rest.pricing.v2.voice import VoiceList as VoiceList

class V2(Version):
    version: str
    def __init__(self, domain) -> None: ...
    @property
    def countries(self): ...
    @property
    def numbers(self): ...
    @property
    def voice(self): ...
