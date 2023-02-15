from typing import Any
from _typeshed import Incomplete
from twilio.base.exceptions import TwilioException as TwilioException
from twilio.base.obsolete import obsolete_client as obsolete_client
from twilio.http.http_client import TwilioHttpClient as TwilioHttpClient
from twilio.rest.accounts import Accounts
from twilio.rest.api import Api
from twilio.rest.autopilot import Autopilot
from twilio.rest.chat import Chat
from twilio.rest.conversations import Conversations
from twilio.rest.events import Events
from twilio.rest.flex_api import FlexApi
from twilio.rest.insights import Insights
from twilio.rest.ip_messaging import IpMessaging
from twilio.rest.lookups import Lookups
from twilio.rest.media import Media
from twilio.rest.messaging import Messaging
from twilio.rest.microvisor import Microvisor
from twilio.rest.monitor import Monitor
from twilio.rest.notify import Notify
from twilio.rest.numbers import Numbers
from twilio.rest.preview import Preview
from twilio.rest.pricing import Pricing
from twilio.rest.proxy import Proxy
from twilio.rest.serverless import Serverless
from twilio.rest.studio import Studio
from twilio.rest.sync import Sync
from twilio.rest.taskrouter import Taskrouter
from twilio.rest.trunking import Trunking
from twilio.rest.trusthub import Trusthub
from twilio.rest.verify import Verify
from twilio.rest.video import Video
from twilio.rest.voice import Voice
from twilio.rest.wireless import Wireless
from twilio.rest.supersim import Supersim
from twilio.rest.bulkexports import Bulkexports
from twilio.rest.api.v2010.account.address import AddressList
from twilio.rest.api.v2010.account.application import ApplicationList
from twilio.rest.api.v2010.account.authorized_connect_app import AuthorizedConnectAppList
from twilio.rest.api.v2010.account.available_phone_number import AvailablePhoneNumberCountryList
from twilio.rest.api.v2010.account.balance import BalanceList
from twilio.rest.api.v2010.account.call import CallList
from twilio.rest.api.v2010.account.conference import ConferenceList
from twilio.rest.api.v2010.account.connect_app import ConnectAppList
from twilio.rest.api.v2010.account.incoming_phone_number import IncomingPhoneNumberList
from twilio.rest.api.v2010.account.key import KeyList
from twilio.rest.api.v2010.account.message import MessageList
from twilio.rest.api.v2010.account.new_key import NewKeyList
from twilio.rest.api.v2010.account.new_signing_key import NewSigningKeyList
from twilio.rest.api.v2010.account.notification import NotificationList
from twilio.rest.api.v2010.account.outgoing_caller_id import OutgoingCallerIdList
from twilio.rest.api.v2010.account.queue import QueueList
from twilio.rest.api.v2010.account.recording import RecordingList
from twilio.rest.api.v2010.account.short_code import ShortCodeList
from twilio.rest.api.v2010.account.signing_key import SigningKeyList
from twilio.rest.api.v2010.account.sip import SipList
from twilio.rest.api.v2010.account.token import TokenList
from twilio.rest.api.v2010.account.transcription import TranscriptionList
from twilio.rest.api.v2010.account.usage import UsageList
from twilio.rest.api.v2010.account.validation_request import ValidationRequestList


class Client:
    username: Incomplete
    password: Incomplete
    account_sid: Incomplete
    edge: Incomplete
    region: Incomplete
    user_agent_extensions: Incomplete
    auth: Incomplete

    http_client: TwilioHttpClient = ...

    def __init__(self, username: Incomplete | None = ..., password: Incomplete | None = ..., account_sid: Incomplete | None = ..., region: Incomplete | None = ..., http_client: Incomplete | None = ..., environment: Incomplete | None = ..., edge: Incomplete | None = ..., user_agent_extensions: Incomplete | None = ...) -> None: ...
    def request(self, method, uri, params: Incomplete | None = ..., data: Incomplete | None = ..., headers: Incomplete | None = ..., auth: Incomplete | None = ..., timeout: Incomplete | None = ..., allow_redirects: bool = ...): ...
    def get_hostname(self, uri): ...

    @property
    def accounts(self) -> Accounts: ...

    @property
    def api(self) -> Api: ...

    @property
    def autopilot(self) -> Autopilot: ...

    @property
    def chat(self) -> Chat: ...

    @property
    def content(self): ...

    @property
    def conversations(self) -> Conversations: ...

    @property
    def events(self) -> Events: ...

    @property
    def flex_api(self) -> FlexApi: ...

    @property
    def frontline_api(self): ...

    @property
    def insights(self) -> Insights: ...

    @property
    def ip_messaging(self) -> IpMessaging: ...

    @property
    def lookups(self) -> Lookups: ...

    @property
    def media(self) -> Media: ...

    @property
    def messaging(self) -> Messaging: ...

    @property
    def monitor(self) -> Monitor: ...

    @property
    def notify(self) -> Notify: ...

    @property
    def numbers(self) -> Numbers: ...

    @property
    def oauth(self): ...

    @property
    def preview(self) -> Preview: ...

    @property
    def pricing(self) -> Pricing: ...

    @property
    def proxy(self) -> Proxy: ...

    @property
    def routes(self): ...

    @property
    def serverless(self) -> Serverless: ...

    @property
    def studio(self) -> Studio: ...

    @property
    def sync(self) -> Sync: ...

    @property
    def taskrouter(self) -> Taskrouter: ...

    @property
    def trunking(self) -> Trunking: ...

    @property
    def trusthub(self) -> Trusthub: ...

    @property
    def verify(self) -> Verify: ...

    @property
    def video(self) -> Video: ...

    @property
    def voice(self) -> Voice: ...

    @property
    def wireless(self) -> Wireless: ...

    @property
    def supersim(self) -> Supersim: ...

    @property
    def bulkexports(self) -> Bulkexports: ...

    @property
    def microvisor(self) -> Microvisor: ...

    @property
    def addresses(self) -> AddressList: ...

    @property
    def applications(self) -> ApplicationList: ...

    @property
    def authorized_connect_apps(self) -> AuthorizedConnectAppList: ...

    @property
    def available_phone_numbers(self) -> AvailablePhoneNumberCountryList: ...

    @property
    def balance(self) -> BalanceList: ...

    @property
    def calls(self) -> CallList: ...

    @property
    def conferences(self) -> ConferenceList: ...

    @property
    def connect_apps(self) -> ConnectAppList: ...

    @property
    def incoming_phone_numbers(self) -> IncomingPhoneNumberList: ...

    @property
    def keys(self) -> KeyList: ...

    @property
    def messages(self) -> MessageList: ...

    @property
    def new_keys(self) -> NewKeyList: ...

    @property
    def new_signing_keys(self) -> NewSigningKeyList: ...

    @property
    def notifications(self) -> NotificationList: ...

    @property
    def outgoing_caller_ids(self) -> OutgoingCallerIdList: ...

    @property
    def queues(self) -> QueueList: ...

    @property
    def recordings(self) -> RecordingList: ...

    @property
    def signing_keys(self) -> SigningKeyList: ...

    @property
    def sip(self) -> SipList: ...

    @property
    def short_codes(self) -> ShortCodeList: ...

    @property
    def tokens(self) -> TokenList: ...

    @property
    def transcriptions(self) -> TranscriptionList: ...

    @property
    def usage(self) -> UsageList: ...

    @property
    def validation_requests(self) -> ValidationRequestList: ...

def TwilioClient(*args: Any) -> Any: ...

def TwilioRestClient(*args: Any) -> Any: ...

def TwilioIpMessagingClient(*args: Any) -> Any: ...

def TwilioLookupsClient(*args: Any) -> Any: ...

def TwilioMonitorClient(*args: Any) -> Any: ...

def TwilioPricingClient(*args: Any) -> Any: ...

def TwilioTaskRouterClient(*args: Any) -> Any: ...

def TwilioTrunkingClient(*args: Any) -> Any: ...
