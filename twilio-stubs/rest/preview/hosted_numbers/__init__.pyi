from twilio.base.version import Version as Version
from twilio.rest.preview.hosted_numbers.authorization_document import AuthorizationDocumentList as AuthorizationDocumentList
from twilio.rest.preview.hosted_numbers.hosted_number_order import HostedNumberOrderList as HostedNumberOrderList

class HostedNumbers(Version):
    version: str
    def __init__(self, domain) -> None: ...
    @property
    def authorization_documents(self): ...
    @property
    def hosted_number_orders(self): ...
