from twilio.base.instance_resource import InstanceResource as InstanceResource
from twilio.base.list_resource import ListResource as ListResource
from twilio.base.page import Page as Page
from twilio.rest.api.v2010.account.sip.domain.auth_types.auth_registrations_mapping.auth_registrations_credential_list_mapping import AuthRegistrationsCredentialListMappingList as AuthRegistrationsCredentialListMappingList
from typing import Any

class AuthTypeRegistrationsList(ListResource):
    def __init__(self, version: Any, account_sid: Any, domain_sid: Any) -> None: ...
    @property
    def credential_list_mappings(self): ...

class AuthTypeRegistrationsPage(Page):
    def __init__(self, version: Any, response: Any, solution: Any) -> None: ...
    def get_instance(self, payload: Any): ...

class AuthTypeRegistrationsInstance(InstanceResource):
    def __init__(self, version: Any, payload: Any, account_sid: Any, domain_sid: Any) -> None: ...
