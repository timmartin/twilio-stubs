from twilio.base.version import Version as Version
from twilio.rest.sync.v1.service import ServiceList as ServiceList

class V1(Version):
    version: str
    def __init__(self, domain) -> None: ...
    @property
    def services(self): ...
