from twilio.base.version import Version as Version
from twilio.rest.video.v1.composition import CompositionList as CompositionList
from twilio.rest.video.v1.composition_hook import CompositionHookList as CompositionHookList
from twilio.rest.video.v1.composition_settings import CompositionSettingsList as CompositionSettingsList
from twilio.rest.video.v1.recording import RecordingList as RecordingList
from twilio.rest.video.v1.recording_settings import RecordingSettingsList as RecordingSettingsList
from twilio.rest.video.v1.room import RoomList as RoomList

class V1(Version):
    version: str
    def __init__(self, domain) -> None: ...
    @property
    def compositions(self): ...
    @property
    def composition_hooks(self): ...
    @property
    def composition_settings(self): ...
    @property
    def recordings(self): ...
    @property
    def recording_settings(self): ...
    @property
    def rooms(self): ...
