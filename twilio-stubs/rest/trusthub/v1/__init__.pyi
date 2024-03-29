from twilio.base.version import Version as Version
from twilio.rest.trusthub.v1.customer_profiles import CustomerProfilesList as CustomerProfilesList
from twilio.rest.trusthub.v1.end_user import EndUserList as EndUserList
from twilio.rest.trusthub.v1.end_user_type import EndUserTypeList as EndUserTypeList
from twilio.rest.trusthub.v1.policies import PoliciesList as PoliciesList
from twilio.rest.trusthub.v1.supporting_document import SupportingDocumentList as SupportingDocumentList
from twilio.rest.trusthub.v1.supporting_document_type import SupportingDocumentTypeList as SupportingDocumentTypeList
from twilio.rest.trusthub.v1.trust_products import TrustProductsList as TrustProductsList

class V1(Version):
    version: str
    def __init__(self, domain) -> None: ...
    @property
    def customer_profiles(self): ...
    @property
    def end_users(self): ...
    @property
    def end_user_types(self): ...
    @property
    def policies(self): ...
    @property
    def supporting_documents(self): ...
    @property
    def supporting_document_types(self): ...
    @property
    def trust_products(self): ...
