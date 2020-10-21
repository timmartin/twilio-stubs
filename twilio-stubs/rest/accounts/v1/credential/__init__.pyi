from twilio.base.instance_resource import InstanceResource as InstanceResource
from twilio.base.list_resource import ListResource as ListResource
from twilio.base.page import Page as Page
from twilio.rest.accounts.v1.credential.aws import AwsList as AwsList
from twilio.rest.accounts.v1.credential.public_key import PublicKeyList as PublicKeyList
from typing import Any

class CredentialList(ListResource):
    def __init__(self, version: Any) -> None: ...
    @property
    def public_key(self): ...
    @property
    def aws(self): ...

class CredentialPage(Page):
    def __init__(self, version: Any, response: Any, solution: Any) -> None: ...
    def get_instance(self, payload: Any): ...

class CredentialInstance(InstanceResource):
    def __init__(self, version: Any, payload: Any) -> None: ...
