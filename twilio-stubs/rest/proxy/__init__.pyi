from twilio.base.domain import Domain as Domain
from twilio.rest.proxy.v1 import V1 as V1

class Proxy(Domain):
    base_url: str
    def __init__(self, twilio) -> None: ...
    @property
    def v1(self): ...
    @property
    def services(self): ...
