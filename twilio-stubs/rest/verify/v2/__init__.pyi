from twilio.base.version import Version as Version
from twilio.rest.verify.v2.form import FormList as FormList
from twilio.rest.verify.v2.safelist import SafelistList as SafelistList
from twilio.rest.verify.v2.service import ServiceList as ServiceList
from twilio.rest.verify.v2.template import TemplateList as TemplateList
from twilio.rest.verify.v2.verification_attempt import VerificationAttemptList as VerificationAttemptList
from twilio.rest.verify.v2.verification_attempts_summary import VerificationAttemptsSummaryList as VerificationAttemptsSummaryList

class V2(Version):
    version: str
    def __init__(self, domain) -> None: ...
    @property
    def forms(self): ...
    @property
    def safelist(self): ...
    @property
    def services(self): ...
    @property
    def verification_attempts(self): ...
    @property
    def verification_attempts_summary(self): ...
    @property
    def templates(self): ...
