from twilio.base.version import Version as Version
from twilio.rest.api.v2010.account import AccountContext as AccountContext, AccountList as AccountList
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
from typing import Any

class V2010(Version):
    version: str = ...
    def __init__(self, domain: Any) -> None: ...

    @property
    def accounts(self) -> AccountList: ...

    @property
    def account(self) -> AccountContext: ...

    @account.setter
    def account(self, value: Any) -> None: ...

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
