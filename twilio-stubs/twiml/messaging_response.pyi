from _typeshed import Incomplete
from twilio.twiml import TwiML as TwiML, format_language as format_language

class MessagingResponse(TwiML):
    name: str
    def __init__(self, **kwargs) -> None: ...
    def message(self, body: Incomplete | None = ..., to: Incomplete | None = ..., from_: Incomplete | None = ..., action: Incomplete | None = ..., method: Incomplete | None = ..., status_callback: Incomplete | None = ..., **kwargs): ...
    def redirect(self, url, method: Incomplete | None = ..., **kwargs): ...

class Redirect(TwiML):
    name: str
    value: Incomplete
    def __init__(self, url, **kwargs) -> None: ...

class Message(TwiML):
    name: str
    value: Incomplete
    def __init__(self, body: Incomplete | None = ..., **kwargs) -> None: ...
    def body(self, message, **kwargs): ...
    def media(self, url, **kwargs): ...

class Media(TwiML):
    name: str
    value: Incomplete
    def __init__(self, url, **kwargs) -> None: ...

class Body(TwiML):
    name: str
    value: Incomplete
    def __init__(self, message, **kwargs) -> None: ...
