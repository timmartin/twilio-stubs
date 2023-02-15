from twilio.base.version import Version as Version
from twilio.rest.lookups.v2.phone_number import PhoneNumberList as PhoneNumberList

class V2(Version):
    version: str
    def __init__(self, domain) -> None: ...
    @property
    def phone_numbers(self): ...
