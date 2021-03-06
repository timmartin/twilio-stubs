from twilio.base.domain import Domain as Domain
from twilio.rest.supersim.v1 import V1 as V1
from typing import Any

class Supersim(Domain):
    base_url: str = ...
    def __init__(self, twilio: Any) -> None: ...
    @property
    def v1(self): ...
    @property
    def commands(self): ...
    @property
    def fleets(self): ...
    @property
    def networks(self): ...
    @property
    def network_access_profiles(self): ...
    @property
    def sims(self): ...
    @property
    def usage_records(self): ...
