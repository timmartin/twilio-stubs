from twilio.base.version import Version as Version
from twilio.rest.preview.understand.assistant import AssistantList as AssistantList

class Understand(Version):
    version: str
    def __init__(self, domain) -> None: ...
    @property
    def assistants(self): ...
