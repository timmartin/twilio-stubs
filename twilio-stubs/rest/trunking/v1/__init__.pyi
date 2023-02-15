from twilio.base.version import Version as Version
from twilio.rest.trunking.v1.trunk import TrunkList as TrunkList

class V1(Version):
    version: str
    def __init__(self, domain) -> None: ...
    @property
    def trunks(self): ...
