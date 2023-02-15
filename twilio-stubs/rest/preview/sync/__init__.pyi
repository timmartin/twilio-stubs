from twilio.base.version import Version as Version
from twilio.rest.preview.sync.service import ServiceList as ServiceList

class Sync(Version):
    version: str
    def __init__(self, domain) -> None: ...
    @property
    def services(self): ...
