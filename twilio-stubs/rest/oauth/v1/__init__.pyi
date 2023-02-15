from twilio.base.version import Version as Version
from twilio.rest.oauth.v1.device_code import DeviceCodeList as DeviceCodeList
from twilio.rest.oauth.v1.oauth import OauthList as OauthList
from twilio.rest.oauth.v1.openid_discovery import OpenidDiscoveryList as OpenidDiscoveryList
from twilio.rest.oauth.v1.token import TokenList as TokenList
from twilio.rest.oauth.v1.user_info import UserInfoList as UserInfoList

class V1(Version):
    version: str
    def __init__(self, domain) -> None: ...
    @property
    def oauth(self): ...
    @property
    def device_code(self): ...
    @property
    def openid_discovery(self): ...
    @property
    def token(self): ...
    @property
    def user_info(self): ...
