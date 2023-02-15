from twilio.base.domain import Domain as Domain
from twilio.rest.microvisor.v1 import V1 as V1

class Microvisor(Domain):
    base_url: str
    def __init__(self, twilio) -> None: ...
    @property
    def v1(self): ...
    @property
    def account_configs(self): ...
    @property
    def account_secrets(self): ...
    @property
    def apps(self): ...
    @property
    def devices(self): ...