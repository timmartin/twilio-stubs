from twilio.base.version import Version as Version
from twilio.rest.chat.v3.channel import ChannelList as ChannelList

class V3(Version):
    version: str
    def __init__(self, domain) -> None: ...
    @property
    def channels(self): ...
