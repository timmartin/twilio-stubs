from twilio.base.instance_resource import InstanceResource as InstanceResource
from twilio.base.list_resource import ListResource as ListResource
from twilio.base.page import Page as Page
from twilio.rest.preview.trusted_comms.business.insights.impressions_rate import ImpressionsRateList as ImpressionsRateList
from typing import Any

class InsightsList(ListResource):
    def __init__(self, version: Any, business_sid: Any) -> None: ...
    @property
    def impressions_rate(self): ...

class InsightsPage(Page):
    def __init__(self, version: Any, response: Any, solution: Any) -> None: ...
    def get_instance(self, payload: Any): ...

class InsightsInstance(InstanceResource):
    def __init__(self, version: Any, payload: Any, business_sid: Any) -> None: ...
