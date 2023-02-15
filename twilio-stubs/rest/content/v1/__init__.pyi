from twilio.base.version import Version as Version
from twilio.rest.content.v1.content import ContentList as ContentList
from twilio.rest.content.v1.legacy_content import LegacyContentList as LegacyContentList

class V1(Version):
    version: str
    def __init__(self, domain) -> None: ...
    @property
    def contents(self): ...
    @property
    def legacy_contents(self): ...
