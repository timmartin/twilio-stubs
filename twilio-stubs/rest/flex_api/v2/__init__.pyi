from twilio.base.version import Version as Version
from twilio.rest.flex_api.v2.web_channels import WebChannelsList as WebChannelsList

class V2(Version):
    version: str
    def __init__(self, domain) -> None: ...
    @property
    def web_channels(self): ...
