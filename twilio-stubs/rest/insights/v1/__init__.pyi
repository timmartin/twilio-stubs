from twilio.base.version import Version as Version
from twilio.rest.insights.v1.call import CallList as CallList
from twilio.rest.insights.v1.call_summaries import CallSummariesList as CallSummariesList
from twilio.rest.insights.v1.conference import ConferenceList as ConferenceList
from twilio.rest.insights.v1.room import RoomList as RoomList
from twilio.rest.insights.v1.setting import SettingList as SettingList

class V1(Version):
    version: str
    def __init__(self, domain) -> None: ...
    @property
    def settings(self): ...
    @property
    def calls(self): ...
    @property
    def call_summaries(self): ...
    @property
    def conferences(self): ...
    @property
    def rooms(self): ...
