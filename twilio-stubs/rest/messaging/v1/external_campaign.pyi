from twilio.base import deserialize as deserialize, values as values
from twilio.base.instance_resource import InstanceResource as InstanceResource
from twilio.base.list_resource import ListResource as ListResource
from twilio.base.page import Page as Page

class ExternalCampaignList(ListResource):
    def __init__(self, version) -> None: ...
    def create(self, campaign_id, messaging_service_sid): ...

class ExternalCampaignPage(Page):
    def __init__(self, version, response, solution) -> None: ...
    def get_instance(self, payload): ...

class ExternalCampaignInstance(InstanceResource):
    def __init__(self, version, payload) -> None: ...
    @property
    def sid(self): ...
    @property
    def account_sid(self): ...
    @property
    def campaign_id(self): ...
    @property
    def messaging_service_sid(self): ...
    @property
    def date_created(self): ...
