from twilio.base.version import Version as Version
from twilio.rest.microvisor.v1.account_config import AccountConfigList as AccountConfigList
from twilio.rest.microvisor.v1.account_secret import AccountSecretList as AccountSecretList
from twilio.rest.microvisor.v1.app import AppList as AppList
from twilio.rest.microvisor.v1.device import DeviceList as DeviceList

class V1(Version):
    version: str
    def __init__(self, domain) -> None: ...
    @property
    def account_configs(self): ...
    @property
    def account_secrets(self): ...
    @property
    def apps(self): ...
    @property
    def devices(self): ...
