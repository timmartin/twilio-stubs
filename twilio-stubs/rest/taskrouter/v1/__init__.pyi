from twilio.base.version import Version as Version
from twilio.rest.taskrouter.v1.workspace import WorkspaceList as WorkspaceList

class V1(Version):
    version: str
    def __init__(self, domain) -> None: ...
    @property
    def workspaces(self): ...
