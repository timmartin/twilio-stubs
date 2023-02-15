from _typeshed import Incomplete
from twilio.base import deserialize as deserialize, serialize as serialize, values as values
from twilio.base.instance_resource import InstanceResource as InstanceResource
from twilio.base.list_resource import ListResource as ListResource
from twilio.base.page import Page as Page
from twilio.rest.api.v2010.account.usage.record.all_time import AllTimeList as AllTimeList
from twilio.rest.api.v2010.account.usage.record.daily import DailyList as DailyList
from twilio.rest.api.v2010.account.usage.record.last_month import LastMonthList as LastMonthList
from twilio.rest.api.v2010.account.usage.record.monthly import MonthlyList as MonthlyList
from twilio.rest.api.v2010.account.usage.record.this_month import ThisMonthList as ThisMonthList
from twilio.rest.api.v2010.account.usage.record.today import TodayList as TodayList
from twilio.rest.api.v2010.account.usage.record.yearly import YearlyList as YearlyList
from twilio.rest.api.v2010.account.usage.record.yesterday import YesterdayList as YesterdayList

class RecordList(ListResource):
    def __init__(self, version, account_sid) -> None: ...
    def stream(self, category=..., start_date=..., end_date=..., include_subaccounts=..., limit: Incomplete | None = ..., page_size: Incomplete | None = ...): ...
    def list(self, category=..., start_date=..., end_date=..., include_subaccounts=..., limit: Incomplete | None = ..., page_size: Incomplete | None = ...): ...
    def page(self, category=..., start_date=..., end_date=..., include_subaccounts=..., page_token=..., page_number=..., page_size=...): ...
    def get_page(self, target_url): ...
    @property
    def all_time(self): ...
    @property
    def daily(self): ...
    @property
    def last_month(self): ...
    @property
    def monthly(self): ...
    @property
    def this_month(self): ...
    @property
    def today(self): ...
    @property
    def yearly(self): ...
    @property
    def yesterday(self): ...

class RecordPage(Page):
    def __init__(self, version, response, solution) -> None: ...
    def get_instance(self, payload): ...

class RecordInstance(InstanceResource):
    class Category:
        A2P_REGISTRATION_FEES: str
        AGENT_CONFERENCE: str
        AMAZON_POLLY: str
        ANSWERING_MACHINE_DETECTION: str
        AUTHY_AUTHENTICATIONS: str
        AUTHY_CALLS_OUTBOUND: str
        AUTHY_MONTHLY_FEES: str
        AUTHY_PHONE_INTELLIGENCE: str
        AUTHY_PHONE_VERIFICATIONS: str
        AUTHY_SMS_OUTBOUND: str
        CALL_PROGESS_EVENTS: str
        CALLERIDLOOKUPS: str
        CALLS: str
        CALLS_CLIENT: str
        CALLS_GLOBALCONFERENCE: str
        CALLS_INBOUND: str
        CALLS_INBOUND_LOCAL: str
        CALLS_INBOUND_MOBILE: str
        CALLS_INBOUND_TOLLFREE: str
        CALLS_OUTBOUND: str
        CALLS_PAY_VERB_TRANSACTIONS: str
        CALLS_RECORDINGS: str
        CALLS_SIP: str
        CALLS_SIP_INBOUND: str
        CALLS_SIP_OUTBOUND: str
        CALLS_TRANSFERS: str
        CARRIER_LOOKUPS: str
        CONVERSATIONS: str
        CONVERSATIONS_API_REQUESTS: str
        CONVERSATIONS_CONVERSATION_EVENTS: str
        CONVERSATIONS_ENDPOINT_CONNECTIVITY: str
        CONVERSATIONS_EVENTS: str
        CONVERSATIONS_PARTICIPANT_EVENTS: str
        CONVERSATIONS_PARTICIPANTS: str
        CPS: str
        FLEX_USAGE: str
        FRAUD_LOOKUPS: str
        GROUP_ROOMS: str
        GROUP_ROOMS_DATA_TRACK: str
        GROUP_ROOMS_ENCRYPTED_MEDIA_RECORDED: str
        GROUP_ROOMS_MEDIA_DOWNLOADED: str
        GROUP_ROOMS_MEDIA_RECORDED: str
        GROUP_ROOMS_MEDIA_ROUTED: str
        GROUP_ROOMS_MEDIA_STORED: str
        GROUP_ROOMS_PARTICIPANT_MINUTES: str
        GROUP_ROOMS_RECORDED_MINUTES: str
        IMP_V1_USAGE: str
        LOOKUPS: str
        MARKETPLACE: str
        MARKETPLACE_ALGORITHMIA_NAMED_ENTITY_RECOGNITION: str
        MARKETPLACE_CADENCE_TRANSCRIPTION: str
        MARKETPLACE_CADENCE_TRANSLATION: str
        MARKETPLACE_CAPIO_SPEECH_TO_TEXT: str
        MARKETPLACE_CONVRIZA_ABABA: str
        MARKETPLACE_DEEPGRAM_PHRASE_DETECTOR: str
        MARKETPLACE_DIGITAL_SEGMENT_BUSINESS_INFO: str
        MARKETPLACE_FACEBOOK_OFFLINE_CONVERSIONS: str
        MARKETPLACE_GOOGLE_SPEECH_TO_TEXT: str
        MARKETPLACE_IBM_WATSON_MESSAGE_INSIGHTS: str
        MARKETPLACE_IBM_WATSON_MESSAGE_SENTIMENT: str
        MARKETPLACE_IBM_WATSON_RECORDING_ANALYSIS: str
        MARKETPLACE_IBM_WATSON_TONE_ANALYZER: str
        MARKETPLACE_ICEHOOK_SYSTEMS_SCOUT: str
        MARKETPLACE_INFOGROUP_DATAAXLE_BIZINFO: str
        MARKETPLACE_KEEN_IO_CONTACT_CENTER_ANALYTICS: str
        MARKETPLACE_MARCHEX_CLEANCALL: str
        MARKETPLACE_MARCHEX_SENTIMENT_ANALYSIS_FOR_SMS: str
        MARKETPLACE_MARKETPLACE_NEXTCALLER_SOCIAL_ID: str
        MARKETPLACE_MOBILE_COMMONS_OPT_OUT_CLASSIFIER: str
        MARKETPLACE_NEXIWAVE_VOICEMAIL_TO_TEXT: str
        MARKETPLACE_NEXTCALLER_ADVANCED_CALLER_IDENTIFICATION: str
        MARKETPLACE_NOMOROBO_SPAM_SCORE: str
        MARKETPLACE_PAYFONE_TCPA_COMPLIANCE: str
        MARKETPLACE_REMEETING_AUTOMATIC_SPEECH_RECOGNITION: str
        MARKETPLACE_TCPA_DEFENSE_SOLUTIONS_BLACKLIST_FEED: str
        MARKETPLACE_TELO_OPENCNAM: str
        MARKETPLACE_TRUECNAM_TRUE_SPAM: str
        MARKETPLACE_TWILIO_CALLER_NAME_LOOKUP_US: str
        MARKETPLACE_TWILIO_CARRIER_INFORMATION_LOOKUP: str
        MARKETPLACE_VOICEBASE_PCI: str
        MARKETPLACE_VOICEBASE_TRANSCRIPTION: str
        MARKETPLACE_VOICEBASE_TRANSCRIPTION_CUSTOM_VOCABULARY: str
        MARKETPLACE_WHITEPAGES_PRO_CALLER_IDENTIFICATION: str
        MARKETPLACE_WHITEPAGES_PRO_PHONE_INTELLIGENCE: str
        MARKETPLACE_WHITEPAGES_PRO_PHONE_REPUTATION: str
        MARKETPLACE_WOLFARM_SPOKEN_RESULTS: str
        MARKETPLACE_WOLFRAM_SHORT_ANSWER: str
        MARKETPLACE_YTICA_CONTACT_CENTER_REPORTING_ANALYTICS: str
        MEDIASTORAGE: str
        MMS: str
        MMS_INBOUND: str
        MMS_INBOUND_LONGCODE: str
        MMS_INBOUND_SHORTCODE: str
        MMS_MESSAGES_CARRIERFEES: str
        MMS_OUTBOUND: str
        MMS_OUTBOUND_LONGCODE: str
        MMS_OUTBOUND_SHORTCODE: str
        MONITOR_READS: str
        MONITOR_STORAGE: str
        MONITOR_WRITES: str
        NOTIFY: str
        NOTIFY_ACTIONS_ATTEMPTS: str
        NOTIFY_CHANNELS: str
        NUMBER_FORMAT_LOOKUPS: str
        PCHAT: str
        PCHAT_USERS: str
        PEER_TO_PEER_ROOMS_PARTICIPANT_MINUTES: str
        PFAX: str
        PFAX_MINUTES: str
        PFAX_MINUTES_INBOUND: str
        PFAX_MINUTES_OUTBOUND: str
        PFAX_PAGES: str
        PHONENUMBERS: str
        PHONENUMBERS_CPS: str
        PHONENUMBERS_EMERGENCY: str
        PHONENUMBERS_LOCAL: str
        PHONENUMBERS_MOBILE: str
        PHONENUMBERS_SETUPS: str
        PHONENUMBERS_TOLLFREE: str
        PREMIUMSUPPORT: str
        PROXY: str
        PROXY_ACTIVE_SESSIONS: str
        PSTNCONNECTIVITY: str
        PV: str
        PV_COMPOSITION_MEDIA_DOWNLOADED: str
        PV_COMPOSITION_MEDIA_ENCRYPTED: str
        PV_COMPOSITION_MEDIA_STORED: str
        PV_COMPOSITION_MINUTES: str
        PV_RECORDING_COMPOSITIONS: str
        PV_ROOM_PARTICIPANTS: str
        PV_ROOM_PARTICIPANTS_AU1: str
        PV_ROOM_PARTICIPANTS_BR1: str
        PV_ROOM_PARTICIPANTS_IE1: str
        PV_ROOM_PARTICIPANTS_JP1: str
        PV_ROOM_PARTICIPANTS_SG1: str
        PV_ROOM_PARTICIPANTS_US1: str
        PV_ROOM_PARTICIPANTS_US2: str
        PV_ROOMS: str
        PV_SIP_ENDPOINT_REGISTRATIONS: str
        RECORDINGS: str
        RECORDINGSTORAGE: str
        ROOMS_GROUP_BANDWIDTH: str
        ROOMS_GROUP_MINUTES: str
        ROOMS_PEER_TO_PEER_MINUTES: str
        SHORTCODES: str
        SHORTCODES_CUSTOMEROWNED: str
        SHORTCODES_MMS_ENABLEMENT: str
        SHORTCODES_MPS: str
        SHORTCODES_RANDOM: str
        SHORTCODES_UK: str
        SHORTCODES_VANITY: str
        SMALL_GROUP_ROOMS: str
        SMALL_GROUP_ROOMS_DATA_TRACK: str
        SMALL_GROUP_ROOMS_PARTICIPANT_MINUTES: str
        SMS: str
        SMS_INBOUND: str
        SMS_INBOUND_LONGCODE: str
        SMS_INBOUND_SHORTCODE: str
        SMS_MESSAGES_CARRIERFEES: str
        SMS_MESSAGES_FEATURES: str
        SMS_MESSAGES_FEATURES_SENDERID: str
        SMS_OUTBOUND: str
        SMS_OUTBOUND_CONTENT_INSPECTION: str
        SMS_OUTBOUND_LONGCODE: str
        SMS_OUTBOUND_SHORTCODE: str
        SPEECH_RECOGNITION: str
        STUDIO_ENGAGEMENTS: str
        SYNC: str
        SYNC_ACTIONS: str
        SYNC_ENDPOINT_HOURS: str
        SYNC_ENDPOINT_HOURS_ABOVE_DAILY_CAP: str
        TASKROUTER_TASKS: str
        TOTALPRICE: str
        TRANSCRIPTIONS: str
        TRUNKING_CPS: str
        TRUNKING_EMERGENCY_CALLS: str
        TRUNKING_ORIGINATION: str
        TRUNKING_ORIGINATION_LOCAL: str
        TRUNKING_ORIGINATION_MOBILE: str
        TRUNKING_ORIGINATION_TOLLFREE: str
        TRUNKING_RECORDINGS: str
        TRUNKING_SECURE: str
        TRUNKING_TERMINATION: str
        TURNMEGABYTES: str
        TURNMEGABYTES_AUSTRALIA: str
        TURNMEGABYTES_BRASIL: str
        TURNMEGABYTES_GERMANY: str
        TURNMEGABYTES_INDIA: str
        TURNMEGABYTES_IRELAND: str
        TURNMEGABYTES_JAPAN: str
        TURNMEGABYTES_SINGAPORE: str
        TURNMEGABYTES_USEAST: str
        TURNMEGABYTES_USWEST: str
        TWILIO_INTERCONNECT: str
        VERIFY_PUSH: str
        VERIFY_TOTP: str
        VERIFY_WHATSAPP_CONVERSATIONS_BUSINESS_INITIATED: str
        VIDEO_RECORDINGS: str
        VIRTUAL_AGENT: str
        VOICE_INSIGHTS: str
        VOICE_INSIGHTS_CLIENT_INSIGHTS_ON_DEMAND_MINUTE: str
        VOICE_INSIGHTS_PTSN_INSIGHTS_ON_DEMAND_MINUTE: str
        VOICE_INSIGHTS_SIP_INTERFACE_INSIGHTS_ON_DEMAND_MINUTE: str
        VOICE_INSIGHTS_SIP_TRUNKING_INSIGHTS_ON_DEMAND_MINUTE: str
        WIRELESS: str
        WIRELESS_ORDERS: str
        WIRELESS_ORDERS_ARTWORK: str
        WIRELESS_ORDERS_BULK: str
        WIRELESS_ORDERS_ESIM: str
        WIRELESS_ORDERS_STARTER: str
        WIRELESS_USAGE: str
        WIRELESS_USAGE_COMMANDS: str
        WIRELESS_USAGE_COMMANDS_AFRICA: str
        WIRELESS_USAGE_COMMANDS_ASIA: str
        WIRELESS_USAGE_COMMANDS_CENTRALANDSOUTHAMERICA: str
        WIRELESS_USAGE_COMMANDS_EUROPE: str
        WIRELESS_USAGE_COMMANDS_HOME: str
        WIRELESS_USAGE_COMMANDS_NORTHAMERICA: str
        WIRELESS_USAGE_COMMANDS_OCEANIA: str
        WIRELESS_USAGE_COMMANDS_ROAMING: str
        WIRELESS_USAGE_DATA: str
        WIRELESS_USAGE_DATA_AFRICA: str
        WIRELESS_USAGE_DATA_ASIA: str
        WIRELESS_USAGE_DATA_CENTRALANDSOUTHAMERICA: str
        WIRELESS_USAGE_DATA_CUSTOM_ADDITIONALMB: str
        WIRELESS_USAGE_DATA_CUSTOM_FIRST5MB: str
        WIRELESS_USAGE_DATA_DOMESTIC_ROAMING: str
        WIRELESS_USAGE_DATA_EUROPE: str
        WIRELESS_USAGE_DATA_INDIVIDUAL_ADDITIONALGB: str
        WIRELESS_USAGE_DATA_INDIVIDUAL_FIRSTGB: str
        WIRELESS_USAGE_DATA_INTERNATIONAL_ROAMING_CANADA: str
        WIRELESS_USAGE_DATA_INTERNATIONAL_ROAMING_INDIA: str
        WIRELESS_USAGE_DATA_INTERNATIONAL_ROAMING_MEXICO: str
        WIRELESS_USAGE_DATA_NORTHAMERICA: str
        WIRELESS_USAGE_DATA_OCEANIA: str
        WIRELESS_USAGE_DATA_POOLED: str
        WIRELESS_USAGE_DATA_POOLED_DOWNLINK: str
        WIRELESS_USAGE_DATA_POOLED_UPLINK: str
        WIRELESS_USAGE_MRC: str
        WIRELESS_USAGE_MRC_CUSTOM: str
        WIRELESS_USAGE_MRC_INDIVIDUAL: str
        WIRELESS_USAGE_MRC_POOLED: str
        WIRELESS_USAGE_MRC_SUSPENDED: str
        WIRELESS_USAGE_SMS: str
        WIRELESS_USAGE_VOICE: str
    def __init__(self, version, payload, account_sid) -> None: ...
    @property
    def account_sid(self): ...
    @property
    def api_version(self): ...
    @property
    def as_of(self): ...
    @property
    def category(self): ...
    @property
    def count(self): ...
    @property
    def count_unit(self): ...
    @property
    def description(self): ...
    @property
    def end_date(self): ...
    @property
    def price(self): ...
    @property
    def price_unit(self): ...
    @property
    def start_date(self): ...
    @property
    def subresource_uris(self): ...
    @property
    def uri(self): ...
    @property
    def usage(self): ...
    @property
    def usage_unit(self): ...
