from twilio.base.instance_resource import InstanceResource as InstanceResource
from twilio.base.list_resource import ListResource as ListResource
from twilio.base.page import Page as Page
from twilio.rest.api.v2010.account.sip.domain.auth_types.auth_calls_mapping.auth_calls_credential_list_mapping import AuthCallsCredentialListMappingList as AuthCallsCredentialListMappingList
from twilio.rest.api.v2010.account.sip.domain.auth_types.auth_calls_mapping.auth_calls_ip_access_control_list_mapping import AuthCallsIpAccessControlListMappingList as AuthCallsIpAccessControlListMappingList
from typing import Any

class AuthTypeCallsList(ListResource):
    def __init__(self, version: Any, account_sid: Any, domain_sid: Any) -> None: ...
    @property
    def credential_list_mappings(self): ...
    @property
    def ip_access_control_list_mappings(self): ...

class AuthTypeCallsPage(Page):
    def __init__(self, version: Any, response: Any, solution: Any) -> None: ...
    def get_instance(self, payload: Any): ...

class AuthTypeCallsInstance(InstanceResource):
    def __init__(self, version: Any, payload: Any, account_sid: Any, domain_sid: Any) -> None: ...
