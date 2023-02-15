from twilio.base.version import Version as Version
from twilio.rest.bulkexports.v1.export import ExportList as ExportList
from twilio.rest.bulkexports.v1.export_configuration import ExportConfigurationList as ExportConfigurationList

class V1(Version):
    version: str
    def __init__(self, domain) -> None: ...
    @property
    def exports(self): ...
    @property
    def export_configuration(self): ...
