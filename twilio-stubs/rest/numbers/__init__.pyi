from twilio.base.domain import Domain as Domain
from twilio.rest.numbers.v2 import V2 as V2

class Numbers(Domain):
    base_url: str
    def __init__(self, twilio) -> None: ...
    @property
    def v2(self): ...
    @property
    def regulatory_compliance(self): ...
