from twilio.base.version import Version as Version
from twilio.rest.numbers.v2.regulatory_compliance import RegulatoryComplianceList as RegulatoryComplianceList

class V2(Version):
    version: str
    def __init__(self, domain) -> None: ...
    @property
    def regulatory_compliance(self): ...
