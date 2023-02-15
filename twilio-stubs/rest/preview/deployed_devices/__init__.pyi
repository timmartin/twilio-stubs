from twilio.base.version import Version as Version
from twilio.rest.preview.deployed_devices.fleet import FleetList as FleetList

class DeployedDevices(Version):
    version: str
    def __init__(self, domain) -> None: ...
    @property
    def fleets(self): ...
