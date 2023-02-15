from twilio.base.version import Version as Version
from twilio.rest.preview.wireless.command import CommandList as CommandList
from twilio.rest.preview.wireless.rate_plan import RatePlanList as RatePlanList
from twilio.rest.preview.wireless.sim import SimList as SimList

class Wireless(Version):
    version: str
    def __init__(self, domain) -> None: ...
    @property
    def commands(self): ...
    @property
    def rate_plans(self): ...
    @property
    def sims(self): ...
