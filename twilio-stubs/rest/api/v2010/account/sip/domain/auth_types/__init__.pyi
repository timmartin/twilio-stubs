from twilio.base.instance_resource import InstanceResource as InstanceResource
from twilio.base.list_resource import ListResource as ListResource
from twilio.base.page import Page as Page
from twilio.rest.api.v2010.account.sip.domain.auth_types.auth_calls_mapping import AuthTypeCallsList as AuthTypeCallsList
from twilio.rest.api.v2010.account.sip.domain.auth_types.auth_registrations_mapping import AuthTypeRegistrationsList as AuthTypeRegistrationsList

class AuthTypesList(ListResource):
    def __init__(self, version, account_sid, domain_sid) -> None: ...
    @property
    def calls(self): ...
    @property
    def registrations(self): ...

class AuthTypesPage(Page):
    def __init__(self, version, response, solution) -> None: ...
    def get_instance(self, payload): ...

class AuthTypesInstance(InstanceResource):
    def __init__(self, version, payload, account_sid, domain_sid) -> None: ...
