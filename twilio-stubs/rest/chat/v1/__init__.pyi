from twilio.base.version import Version as Version
from twilio.rest.chat.v1.credential import CredentialList as CredentialList
from twilio.rest.chat.v1.service import ServiceList as ServiceList

class V1(Version):
    version: str
    def __init__(self, domain) -> None: ...
    @property
    def credentials(self): ...
    @property
    def services(self): ...
