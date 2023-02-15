from twilio.base.version import Version as Version
from twilio.rest.media.v1.media_processor import MediaProcessorList as MediaProcessorList
from twilio.rest.media.v1.media_recording import MediaRecordingList as MediaRecordingList
from twilio.rest.media.v1.player_streamer import PlayerStreamerList as PlayerStreamerList

class V1(Version):
    version: str
    def __init__(self, domain) -> None: ...
    @property
    def media_processor(self): ...
    @property
    def media_recording(self): ...
    @property
    def player_streamer(self): ...
