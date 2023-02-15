from twilio.base.version import Version as Version
from twilio.rest.frontline_api.v1.user import UserList as UserList

class V1(Version):
    version: str
    def __init__(self, domain) -> None: ...
    @property
    def users(self): ...
