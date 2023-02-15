from twilio.base import deserialize as deserialize, serialize as serialize, values as values
from twilio.base.instance_resource import InstanceResource as InstanceResource
from twilio.base.list_resource import ListResource as ListResource
from twilio.base.page import Page as Page

class SubscribeRulesList(ListResource):
    def __init__(self, version, room_sid, participant_sid) -> None: ...
    def fetch(self): ...
    def update(self, rules=...): ...

class SubscribeRulesPage(Page):
    def __init__(self, version, response, solution) -> None: ...
    def get_instance(self, payload): ...

class SubscribeRulesInstance(InstanceResource):
    def __init__(self, version, payload, room_sid, participant_sid) -> None: ...
    @property
    def participant_sid(self): ...
    @property
    def room_sid(self): ...
    @property
    def rules(self): ...
    @property
    def date_created(self): ...
    @property
    def date_updated(self): ...
