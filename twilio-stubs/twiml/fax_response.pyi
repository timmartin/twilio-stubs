from _typeshed import Incomplete
from twilio.twiml import TwiML as TwiML, format_language as format_language

class FaxResponse(TwiML):
    name: str
    def __init__(self, **kwargs) -> None: ...
    def receive(self, action: Incomplete | None = ..., method: Incomplete | None = ..., media_type: Incomplete | None = ..., page_size: Incomplete | None = ..., store_media: Incomplete | None = ..., **kwargs): ...

class Receive(TwiML):
    name: str
    def __init__(self, **kwargs) -> None: ...
