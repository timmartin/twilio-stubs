from twilio.base.domain import Domain as Domain
from twilio.rest.frontline_api.v1 import V1 as V1

class FrontlineApi(Domain):
    base_url: str
    def __init__(self, twilio) -> None: ...
    @property
    def v1(self): ...
    @property
    def users(self): ...
