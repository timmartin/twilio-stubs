from twilio.base.version import Version as Version
from twilio.rest.chat.v2.credential import CredentialList as CredentialList
from twilio.rest.chat.v2.service import ServiceList as ServiceList

class V2(Version):
    version: str
    def __init__(self, domain) -> None: ...
    @property
    def credentials(self): ...
    @property
    def services(self): ...
