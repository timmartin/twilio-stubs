from twilio.base.domain import Domain as Domain
from twilio.rest.flex_api.v1 import V1 as V1
from twilio.rest.flex_api.v2 import V2 as V2

class FlexApi(Domain):
    base_url: str
    def __init__(self, twilio) -> None: ...
    @property
    def v1(self): ...
    @property
    def v2(self): ...
    @property
    def channel(self): ...
    @property
    def configuration(self): ...
    @property
    def flex_flow(self): ...
    @property
    def assessments(self): ...
    @property
    def insights_assessments_comment(self): ...
    @property
    def insights_questionnaires(self): ...
    @property
    def insights_questionnaires_category(self): ...
    @property
    def insights_questionnaires_question(self): ...
    @property
    def insights_segments(self): ...
    @property
    def insights_session(self): ...
    @property
    def insights_settings_answer_sets(self): ...
    @property
    def insights_settings_comment(self): ...
    @property
    def insights_user_roles(self): ...
    @property
    def interaction(self): ...
    @property
    def web_channel(self): ...
    @property
    def web_channels(self): ...
