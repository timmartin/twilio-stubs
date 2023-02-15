from twilio.base.version import Version as Version
from twilio.rest.preview.marketplace.available_add_on import AvailableAddOnList as AvailableAddOnList
from twilio.rest.preview.marketplace.installed_add_on import InstalledAddOnList as InstalledAddOnList

class Marketplace(Version):
    version: str
    def __init__(self, domain) -> None: ...
    @property
    def available_add_ons(self): ...
    @property
    def installed_add_ons(self): ...
